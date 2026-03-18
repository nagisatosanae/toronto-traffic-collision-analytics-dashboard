"""Pedestrian and cyclist collision analytics module.

Provides functions to analyze collisions involving vulnerable road users.
"""

import pandas as pd


def analyze_vulnerable_users(df: pd.DataFrame) -> pd.DataFrame:
    """Summarize collisions involving pedestrians and cyclists.

    Args:
        df: DataFrame containing collision records.

    Returns:
        DataFrame with columns [user_type, collision_count].
    """
    summary = {
        "Pedestrian": (df["PEDESTRIAN"] == "YES").sum(),
        "Cyclist": (df["BICYCLE"] == "YES").sum(),
    }
    result = pd.DataFrame(
        list(summary.items()),
        columns=["user_type", "collision_count"]
    )
    return result
