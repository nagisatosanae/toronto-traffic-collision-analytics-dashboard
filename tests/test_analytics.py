"""Tests for analytics module (Story #3)."""

import pytest
import pandas as pd
from src.analytics import analyze_collisions_by_hour


class TestAnalyzeByHour:
    """Tests for analyze_collisions_by_hour function."""

    def test_returns_dataframe(self):
        """Result should be a DataFrame."""
        df = pd.DataFrame({"OCC_HOUR": [1, 2, 3, 1, 2]})
        result = analyze_collisions_by_hour(df)
        assert isinstance(result, pd.DataFrame)

    def test_aggregates_by_hour(self):
        """Collisions should be counted per hour."""
        df = pd.DataFrame({"OCC_HOUR": [1, 1, 1, 2, 2, 3]})
        result = analyze_collisions_by_hour(df)
        row_hour_1 = result[result["OCC_HOUR"] == 1]
        assert row_hour_1["collision_count"].values[0] == 3

    def test_covers_all_hours(self):
        """Result should contain every hour present in the input."""
        df = pd.DataFrame({"OCC_HOUR": [0, 12, 23]})
        result = analyze_collisions_by_hour(df)
        assert len(result) == 3

    def test_sorted_by_hour(self):
        """Result should be sorted by OCC_HOUR ascending."""
        df = pd.DataFrame({"OCC_HOUR": [23, 0, 12, 5]})
        result = analyze_collisions_by_hour(df)
        assert list(result["OCC_HOUR"]) == [0, 5, 12, 23]
