"""Data loading and preprocessing utilities."""

from pathlib import Path

import pandas as pd


TARGET_COLUMN = "ad_revenue_usd"
ID_COLUMNS = ["video_id", "date"]
CATEGORICAL_COLUMNS = ["category", "device", "country"]
NUMERIC_COLUMNS = [
    "views",
    "likes",
    "comments",
    "watch_time_minutes",
    "video_length_minutes",
    "subscribers",
    "engagement_rate",
    "likes_per_view",
    "comments_per_view",
    "watch_time_efficiency",
    "interaction_score",
    "subscriber_engagement_score",
]
FEATURE_COLUMNS = NUMERIC_COLUMNS + CATEGORICAL_COLUMNS


def load_dataset(path: str | Path) -> pd.DataFrame:
    """Load the raw YouTube ad revenue dataset."""
    return pd.read_csv(path)


def clean_dataset(df: pd.DataFrame, treat_outliers: bool = True) -> pd.DataFrame:
    """Clean nulls, duplicates, datatypes, category text, and outliers."""
    data = df.copy()
    data = data.drop_duplicates()

    if "date" in data.columns:
        data["date"] = pd.to_datetime(data["date"], errors="coerce")

    for col in CATEGORICAL_COLUMNS:
        data[col] = data[col].astype(str).str.strip().str.title()
        data[col] = data[col].replace({"Nan": "Unknown", "": "Unknown"})
        data[col] = data[col].fillna("Unknown")

    numeric_base = [
        "views",
        "likes",
        "comments",
        "watch_time_minutes",
        "video_length_minutes",
        "subscribers",
        TARGET_COLUMN,
    ]
    for col in numeric_base:
        data[col] = pd.to_numeric(data[col], errors="coerce")
        data[col] = data[col].fillna(data[col].median())

    data = data[data[TARGET_COLUMN] >= 0].copy()

    if treat_outliers:
        for col in numeric_base:
            low, high = iqr_bounds(data[col])
            data[col] = data[col].clip(lower=low, upper=high)

    return data


def iqr_bounds(series: pd.Series) -> tuple[float, float]:
    """Return common IQR lower and upper bounds."""
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    return q1 - (1.5 * iqr), q3 + (1.5 * iqr)


def split_features_target(df: pd.DataFrame):
    """Return X and y using only model-ready feature columns."""
    return df[FEATURE_COLUMNS].copy(), df[TARGET_COLUMN].copy()
