"""Tests for pedestrian and cyclist analytics (Story #6)."""

import pandas as pd
from src.analytics import analyze_vulnerable_users


class TestVulnerableUserAnalytics:

    def setup_method(self):
        self.df = pd.DataFrame({
            "PEDESTRIAN": ["YES", "NO", "YES", "NO"],
            "BICYCLE": ["NO", "YES", "NO", "NO"],
        })

    def test_returns_dataframe(self):
        result = analyze_vulnerable_users(self.df)
        assert isinstance(result, pd.DataFrame)

    def test_pedestrian_count(self):
        result = analyze_vulnerable_users(self.df)
        ped = result[result["user_type"] == "Pedestrian"]
        assert ped["collision_count"].values[0] == 2

    def test_cyclist_count(self):
        result = analyze_vulnerable_users(self.df)
        cyc = result[result["user_type"] == "Cyclist"]
        assert cyc["collision_count"].values[0] == 1

    def test_has_two_categories(self):
        result = analyze_vulnerable_users(self.df)
        assert len(result) == 2
