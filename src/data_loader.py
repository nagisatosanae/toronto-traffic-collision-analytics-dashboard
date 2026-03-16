"""Data loader module for Toronto Traffic Collision dataset.

Provides functions to load and validate the Toronto Traffic
Collisions Open Data CSV file.
"""

import os
import pandas as pd

EXPECTED_COLUMNS = [
    "OBJECTID", "EVENT_UNIQUE_ID", "OCC_DATE", "OCC_MONTH", "OCC_DOW",
    "OCC_YEAR", "OCC_HOUR", "DIVISION", "FATALITIES", "INJURY_COLLISIONS",
    "FTR_COLLISIONS", "PD_COLLISIONS", "HOOD_158", "NEIGHBOURHOOD_158",
    "LONG_WGS84", "LAT_WGS84", "AUTOMOBILE", "MOTORCYCLE", "PASSENGER",
    "BICYCLE", "PEDESTRIAN", "x", "y"
]

DEFAULT_DATA_PATH = os.path.join("data", "Traffic_Collisions_Open_Data.csv")


def load_dataset(filepath: str = None) -> pd.DataFrame:
    """Load the Toronto Traffic Collision dataset from a CSV file.

    Args:
        filepath: Path to the CSV file. Defaults to data/ directory.

    Returns:
        DataFrame containing the collision records.

    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    if filepath is None:
        filepath = DEFAULT_DATA_PATH

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dataset not found: {filepath}")

    return pd.read_csv(filepath)


def validate_columns(df: pd.DataFrame) -> bool:
    """Validate that the DataFrame contains all expected columns.

    Args:
        df: DataFrame to validate.

    Returns:
        True if all expected columns are present, False otherwise.
    """
    return all(col in df.columns for col in EXPECTED_COLUMNS)
