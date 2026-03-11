"""Data loader module for Toronto Traffic Collision dataset."""

import pandas as pd


EXPECTED_COLUMNS = [
    "OBJECTID", "EVENT_UNIQUE_ID", "OCC_DATE", "OCC_MONTH", "OCC_DOW",
    "OCC_YEAR", "OCC_HOUR", "DIVISION", "FATALITIES", "INJURY_COLLISIONS",
    "FTR_COLLISIONS", "PD_COLLISIONS", "HOOD_158", "NEIGHBOURHOOD_158",
    "LONG_WGS84", "LAT_WGS84", "AUTOMOBILE", "MOTORCYCLE", "PASSENGER",
    "BICYCLE", "PEDESTRIAN", "x", "y"
]


def load_dataset(filepath: str) -> pd.DataFrame:
    """Load the Toronto Traffic Collision dataset from a CSV file."""
    if not isinstance(filepath, str):
        raise TypeError("filepath must be a string")
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        raise FileNotFoundError(f"Dataset not found: {filepath}")
    return df


def validate_columns(df: pd.DataFrame) -> bool:
    """Validate that the DataFrame contains all expected columns."""
    return all(col in df.columns for col in EXPECTED_COLUMNS)
