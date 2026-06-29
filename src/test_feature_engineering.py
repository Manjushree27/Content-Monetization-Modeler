"""Unit tests for feature_engineering.py"""

import numpy as np
import pandas as pd
import pytest

import feature_engineering as fe


class TestSafeDivide:
    def test_normal_division(self):
        result = fe.safe_divide(10, 2)
        assert result == 5

    def test_division_by_zero_returns_zero_not_inf_or_nan(self):
        result = fe.safe_divide(10, 0)
        assert result == 0
        assert not np.isnan(result)
        assert not np.isinf(result)

    def test_zero_divided_by_zero_returns_zero(self):
        result = fe.safe_divide(0, 0)
        assert result == 0

    def test_array_division_with_mixed_zero_denominators(self):
        numerator = np.array([10, 20, 30])
        denominator = np.array([2, 0, 5])
        result = fe.safe_divide(numerator, denominator)
        np.testing.assert_array_almost_equal(result, [5, 0, 6])


class TestAddEngineeredFeatures:
    @pytest.fixture
    def sample_df(self):
        return pd.DataFrame(
            {
                "views": [1000, 0, 500],
                "likes": [100, 10, 0],
                "comments": [20, 5, 0],
                "watch_time_minutes": [300, 0, 150],
                "video_length_minutes": [10, 5, 0],
                "subscribers": [1000, 0, 200],
            }
        )

    def test_adds_all_six_expected_columns(self, sample_df):
        result = fe.add_engineered_features(sample_df)
        for col in fe.ENGINEERED_FEATURES:
            assert col in result.columns

    def test_does_not_mutate_input_dataframe(self, sample_df):
        original = sample_df.copy()
        fe.add_engineered_features(sample_df)
        pd.testing.assert_frame_equal(sample_df, original)

    def test_engagement_rate_matches_formula_for_normal_row(self, sample_df):
        result = fe.add_engineered_features(sample_df)
        # Row 0: (100 + 20) / 1000 = 0.12
        assert result.loc[0, "engagement_rate"] == pytest.approx(0.12)

    def test_engagement_rate_is_zero_when_views_is_zero(self, sample_df):
        result = fe.add_engineered_features(sample_df)
        # Row 1 has views == 0, so the safe_divide guard should produce 0.
        assert result.loc[1, "engagement_rate"] == 0

    def test_likes_per_view_matches_formula(self, sample_df):
        result = fe.add_engineered_features(sample_df)
        assert result.loc[0, "likes_per_view"] == pytest.approx(100 / 1000)

    def test_comments_per_view_matches_formula(self, sample_df):
        result = fe.add_engineered_features(sample_df)
        assert result.loc[0, "comments_per_view"] == pytest.approx(20 / 1000)

    def test_watch_time_efficiency_handles_zero_length_video(self, sample_df):
        result = fe.add_engineered_features(sample_df)
        # Row 2 has video_length_minutes == 0, should not raise or return inf.
        assert result.loc[2, "watch_time_efficiency"] == 0

    def test_watch_time_efficiency_matches_formula_for_normal_row(self, sample_df):
        result = fe.add_engineered_features(sample_df)
        assert result.loc[0, "watch_time_efficiency"] == pytest.approx(300 / 10)

    def test_interaction_score_matches_weighted_formula(self, sample_df):
        result = fe.add_engineered_features(sample_df)
        # Row 0: 0.7 * 100 + 1.3 * 20 = 70 + 26 = 96
        assert result.loc[0, "interaction_score"] == pytest.approx(96)

    def test_interaction_score_is_zero_when_likes_and_comments_are_zero(self, sample_df):
        result = fe.add_engineered_features(sample_df)
        assert result.loc[2, "interaction_score"] == 0

    def test_subscriber_engagement_score_handles_zero_subscribers(self, sample_df):
        result = fe.add_engineered_features(sample_df)
        # Row 1 has subscribers == 0, should resolve to 0, not inf/nan.
        assert result.loc[1, "subscriber_engagement_score"] == 0

    def test_subscriber_engagement_score_matches_formula_for_normal_row(self, sample_df):
        result = fe.add_engineered_features(sample_df)
        assert result.loc[0, "subscriber_engagement_score"] == pytest.approx(
            (100 + 20) / 1000
        )

    def test_no_nan_or_inf_in_any_engineered_column(self, sample_df):
        result = fe.add_engineered_features(sample_df)
        for col in fe.ENGINEERED_FEATURES:
            assert not result[col].isna().any()
            assert np.isfinite(result[col]).all()
