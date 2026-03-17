import pandas as pd

HOUR_COLUMN = "OCC_HOUR"
COUNT_COLUMN = "collision_count"


def analyze_collisions_by_hour(collision_data: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate collision counts by hour of the day.

    Args:
        collision_data: DataFrame containing collision records with OCC_HOUR column.

    Returns:
        DataFrame with columns [OCC_HOUR, collision_count], sorted by hour.
    """
    if HOUR_COLUMN not in collision_data.columns:
        raise KeyError(f"{HOUR_COLUMN} column is required")

    return (
        collision_data.groupby(HOUR_COLUMN)
        .size()
        .reset_index(name=COUNT_COLUMN)
        .sort_values(HOUR_COLUMN)
        .reset_index(drop=True)
    )