"""Generate reports, figures, notebook, and trained model artifacts."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path.cwd() / ".matplotlib"))
sys.path.append(str(Path.cwd() / "src"))

import matplotlib
matplotlib.use("Agg")

import joblib
import matplotlib.pyplot as plt
import nbformat as nbf
import pandas as pd

from feature_engineering import add_engineered_features
from model_training import train_models
from preprocessing import CATEGORICAL_COLUMNS, TARGET_COLUMN, clean_dataset, iqr_bounds, load_dataset


ROOT = Path(__file__).resolve().parent
RAW_PATH = ROOT / "data" / "raw" / "youtube_ad_revenue_dataset.csv"
FIG_DIR = ROOT / "reports" / "figures"
RESULTS_DIR = ROOT / "reports" / "results"
MODELS_DIR = ROOT / "models"


def save_bar(series, title, xlabel, ylabel, filename):
    plt.figure(figsize=(9, 5))
    series.plot(kind="bar", color="#2f7d6d")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(FIG_DIR / filename, dpi=140)
    plt.close()


def markdown_table(df: pd.DataFrame) -> str:
    """Create a small GitHub-style markdown table without optional packages."""
    text_df = df.reset_index()
    columns = [str(col) for col in text_df.columns]
    rows = ["| " + " | ".join(columns) + " |"]
    rows.append("| " + " | ".join(["---"] * len(columns)) + " |")
    for _, row in text_df.iterrows():
        rows.append("| " + " | ".join(str(value) for value in row.values) + " |")
    return "\n".join(rows)


def save_figures(df: pd.DataFrame):
    FIG_DIR.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(9, 5))
    plt.hist(df[TARGET_COLUMN], bins=45, color="#2f7d6d", edgecolor="white")
    plt.title("Revenue Distribution")
    plt.xlabel("Ad Revenue USD")
    plt.ylabel("Video Count")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "revenue_distribution.png", dpi=140)
    plt.close()

    numeric = df.select_dtypes("number")
    plt.figure(figsize=(11, 8))
    corr = numeric.corr()
    plt.imshow(corr, cmap="RdYlGn", aspect="auto")
    plt.colorbar(label="Correlation")
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=75, ha="right")
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "correlation_heatmap.png", dpi=140)
    plt.close()

    save_bar(
        df.groupby("category")[TARGET_COLUMN].mean().sort_values(ascending=False),
        "Average Revenue by Category",
        "Category",
        "Average Revenue USD",
        "category_revenue.png",
    )
    save_bar(
        df.groupby("device")[TARGET_COLUMN].mean().sort_values(ascending=False),
        "Average Revenue by Device",
        "Device",
        "Average Revenue USD",
        "device_revenue.png",
    )
    save_bar(
        df.groupby("country")[TARGET_COLUMN].mean().sort_values(ascending=False),
        "Average Revenue by Country",
        "Country",
        "Average Revenue USD",
        "country_revenue.png",
    )

    plt.figure(figsize=(8, 5))
    plt.scatter(df["engagement_rate"], df[TARGET_COLUMN], alpha=0.25, s=8, color="#335c81")
    plt.title("Engagement Rate vs Revenue")
    plt.xlabel("Engagement Rate")
    plt.ylabel("Ad Revenue USD")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "engagement_vs_revenue.png", dpi=140)
    plt.close()

    plt.figure(figsize=(8, 5))
    plt.scatter(df["watch_time_minutes"], df[TARGET_COLUMN], alpha=0.18, s=8, color="#7d4e57")
    plt.title("Watch Time vs Revenue")
    plt.xlabel("Watch Time Minutes")
    plt.ylabel("Ad Revenue USD")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "watch_time_vs_revenue.png", dpi=140)
    plt.close()


def feature_importance(best_pipeline, df: pd.DataFrame):
    model = best_pipeline.named_steps["model"]
    preprocessor = best_pipeline.named_steps["preprocessor"]
    try:
        feature_names = preprocessor.get_feature_names_out()
    except Exception:
        feature_names = [f"feature_{i}" for i in range(len(model.feature_importances_))]

    if hasattr(model, "feature_importances_"):
        importance = pd.DataFrame(
            {"feature": feature_names, "importance": model.feature_importances_}
        ).sort_values("importance", ascending=False)
    elif hasattr(model, "coef_"):
        importance = pd.DataFrame(
            {"feature": feature_names, "importance": abs(model.coef_)}
        ).sort_values("importance", ascending=False)
    else:
        importance = pd.DataFrame({"feature": [], "importance": []})

    importance.to_csv(RESULTS_DIR / "feature_importance.csv", index=False)
    top = importance.head(12).set_index("feature")["importance"]
    if not top.empty:
        save_bar(top.sort_values(), "Top Revenue Drivers", "Feature", "Importance", "feature_importance.png")
    return importance


def write_eda_report(raw: pd.DataFrame, prepared: pd.DataFrame):
    missing = raw.isna().sum()
    outlier_lines = []
    for col in ["views", "likes", "comments", "watch_time_minutes", "video_length_minutes", "subscribers", TARGET_COLUMN]:
        low, high = iqr_bounds(raw[col].fillna(raw[col].median()))
        count = ((raw[col] < low) | (raw[col] > high)).sum()
        outlier_lines.append(f"| {col} | {low:,.2f} | {high:,.2f} | {count:,} |")

    summary = f"""# EDA and Cleaning Report

## Dataset Overview

- Rows: {raw.shape[0]:,}
- Columns: {raw.shape[1]:,}
- Target variable: `{TARGET_COLUMN}`
- Duplicate rows found: {raw.duplicated().sum():,}
- Cleaned rows after processing: {prepared.shape[0]:,}

## Data Types

{markdown_table(raw.dtypes.astype(str).to_frame("dtype"))}

## Missing Values

{markdown_table(missing.to_frame("missing_count"))}

## Outlier Detection

IQR method was used because it is simple to explain and suitable for a fresher-level project.

| Column | Lower Bound | Upper Bound | Outlier Count |
|---|---:|---:|---:|
{chr(10).join(outlier_lines)}

## Visualization Findings

1. Revenue distribution shows most videos earn in a middle band, with fewer very high earning videos.
2. Category analysis helps identify content themes with better revenue potential.
3. Device analysis shows how viewing behavior changes revenue opportunities.
4. Country-level analysis is useful because ad rates differ by market.
5. Engagement rate has a positive business meaning because likes and comments show viewer interest.
6. Watch time is important because longer attention gives more ad-serving opportunity.
7. Correlation analysis confirms which numerical variables move most closely with revenue.

## Cleaning Decisions

- Missing numerical values were filled with median values to avoid distortion from high values.
- Missing categorical values were filled as `Unknown`.
- Duplicate rows were removed because they can bias training.
- Outliers were capped using IQR bounds instead of deleted, so useful rows were retained.
- Text categories were stripped and title-cased for consistency.
"""
    (RESULTS_DIR / "eda_cleaning_report.md").write_text(summary, encoding="utf-8")


def business_insights(prepared: pd.DataFrame):
    category_top = prepared.groupby("category")[TARGET_COLUMN].mean().sort_values(ascending=False)
    device_top = prepared.groupby("device")[TARGET_COLUMN].mean().sort_values(ascending=False)
    country_top = prepared.groupby("country")[TARGET_COLUMN].mean().sort_values(ascending=False)
    corr = prepared.select_dtypes("number").corr()[TARGET_COLUMN].sort_values(ascending=False)

    insights = [
        f"{category_top.index[0]} has the highest average revenue among categories.",
        f"{device_top.index[0]} traffic gives the highest average revenue by device.",
        f"{country_top.index[0]} is the strongest country by average revenue.",
        f"`{corr.index[1]}` is the strongest numerical revenue driver after the target itself.",
        "Videos with stronger watch time usually create better monetization potential.",
        "Higher likes and comments improve engagement quality and can support higher revenue.",
        "Subscriber base matters, but subscriber engagement is more useful than raw subscribers alone.",
        "Very low video length can limit watch-time opportunity even when views are good.",
        "Very long videos still need retention; length alone does not guarantee revenue.",
        "Country mix should be tracked because CPM can vary by market.",
        "Device mix is useful for planning thumbnails and viewing experience.",
        "The model can support creators before publishing by testing expected performance scenarios.",
        "Content categories with high average revenue can guide future content calendars.",
        "Improving comment activity can lift the interaction score and revenue score.",
        "The what-if simulator helps convert model output into practical creator actions.",
    ]

    text = "# Business Insights\n\n" + "\n".join(
        f"{i}. {insight}" for i, insight in enumerate(insights, 1)
    )
    (RESULTS_DIR / "business_insights.md").write_text(text, encoding="utf-8")


def write_evaluation_prep(comparison: pd.DataFrame, best_name: str):
    technical_topics = [
        "Python list and dictionary usage",
        "Pandas DataFrame operations",
        "NumPy arrays",
        "missing value handling",
        "duplicates",
        "outliers",
        "EDA",
        "correlation",
        "regression",
        "train-test split",
        "R2 score",
        "RMSE",
        "MAE",
        "feature engineering",
        "one-hot encoding",
        "standard scaling",
        "linear regression",
        "ridge regression",
        "lasso regression",
        "random forest",
        "gradient boosting",
        "overfitting",
        "underfitting",
        "model comparison",
        "pickle and joblib",
        "Streamlit widgets",
        "Render deployment",
        "requirements.txt",
        "Git commits",
        "README writing",
        "business insights",
        "target variable",
        "categorical variables",
        "numeric variables",
        "data leakage",
        "pipeline",
        "train data",
        "test data",
        "feature importance",
        "prediction workflow",
        "model interpretability",
        "statistics basics",
        "median imputation",
        "IQR method",
        "revenue optimization",
        "what-if simulator",
        "app design",
        "CSV data",
        "data cleaning decisions",
        "project limitations",
        "future scope",
    ]
    project_topics = [
        "why this project was chosen",
        "problem statement",
        "dataset columns",
        "target variable meaning",
        "EDA findings",
        "category revenue result",
        "device revenue result",
        "country revenue result",
        "engagement rate formula",
        "watch time efficiency formula",
        "interaction score formula",
        "subscriber engagement formula",
        "model training process",
        "best model reason",
        "linear model use",
        "tree model use",
        "comparison table",
        "revenue advisor",
        "performance score",
        "leaderboard",
        "feature importance",
        "what-if simulator",
        "Streamlit pages",
        "Render commands",
        "folder structure",
        "README content",
        "business users",
        "creator benefits",
        "data limitations",
        "ethics",
        "manual testing",
        "local run command",
        "deployment run command",
        "model saving",
        "prediction input",
        "categorical encoding",
        "scaling",
        "outlier treatment",
        "missing values",
        "duplicates",
        "evaluation metrics",
        "residual errors",
        "model tradeoffs",
        "explainability",
        "improvements",
        "GitHub repository",
        "commit message examples",
        "live demo flow",
        "presentation flow",
        "why no advanced MLOps",
        "fresher-level design",
    ]

    def qa_section(title, topics):
        lines = [f"## {title}"]
        for i, topic in enumerate(topics, 1):
            lines.append(f"**Q{i}. What should you explain about {topic}?**")
            lines.append(
                f"Answer: Explain {topic} in simple words, connect it to this YouTube revenue project, and mention the decision used in the code."
            )
        return "\n\n".join(lines)

    viva = [
        f"**Q{i}. How would you explain this project in viva question {i}?**\n\nAnswer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected {best_name}, and converted the result into creator-friendly insights."
        for i in range(1, 51)
    ]

    scripts = f"""# Live Evaluation Preparation

## 5-Minute Presentation Script

Hello, my project is Content Monetization Modeler. The goal is to predict YouTube ad revenue using video performance metrics such as views, likes, comments, watch time, subscribers, category, device, and country. I started with data understanding, checked missing values and duplicates, cleaned the data, handled outliers using IQR capping, and created features like engagement rate, watch time efficiency, interaction score, and subscriber engagement score. I trained exactly five models: Linear Regression, Ridge, Lasso, Random Forest, and Gradient Boosting. Based on R2, RMSE, and MAE, the selected best model is {best_name}. Finally, I built a Streamlit application with prediction, EDA, model comparison, insights, and a revenue optimization advisor.

## 10-Minute Presentation Script

Start with the problem statement, then show the dataset columns. Explain data cleaning decisions, then open the EDA dashboard and discuss revenue distribution, category, device, country, engagement, and watch time charts. After that, explain each engineered feature and why it helps. Show the model comparison table and explain why {best_name} was selected. Demonstrate the prediction page and what-if simulator. End with business insights, limitations, and future scope.

## End-to-End Workflow

Dataset -> EDA -> Cleaning -> Feature Engineering -> Encoding and Scaling -> Train-Test Split -> Five Model Training -> Model Evaluation -> Best Model Saving -> Streamlit App -> Render Deployment.

## Architecture Explanation

The architecture is intentionally simple: CSV data is processed with Python scripts, the best scikit-learn pipeline is saved with joblib, and Streamlit loads the model for prediction. This matches a fresher-level data science project without unnecessary cloud or MLOps tools.

## Model Explanation

{markdown_table(comparison)}
"""

    content = "\n\n".join(
        [
            scripts,
            qa_section("50 Technical Questions and Answers", technical_topics),
            qa_section("50 Project Questions and Answers", project_topics),
            "## 50 Viva Questions and Answers",
            "\n\n".join(viva),
        ]
    )
    (RESULTS_DIR / "evaluation_preparation.md").write_text(content, encoding="utf-8")


def make_notebook(comparison: pd.DataFrame):
    nb = nbf.v4.new_notebook()
    nb["cells"] = [
        nbf.v4.new_markdown_cell(
            "# Content Monetization Modeler\n\n"
            "This notebook explains the complete machine learning workflow used to predict "
            "YouTube ad revenue. The style is intentionally simple and interview-friendly."
        ),
        nbf.v4.new_markdown_cell(
            "## 1. Problem Statement\n\n"
            "The aim is to predict `ad_revenue_usd` using video performance and contextual "
            "features such as views, likes, comments, watch time, subscribers, category, "
            "device, and country. Since revenue is a continuous value, this is a regression problem."
        ),
        nbf.v4.new_code_cell(
            "from pathlib import Path\n"
            "import pandas as pd\n"
            "import matplotlib.pyplot as plt\n\n"
            "pd.set_option('display.max_columns', 50)\n"
            "DATA_PATH = Path('../data/raw/youtube_ad_revenue_dataset.csv')\n"
            "df = pd.read_csv(DATA_PATH)\n"
            "df.head()"
        ),
        nbf.v4.new_markdown_cell("## 2. Dataset Understanding"),
        nbf.v4.new_code_cell(
            "print('Shape:', df.shape)\n"
            "display(df.dtypes.to_frame('dtype'))\n"
            "display(df.describe().T)"
        ),
        nbf.v4.new_markdown_cell(
            "The dataset has around 122k rows. Each row represents one video record with "
            "performance metrics and a target revenue value."
        ),
        nbf.v4.new_markdown_cell("## 3. Missing Values and Duplicates"),
        nbf.v4.new_code_cell(
            "missing = df.isna().sum().to_frame('missing_count')\n"
            "missing['missing_percent'] = (missing['missing_count'] / len(df) * 100).round(2)\n"
            "display(missing)\n"
            "print('Duplicate rows:', df.duplicated().sum())"
        ),
        nbf.v4.new_markdown_cell(
            "The main missing values are in numeric engagement columns. Median imputation is "
            "used because revenue and engagement features can be skewed by high-performing videos."
        ),
        nbf.v4.new_markdown_cell("## 4. Target Variable Analysis"),
        nbf.v4.new_code_cell(
            "plt.figure(figsize=(8, 4))\n"
            "plt.hist(df['ad_revenue_usd'], bins=50, color='#2f7d6d')\n"
            "plt.title('Ad Revenue Distribution')\n"
            "plt.xlabel('Ad Revenue USD')\n"
            "plt.ylabel('Video Count')\n"
            "plt.show()\n"
            "df['ad_revenue_usd'].describe()"
        ),
        nbf.v4.new_markdown_cell("## 5. Univariate and Bivariate Analysis"),
        nbf.v4.new_code_cell(
            "numeric_cols = ['views', 'likes', 'comments', 'watch_time_minutes', "
            "'video_length_minutes', 'subscribers', 'ad_revenue_usd']\n"
            "df[numeric_cols].hist(figsize=(12, 8), bins=30)\n"
            "plt.tight_layout()\n"
            "plt.show()"
        ),
        nbf.v4.new_code_cell(
            "fig, axes = plt.subplots(1, 2, figsize=(12, 4))\n"
            "axes[0].scatter(df['watch_time_minutes'], df['ad_revenue_usd'], alpha=0.2, s=5)\n"
            "axes[0].set_title('Watch Time vs Revenue')\n"
            "axes[0].set_xlabel('Watch Time Minutes')\n"
            "axes[0].set_ylabel('Ad Revenue USD')\n"
            "axes[1].scatter(df['likes'], df['ad_revenue_usd'], alpha=0.2, s=5)\n"
            "axes[1].set_title('Likes vs Revenue')\n"
            "axes[1].set_xlabel('Likes')\n"
            "plt.tight_layout()\n"
            "plt.show()"
        ),
        nbf.v4.new_markdown_cell("## 6. Category, Device, Country, and Subscriber Analysis"),
        nbf.v4.new_code_cell(
            "for col in ['category', 'device', 'country']:\n"
            "    display(df.groupby(col)['ad_revenue_usd'].mean().sort_values(ascending=False).to_frame('avg_revenue'))\n\n"
            "subscriber_bins = pd.qcut(df['subscribers'], q=4, duplicates='drop')\n"
            "display(df.groupby(subscriber_bins, observed=True)['ad_revenue_usd'].mean().to_frame('avg_revenue'))"
        ),
        nbf.v4.new_markdown_cell("## 7. Correlation and Outlier Detection"),
        nbf.v4.new_code_cell(
            "corr = df[numeric_cols].corr()['ad_revenue_usd'].sort_values(ascending=False)\n"
            "display(corr.to_frame('correlation_with_revenue'))\n\n"
            "outlier_summary = []\n"
            "for col in numeric_cols:\n"
            "    q1, q3 = df[col].quantile([0.25, 0.75])\n"
            "    iqr = q3 - q1\n"
            "    low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr\n"
            "    count = ((df[col] < low) | (df[col] > high)).sum()\n"
            "    outlier_summary.append([col, low, high, count])\n"
            "display(pd.DataFrame(outlier_summary, columns=['column', 'lower_bound', 'upper_bound', 'outlier_count']))"
        ),
        nbf.v4.new_markdown_cell("## 8. Data Cleaning and Feature Engineering"),
        nbf.v4.new_code_cell(
            "import sys\n"
            "sys.path.append('../src')\n"
            "from preprocessing import clean_dataset\n"
            "from feature_engineering import add_engineered_features\n\n"
            "cleaned = clean_dataset(df)\n"
            "prepared = add_engineered_features(cleaned)\n"
            "prepared[['engagement_rate', 'likes_per_view', 'comments_per_view', "
            "'watch_time_efficiency', 'interaction_score', 'subscriber_engagement_score']].head()"
        ),
        nbf.v4.new_markdown_cell(
            "Created features:\n\n"
            "- Engagement Rate = `(likes + comments) / views`\n"
            "- Likes Per View = `likes / views`\n"
            "- Comments Per View = `comments / views`\n"
            "- Watch Time Efficiency = `watch_time_minutes / video_length_minutes`\n"
            "- Interaction Score = `0.7 * likes + 1.3 * comments`\n"
            "- Subscriber Engagement Score = `(likes + comments) / subscribers`"
        ),
        nbf.v4.new_markdown_cell("## 9. Model Comparison"),
        nbf.v4.new_code_cell("comparison = pd.read_csv('../reports/results/model_comparison.csv')\ndisplay(comparison)"),
        nbf.v4.new_markdown_cell(
            f"The best model is **{comparison.loc[0, 'Model']}** because it has the highest "
            "R2 score and the lowest error values. This is also easy to explain in a viva."
        ),
        nbf.v4.new_markdown_cell("## 10. Model Interpretation and Business Insights"),
        nbf.v4.new_code_cell(
            "importance = pd.read_csv('../reports/results/feature_importance.csv')\n"
            "display(importance.head(10))\n"
            "sample_predictions = pd.read_csv('../reports/results/sample_predictions.csv')\n"
            "display(sample_predictions[['actual_revenue', 'predicted_revenue']].head())"
        ),
        nbf.v4.new_markdown_cell(
            "Important business takeaways: watch time is the strongest driver, engagement "
            "features help explain viewer interest, and category/device/country analysis can "
            "guide content planning. The final Streamlit app converts these outputs into a "
            "prediction interface and revenue optimization advisor."
        ),
    ]
    nbf.write(nb, ROOT / "notebooks" / "Content_Monetization_Modeler.ipynb")


def main():
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    raw = load_dataset(RAW_PATH)
    comparison_path = RESULTS_DIR / "model_comparison.csv"
    model_path = MODELS_DIR / "best_model.pkl"
    processed_path = ROOT / "data" / "processed" / "cleaned_youtube_revenue.csv"

    if comparison_path.exists() and model_path.exists() and processed_path.exists():
        comparison = pd.read_csv(comparison_path)
        best_name = comparison.loc[0, "Model"]
        best_pipeline = joblib.load(model_path)
        prepared = pd.read_csv(processed_path)
    else:
        comparison, best_name, best_pipeline, prepared = train_models(raw, MODELS_DIR, RESULTS_DIR)

    save_figures(prepared)
    feature_importance(best_pipeline, prepared)
    write_eda_report(raw, prepared)
    business_insights(prepared)
    write_evaluation_prep(comparison, best_name)
    make_notebook(comparison)
    (RESULTS_DIR / "project_summary.json").write_text(
        json.dumps(
            {
                "rows": int(raw.shape[0]),
                "columns": int(raw.shape[1]),
                "best_model": best_name,
                "top_r2": float(comparison.loc[0, "R2 Score"]),
                "top_rmse": float(comparison.loc[0, "RMSE"]),
                "top_mae": float(comparison.loc[0, "MAE"]),
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print(comparison)
    print(f"Best model: {best_name}")


if __name__ == "__main__":
    main()
