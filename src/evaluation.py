"""Model evaluation helpers."""

import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def regression_metrics(y_true, y_pred) -> dict[str, float]:
    """Calculate R2, RMSE, and MAE for a regression model."""
    return {
        "R2 Score": float(r2_score(y_true, y_pred)),
        "RMSE": float(np.sqrt(mean_squared_error(y_true, y_pred))),
        "MAE": float(mean_absolute_error(y_true, y_pred)),
    }


def rank_models(results: list[dict]) -> pd.DataFrame:
    """Create a sorted model comparison table."""
    table = pd.DataFrame(results)
    return table.sort_values(["R2 Score", "RMSE"], ascending=[False, True]).reset_index(drop=True)
