"""Tests for collision severity analytics (Story #5)."""

import pandas as pd
from src.analytics.severity import analyze_collision_severity


class TestSeverityAnalytics:

    def setup_method(self):
        self.df = pd.DataFrame({
            "FATALITIES": [0, 1, 0, 0],
            "INJURY_COLLISIONS": ["YES", "NO", "YES", "NO"],
            "FTR_COLLISIONS": ["NO", "NO", "YES", "NO"],
            "PD_COLLISIONS": ["NO", "NO", "NO", "YES"],
        })

    def test_returns_dataframe(self):
        result = analyze_collision_severity(self.df)
        assert isinstance(result, pd.DataFrame)

    def test_has_four_categories(self):
        result = analyze_collision_severity(self.df)
        assert len(result) == 4

    def test_fatal_count(self):
        result = analyze_collision_severity(self.df)
        fatal = result[result["severity"] == "Fatal"]
        assert fatal["collision_count"].values[0] == 1

    def test_injury_count(self):
        result = analyze_collision_severity(self.df)
        injury = result[result["severity"] == "Injury"]
        assert injury["collision_count"].values[0] == 2
