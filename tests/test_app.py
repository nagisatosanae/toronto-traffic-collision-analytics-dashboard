"""Tests for Streamlit dashboard (Story #9)."""

import pytest
from unittest.mock import patch
import pandas as pd
from app import main


class TestDashboard:
    """Tests for Streamlit dashboard."""

    def test_app_runs_without_error(self):
        """Dashboard main function should execute without error."""
        with patch("streamlit.title"), \
             patch("streamlit.header"), \
             patch("streamlit.pyplot"), \
             patch("streamlit.sidebar") as mock_sidebar, \
             patch("app.load_dataset") as mock_load:
            mock_sidebar.selectbox.return_value = "All"
            mock_load.return_value = pd.DataFrame({
                "OCC_HOUR": [1, 2],
                "OCC_YEAR": [2022, 2023],
                "NEIGHBOURHOOD_158": ["A", "B"],
                "FATALITIES": [0, 1],
                "INJURY_COLLISIONS": ["YES", "NO"],
                "FTR_COLLISIONS": ["NO", "YES"],
                "PD_COLLISIONS": ["NO", "NO"],
                "PEDESTRIAN": ["YES", "NO"],
                "BICYCLE": ["NO", "YES"],
            })
            main()

    def test_app_handles_missing_data(self):
        """Dashboard should handle missing dataset gracefully."""
        with patch("streamlit.title"), \
             patch("streamlit.error") as mock_error, \
             patch("app.load_dataset", side_effect=FileNotFoundError):
            main()
            mock_error.assert_called_once()

    def test_app_displays_title(self):
        """Dashboard should display the main title."""
        with patch("streamlit.title") as mock_title, \
             patch("streamlit.header"), \
             patch("streamlit.pyplot"), \
             patch("streamlit.sidebar") as mock_sidebar, \
             patch("app.load_dataset") as mock_load:
            mock_sidebar.selectbox.return_value = "All"
            mock_load.return_value = pd.DataFrame({
                "OCC_HOUR": [1],
                "OCC_YEAR": [2022],
                "NEIGHBOURHOOD_158": ["A"],
                "FATALITIES": [0],
                "INJURY_COLLISIONS": ["YES"],
                "FTR_COLLISIONS": ["NO"],
                "PD_COLLISIONS": ["NO"],
                "PEDESTRIAN": ["YES"],
                "BICYCLE": ["NO"],
            })
            main()
            mock_title.assert_called_once()
