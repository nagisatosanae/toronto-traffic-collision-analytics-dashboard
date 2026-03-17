import pandas as pd
import pytest

from src.analytics import analyze_collisions_by_hour


class TestAnalyzeByHour:

    def test_returns_dataframe(self):
        df = pd.DataFrame({"OCC_HOUR": [1, 2, 3, 1, 2]})
        result = analyze_collisions_by_hour(df)
        assert isinstance(result, pd.DataFrame)

    def test_aggregates_by_hour(self):
        df = pd.DataFrame({"OCC_HOUR": [1, 1, 1, 2, 2, 3]})
        result = analyze_collisions_by_hour(df)

        row_hour_1 = result[result["OCC_HOUR"] == 1]
        assert row_hour_1["collision_count"].values[0] == 3

    def test_covers_all_hours(self):
        df = pd.DataFrame({"OCC_HOUR": [0, 12, 23]})
        result = analyze_collisions_by_hour(df)
        assert len(result) == 3

    def test_sorted_by_hour(self):
        df = pd.DataFrame({"OCC_HOUR": [23, 0, 12, 5]})
        result = analyze_collisions_by_hour(df)
        assert result["OCC_HOUR"].tolist() == [0, 5, 12, 23]

    def test_missing_column_raises_error(self):
        df = pd.DataFrame({"HOUR": [1, 2, 3]})

        with pytest.raises(KeyError):
            analyze_collisions_by_hour(df)