"""Tests for hotspot collision visualization (Story #8)."""

import pytest
import pandas as pd
import matplotlib.pyplot as plt
from src.hotspot_visualization import create_hotspot_chart


class TestHotspotChart:
    """Tests for create_hotspot_chart function."""

    def test_returns_figure(self):
        """Result should be a matplotlib Figure."""
        df = pd.DataFrame({
            "NEIGHBOURHOOD_158": ["A", "B", "C"],
            "collision_count": [100, 80, 60]
        })
        result = create_hotspot_chart(df)
        assert isinstance(result, plt.Figure)

    def test_chart_has_bars(self):
        """Chart should contain horizontal bars."""
        df = pd.DataFrame({
            "NEIGHBOURHOOD_158": ["A", "B"],
            "collision_count": [100, 80]
        })
        fig = create_hotspot_chart(df)
        ax = fig.axes[0]
        assert len(ax.patches) > 0

    def test_top_n_limits_bars(self):
        """Chart should only show top_n neighbourhoods."""
        df = pd.DataFrame({
            "NEIGHBOURHOOD_158": ["A", "B", "C", "D", "E"],
            "collision_count": [50, 40, 30, 20, 10]
        })
        fig = create_hotspot_chart(df, top_n=3)
        ax = fig.axes[0]
        assert len(ax.patches) == 3

    def test_chart_title_exists(self):
        """Chart should have a title."""
        df = pd.DataFrame({
            "NEIGHBOURHOOD_158": ["A"],
            "collision_count": [100]
        })
        fig = create_hotspot_chart(df)
        ax = fig.axes[0]
        assert ax.get_title() != ""

    def teardown_method(self):
        plt.close("all")
