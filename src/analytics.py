"""Analytics module for Toronto Traffic Collision dataset.

Provides functions to aggregate and summarize collision data
for analytical and visualization purposes.
"""

import pandas as pd

HOUR_COLUMN = "OCC_HOUR"
COUNT_COLUMN = "collision_count"


def analyze_collisions_by_hour(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate collision counts by hour of the day.

    Args:
        df: DataFrame containing collision records with OCC_HOUR column.

    Returns:
        DataFrame with columns [OCC_HOUR, collision_count], sorted by hour.
    """
    result = (
        df.groupby(HOUR_COLUMN)
        .size()
        .reset_index(name=COUNT_COLUMN)
        .sort_values(HOUR_COLUMN)
        .reset_index(drop=True)
    )
    return result
