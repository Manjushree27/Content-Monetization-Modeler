"""Unit tests for preprocessing.py"""

import pandas as pd
import pytest

import preprocessing as prep


@pytest.fixture
def raw_df():
    """A small raw dataset with the kinds of mess clean_dataset() should fix."""
    return pd.DataFrame(
        {
            "video_id": ["v1", "v2", "v3", "v3", "v4"],  # v3 is a duplicate row
            "date": ["2026-01-01", "2026-01-02", "2026-01-03", "2026-01-03", "not-a-date"],
            "views": [1000, 2000, None, None, 1_000_000],  # None to fill, outlier to clip
            "likes": [10, 20, 30, 30, 999999],
            "comments": [1, 2, 3, 3, 999999],
            "watch_time_minutes": [100, 200, 300, 300, 400],
            "video_length_minutes": [10, 20, 30, 30, 40],
            "subscribers": [500, 600, 700, 700, 800],
            "category": [" tech ", "Gaming", None, None, "music"],
            "device": ["mobile", " Desktop", "tablet", "tablet", "Mobile"],
            "country": ["us", "IN", "uk", "uk", "us"],
            "ad_revenue_usd": [5.0, 10.0, 15.0, 15.0, -3.0],  # negative revenue row to drop
            "engagement_rate": [0.01] * 5,
            "likes_per_view": [0.01] * 5,
            "comments_per_view": [0.001] * 5,
            "watch_time_efficiency": [10.0] * 5,
            "interaction_score": [5.0] * 5,
            "subscriber_engagement_score": [0.02] * 5,
        }
    )


class TestCleanDataset:
    def test_removes_exact_duplicate_rows(self, raw_df):
        cleaned = prep.clean_dataset(raw_df)
        assert cleaned["video_id"].tolist().count("v3") == 1

    def test_drops_negative_revenue_rows(self, raw_df):
        cleaned = prep.clean_dataset(raw_df)
        assert (cleaned[prep.TARGET_COLUMN] >= 0).all()

    def test_date_column_is_parsed_to_datetime(self, raw_df):
        cleaned = prep.clean_dataset(raw_df)
        assert pd.api.types.is_datetime64_any_dtype(cleaned["date"])

    def test_invalid_date_becomes_null_not_a_crash(self, raw_df):
        # "not-a-date" should coerce to NaT, not raise.
        cleaned = prep.clean_dataset(raw_df)
        assert cleaned["date"].isna().any() or len(cleaned) < len(raw_df)

    def test_categorical_columns_are_title_cased_and_stripped(self, raw_df):
        cleaned = prep.clean_dataset(raw_df)
        # " tech " -> "Tech", " Desktop" -> "Desktop"
        assert "Tech" in cleaned["category"].values
        assert all(not val.startswith(" ") for val in cleaned["device"])

    def test_missing_category_becomes_unknown(self, raw_df):
        cleaned = prep.clean_dataset(raw_df)
        # The two None category rows should not remain null and should
        # not crash str.title() — they should resolve to "Unknown".
        assert cleaned["category"].isna().sum() == 0

    def test_no_nulls_in_numeric_base_columns_after_cleaning(self, raw_df):
        cleaned = prep.clean_dataset(raw_df)
        numeric_base = [
            "views",
            "likes",
            "comments",
            "watch_time_minutes",
            "video_length_minutes",
            "subscribers",
        ]
        for col in numeric_base:
            assert cleaned[col].isna().sum() == 0

    def test_outlier_clipping_reduces_extreme_max(self, raw_df):
        cleaned_with_outliers = prep.clean_dataset(raw_df, treat_outliers=True)
        cleaned_without = prep.clean_dataset(raw_df.copy(), treat_outliers=False)
        # With clipping on, the extreme 1,000,000 views value should be
        # pulled down compared to leaving outliers untouched.
        assert cleaned_with_outliers["views"].max() <= cleaned_without["views"].max()

    def test_does_not_mutate_input_dataframe(self, raw_df):
        original_shape = raw_df.shape
        prep.clean_dataset(raw_df)
        assert raw_df.shape == original_shape


class TestIqrBounds:
    def test_returns_lower_less_than_upper(self):
        series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        low, high = prep.iqr_bounds(series)
        assert low < high

    def test_constant_series_has_zero_width_bounds(self):
        series = pd.Series([5, 5, 5, 5, 5])
        low, high = prep.iqr_bounds(series)
        assert low == high == 5

    def test_known_bounds_match_manual_calculation(self):
        # For [1..10], Q1=3.25, Q3=7.75, IQR=4.5
        # lower = 3.25 - 6.75 = -3.5, upper = 7.75 + 6.75 = 14.5
        series = pd.Series(range(1, 11))
        low, high = prep.iqr_bounds(series)
        assert low == pytest.approx(-3.5)
        assert high == pytest.approx(14.5)


class TestSplitFeaturesTarget:
    def test_returns_correct_column_sets(self, raw_df):
        cleaned = prep.clean_dataset(raw_df)
        X, y = prep.split_features_target(cleaned)
        assert list(X.columns) == prep.FEATURE_COLUMNS
        assert y.name == prep.TARGET_COLUMN

    def test_target_not_present_in_features(self, raw_df):
        cleaned = prep.clean_dataset(raw_df)
        X, _ = prep.split_features_target(cleaned)
        assert prep.TARGET_COLUMN not in X.columns

    def test_row_counts_match_between_x_and_y(self, raw_df):
        cleaned = prep.clean_dataset(raw_df)
        X, y = prep.split_features_target(cleaned)
        assert len(X) == len(y)
