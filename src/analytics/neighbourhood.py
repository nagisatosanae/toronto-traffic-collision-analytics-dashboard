"""Neighbourhood collision analytics module.

Provides functions to aggregate collision data by neighbourhood
for identifying high-risk areas.
"""

import pandas as pd

NEIGHBOURHOOD_COLUMN = "NEIGHBOURHOOD_158"
COUNT_COLUMN = "collision_count"
NSA_VALUE = "NSA"


def analyze_collisions_by_neighbourhood(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate collision counts by neighbourhood, excluding NSA records.

    Args:
        df: DataFrame containing collision records with NEIGHBOURHOOD_158 column.

    Returns:
        DataFrame with columns [NEIGHBOURHOOD_158, collision_count],
        sorted by collision count in descending order.
    """
    filtered = df[df[NEIGHBOURHOOD_COLUMN] != NSA_VALUE]
    result = (
        filtered.groupby(NEIGHBOURHOOD_COLUMN)
        .size()
        .reset_index(name=COUNT_COLUMN)
        .sort_values(COUNT_COLUMN, ascending=False)
        .reset_index(drop=True)
    )
    return result
