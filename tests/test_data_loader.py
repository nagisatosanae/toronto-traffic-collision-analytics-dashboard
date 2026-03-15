"""Tests for data loader module (Story #1, #11)."""

import pytest
import pandas as pd
from src.data_loader import load_dataset, validate_columns, EXPECTED_COLUMNS


class TestLoadDataset:
    """Tests for load_dataset function."""

    def test_load_returns_dataframe(self, tmp_path):
        """Loading a valid CSV should return a DataFrame."""
        csv_file = tmp_path / "test.csv"
        csv_file.write_text("OBJECTID,EVENT_UNIQUE_ID\n1,GO-001\n")
        result = load_dataset(str(csv_file))
        assert isinstance(result, pd.DataFrame)

    def test_load_not_empty(self, tmp_path):
        """Loaded DataFrame should not be empty."""
        csv_file = tmp_path / "test.csv"
        csv_file.write_text("OBJECTID,EVENT_UNIQUE_ID\n1,GO-001\n")
        result = load_dataset(str(csv_file))
        assert len(result) > 0

    def test_load_missing_file_raises_error(self):
        """Loading a non-existent file should raise FileNotFoundError."""
        with pytest.raises(FileNotFoundError):
            load_dataset("nonexistent.csv")


class TestValidateColumns:
    """Tests for validate_columns function."""

    def test_valid_columns_returns_true(self):
        """DataFrame with all expected columns should return True."""
        df = pd.DataFrame(columns=EXPECTED_COLUMNS)
        assert validate_columns(df) is True

    def test_missing_columns_returns_false(self):
        """DataFrame missing columns should return False."""
        df = pd.DataFrame(columns=["OBJECTID", "OCC_DATE"])
        assert validate_columns(df) is False
