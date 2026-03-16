"""Analytics module for Toronto Traffic Collision dataset."""

import pandas as pd


def analyze_collisions_by_hour(df: pd.DataFrame) -> pd.DataFrame:
    """Analyze collisions by hour of the day."""
    result = df.groupby("OCC_HOUR").size().reset_index(name="collision_count")
    result = result.sort_values("OCC_HOUR").reset_index(drop=True)
    return result
