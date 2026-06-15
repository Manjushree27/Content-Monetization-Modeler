"""Feature engineering helpers for the Content Monetization Modeler."""

import numpy as np
import pandas as pd


def safe_divide(numerator, denominator):
    """Return numerator / denominator while avoiding division by zero."""
    denominator = np.where(np.asarray(denominator) == 0, np.nan, denominator)
    return np.nan_to_num(np.asarray(numerator) / denominator, nan=0.0, posinf=0.0, neginf=0.0)


def add_engineered_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create beginner-friendly revenue features from raw video metrics."""
    data = df.copy()

    data["engagement_rate"] = safe_divide(data["likes"] + data["comments"], data["views"])
    data["likes_per_view"] = safe_divide(data["likes"], data["views"])
    data["comments_per_view"] = safe_divide(data["comments"], data["views"])
    data["watch_time_efficiency"] = safe_divide(
        data["watch_time_minutes"], data["video_length_minutes"]
    )
    data["interaction_score"] = (0.7 * data["likes"]) + (1.3 * data["comments"])
    data["subscriber_engagement_score"] = safe_divide(
        data["likes"] + data["comments"], data["subscribers"]
    )

    return data


ENGINEERED_FEATURES = [
    "engagement_rate",
    "likes_per_view",
    "comments_per_view",
    "watch_time_efficiency",
    "interaction_score",
    "subscriber_engagement_score",
]
