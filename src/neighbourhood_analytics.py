"""Neighbourhood collision analytics module."""

import pandas as pd


def analyze_collisions_by_neighbourhood(df: pd.DataFrame) -> pd.DataFrame:
    """Analyze collisions by neighbourhood."""
    filtered = df[df["NEIGHBOURHOOD_158"] != "NSA"]
    result = filtered.groupby("NEIGHBOURHOOD_158").size().reset_index(name="collision_count")
    result = result.sort_values("collision_count", ascending=False).reset_index(drop=True)
    return result
