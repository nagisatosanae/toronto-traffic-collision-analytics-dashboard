"""Tests for neighbourhood analytics module (Story #4)."""

import pytest
import pandas as pd
from src.analytics import analyze_collisions_by_neighbourhood


class TestAnalyzeByNeighbourhood:
    """Tests for analyze_collisions_by_neighbourhood function."""

    def test_returns_dataframe(self):
        """Result should be a DataFrame."""
        df = pd.DataFrame({"NEIGHBOURHOOD_158": ["Downtown", "Midtown"]})
        result = analyze_collisions_by_neighbourhood(df)
        assert isinstance(result, pd.DataFrame)

    def test_aggregates_by_neighbourhood(self):
        """Collisions should be counted per neighbourhood."""
        df = pd.DataFrame({"NEIGHBOURHOOD_158": ["Downtown", "Downtown", "Midtown"]})
        result = analyze_collisions_by_neighbourhood(df)
        row = result[result["NEIGHBOURHOOD_158"] == "Downtown"]
        assert row["collision_count"].values[0] == 2

    def test_sorted_by_count_descending(self):
        """Result should be sorted by collision count descending."""
        df = pd.DataFrame({"NEIGHBOURHOOD_158": ["A", "B", "B", "C", "C", "C"]})
        result = analyze_collisions_by_neighbourhood(df)
        assert list(result["NEIGHBOURHOOD_158"]) == ["C", "B", "A"]

    def test_excludes_nsa(self):
        """NSA values should be excluded from results."""
        df = pd.DataFrame({"NEIGHBOURHOOD_158": ["Downtown", "NSA", "NSA"]})
        result = analyze_collisions_by_neighbourhood(df)
        assert "NSA" not in result["NEIGHBOURHOOD_158"].values
