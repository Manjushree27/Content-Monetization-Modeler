"""Prediction and advisor utilities used by the Streamlit app."""

import joblib
import pandas as pd

from feature_engineering import add_engineered_features
from preprocessing import FEATURE_COLUMNS, clean_dataset


def load_model(model_path):
    """Load the saved best model pipeline."""
    return joblib.load(model_path)


def predict_revenue(model, input_data: dict) -> float:
    """Predict ad revenue for one video input dictionary."""
    row = pd.DataFrame([input_data])
    cleaned = clean_dataset(row, treat_outliers=False)
    engineered = add_engineered_features(cleaned)
    return float(model.predict(engineered[FEATURE_COLUMNS])[0])


def performance_score(revenue: float, benchmark: float) -> int:
    """Convert predicted revenue into a simple 0-100 score."""
    if benchmark <= 0:
        return 0
    score = (revenue / benchmark) * 70
    return int(max(0, min(100, round(score))))


def advisor_messages(input_data: dict, predicted_revenue: float) -> list[str]:
    """Return beginner-friendly recommendations based on the input values."""
    views = max(input_data.get("views", 1), 1)
    likes = input_data.get("likes", 0)
    comments = input_data.get("comments", 0)
    watch_time = input_data.get("watch_time_minutes", 0)
    video_length = max(input_data.get("video_length_minutes", 1), 1)

    engagement = (likes + comments) / views
    avg_watch_per_min = watch_time / video_length
    messages = []

    if engagement < 0.10:
        messages.append(
            f"Engagement is {engagement:.2%}. Improving titles, thumbnails, and calls to action can help lift expected revenue by around 5-10%."
        )
    else:
        messages.append("Engagement is healthy. Keep using the same content style and topic format.")

    if avg_watch_per_min < 1500:
        messages.append(
            "Watch time efficiency is low. Stronger intros and clearer pacing may increase revenue potential."
        )
    else:
        messages.append("Watch time is strong, which is a good signal for ad revenue.")

    messages.append(
        f"A realistic optimization target is about ${predicted_revenue * 1.08:,.2f}, assuming small gains in engagement and watch time."
    )
    return messages
