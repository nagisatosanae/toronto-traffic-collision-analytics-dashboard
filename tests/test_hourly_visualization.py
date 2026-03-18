"""Tests for hourly collision visualization (Story #7)."""

import pytest
import pandas as pd
import matplotlib.pyplot as plt
from src.visualizations import create_hourly_chart


class TestHourlyChart:
    """Tests for create_hourly_chart function."""

    def test_returns_figure(self):
        """Result should be a matplotlib Figure."""
        df = pd.DataFrame({"OCC_HOUR": [1, 2, 3], "collision_count": [10, 20, 30]})
        result = create_hourly_chart(df)
        assert isinstance(result, plt.Figure)

    def test_chart_has_data(self):
        """Chart should contain at least one axes with bars."""
        df = pd.DataFrame({"OCC_HOUR": [1, 2, 3], "collision_count": [10, 20, 30]})
        fig = create_hourly_chart(df)
        ax = fig.axes[0]
        assert len(ax.patches) > 0

    def test_chart_title_exists(self):
        """Chart should have a title."""
        df = pd.DataFrame({"OCC_HOUR": [1, 2], "collision_count": [10, 20]})
        fig = create_hourly_chart(df)
        ax = fig.axes[0]
        assert ax.get_title() != ""

    def teardown_method(self):
        plt.close("all")
