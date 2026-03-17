"""Pedestrian and cyclist collision analytics module."""

import pandas as pd


def analyze_vulnerable_users(df: pd.DataFrame) -> pd.DataFrame:
    """Summarize collisions involving pedestrians and cyclists."""
    summary = {
        "Pedestrian": (df["PEDESTRIAN"] == "YES").sum(),
        "Cyclist": (df["BICYCLE"] == "YES").sum(),
    }
    result = pd.DataFrame(
        list(summary.items()),
        columns=["user_type", "collision_count"]
    )
    return result
