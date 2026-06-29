"""Unit tests for statistics_analysis.py"""

import numpy as np
import pandas as pd
import pytest

import statistics_analysis as stats


class TestRegressionMetrics:
    def test_perfect_predictions_give_r2_of_one_and_zero_error(self):
        y_true = [10, 20, 30, 40]
        y_pred = [10, 20, 30, 40]
        result = stats.regression_metrics(y_true, y_pred)
        assert result["R2 Score"] == pytest.approx(1.0)
        assert result["RMSE"] == pytest.approx(0.0)
        assert result["MAE"] == pytest.approx(0.0)

    def test_returns_expected_keys(self):
        result = stats.regression_metrics([1, 2, 3], [1, 2, 3])
        assert set(result.keys()) == {"R2 Score", "RMSE", "MAE"}

    def test_all_values_are_python_floats(self):
        result = stats.regression_metrics([1, 2, 3], [1.1, 2.2, 2.9])
        for value in result.values():
            assert isinstance(value, float)

    def test_known_mae_and_rmse_for_simple_case(self):
        # Errors are exactly [1, -1, 1] -> abs errors [1, 1, 1] -> MAE = 1
        # squared errors [1, 1, 1] -> mean = 1 -> RMSE = 1
        y_true = [10, 20, 30]
        y_pred = [11, 19, 31]
        result = stats.regression_metrics(y_true, y_pred)
        assert result["MAE"] == pytest.approx(1.0)
        assert result["RMSE"] == pytest.approx(1.0)

    def test_worse_predictions_increase_error_metrics(self):
        y_true = [10, 20, 30, 40]
        good_pred = [11, 19, 31, 39]
        bad_pred = [50, 5, 60, 1]
        good_result = stats.regression_metrics(y_true, good_pred)
        bad_result = stats.regression_metrics(y_true, bad_pred)
        assert bad_result["RMSE"] > good_result["RMSE"]
        assert bad_result["MAE"] > good_result["MAE"]
        assert bad_result["R2 Score"] < good_result["R2 Score"]


class TestRankModels:
    def test_sorts_by_r2_score_descending(self):
        results = [
            {"Model": "A", "R2 Score": 0.80, "RMSE": 5.0, "MAE": 2.0},
            {"Model": "B", "R2 Score": 0.95, "RMSE": 3.0, "MAE": 1.0},
            {"Model": "C", "R2 Score": 0.60, "RMSE": 8.0, "MAE": 4.0},
        ]
        ranked = stats.rank_models(results)
        assert ranked.iloc[0]["Model"] == "B"
        assert ranked.iloc[-1]["Model"] == "C"

    def test_ties_in_r2_break_on_lower_rmse(self):
        # Mirrors the real project: Lasso, Ridge, and Linear all tie at
        # R2 = 0.9526, and the winner should be the one with lowest RMSE.
        results = [
            {"Model": "Ridge", "R2 Score": 0.9526, "RMSE": 13.4798, "MAE": 3.1155},
            {"Model": "Lasso", "R2 Score": 0.9526, "RMSE": 13.4781, "MAE": 3.0830},
            {"Model": "Linear", "R2 Score": 0.9526, "RMSE": 13.4799, "MAE": 3.1170},
        ]
        ranked = stats.rank_models(results)
        assert ranked.iloc[0]["Model"] == "Lasso"

    def test_returned_index_is_reset(self):
        results = [
            {"Model": "A", "R2 Score": 0.5, "RMSE": 10.0, "MAE": 5.0},
            {"Model": "B", "R2 Score": 0.9, "RMSE": 2.0, "MAE": 1.0},
        ]
        ranked = stats.rank_models(results)
        assert list(ranked.index) == [0, 1]

    def test_returns_dataframe_with_same_row_count(self):
        results = [
            {"Model": "A", "R2 Score": 0.5, "RMSE": 10.0, "MAE": 5.0},
            {"Model": "B", "R2 Score": 0.9, "RMSE": 2.0, "MAE": 1.0},
            {"Model": "C", "R2 Score": 0.7, "RMSE": 6.0, "MAE": 3.0},
        ]
        ranked = stats.rank_models(results)
        assert len(ranked) == len(results)
