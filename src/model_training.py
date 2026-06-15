"""Train and compare five regression models for YouTube ad revenue."""

from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import Lasso, LinearRegression, Ridge
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from evaluation import rank_models, regression_metrics
from feature_engineering import add_engineered_features
from preprocessing import (
    CATEGORICAL_COLUMNS,
    FEATURE_COLUMNS,
    NUMERIC_COLUMNS,
    clean_dataset,
    split_features_target,
)


def build_preprocessor() -> ColumnTransformer:
    """Build encoding and scaling steps used by every model."""
    return ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), NUMERIC_COLUMNS),
            ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), CATEGORICAL_COLUMNS),
        ]
    )


def get_models() -> dict[str, object]:
    """Return exactly five beginner-friendly regression models."""
    return {
        "Linear Regression": LinearRegression(),
        "Ridge Regression": Ridge(alpha=1.0),
        "Lasso Regression": Lasso(alpha=0.05, max_iter=5000),
        "Random Forest Regressor": RandomForestRegressor(
            n_estimators=80, max_depth=16, random_state=42, n_jobs=-1
        ),
        "Gradient Boosting Regressor": GradientBoostingRegressor(
            n_estimators=120, learning_rate=0.08, max_depth=3, random_state=42
        ),
    }


def train_models(raw_df: pd.DataFrame, model_dir: str | Path, results_dir: str | Path):
    """Clean data, engineer features, train models, and save the best model."""
    model_dir = Path(model_dir)
    results_dir = Path(results_dir)
    model_dir.mkdir(parents=True, exist_ok=True)
    results_dir.mkdir(parents=True, exist_ok=True)

    cleaned = clean_dataset(raw_df)
    prepared = add_engineered_features(cleaned)
    X, y = split_features_target(prepared)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    results = []
    trained_pipelines = {}

    for name, model in get_models().items():
        pipeline = Pipeline(
            steps=[
                ("preprocessor", build_preprocessor()),
                ("model", model),
            ]
        )
        pipeline.fit(X_train[FEATURE_COLUMNS], y_train)
        predictions = pipeline.predict(X_test[FEATURE_COLUMNS])
        metrics = regression_metrics(y_test, predictions)
        results.append({"Model": name, **metrics})
        trained_pipelines[name] = pipeline

    comparison = rank_models(results)
    best_name = comparison.loc[0, "Model"]
    best_pipeline = trained_pipelines[best_name]

    joblib.dump(best_pipeline, model_dir / "best_model.pkl")
    joblib.dump(best_pipeline.named_steps["preprocessor"], model_dir / "scaler.pkl")
    joblib.dump(
        {
            "feature_columns": FEATURE_COLUMNS,
            "numeric_columns": NUMERIC_COLUMNS,
            "categorical_columns": CATEGORICAL_COLUMNS,
            "best_model": best_name,
        },
        model_dir / "model_metadata.pkl",
    )

    comparison.to_csv(results_dir / "model_comparison.csv", index=False)
    prepared.to_csv(results_dir.parent.parent / "data" / "processed" / "cleaned_youtube_revenue.csv", index=False)

    sample_predictions = X_test.copy()
    sample_predictions["actual_revenue"] = y_test.values
    sample_predictions["predicted_revenue"] = best_pipeline.predict(X_test)
    sample_predictions.head(200).to_csv(results_dir / "sample_predictions.csv", index=False)

    return comparison, best_name, best_pipeline, prepared
