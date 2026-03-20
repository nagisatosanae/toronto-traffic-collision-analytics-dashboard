"""Collision severity analytics module."""

import pandas as pd


def analyze_collision_severity(df: pd.DataFrame) -> pd.DataFrame:
    """Summarize collisions by severity category.

    Categories: Fatal, Injury, FTR (Fail to Remain), Property Damage.

    Args:
        df: DataFrame containing collision records.

    Returns:
        DataFrame with columns [severity, collision_count].
    """
    severity = {
        "Fatal": (df["FATALITIES"] > 0).sum(),
        "Injury": (df["INJURY_COLLISIONS"] == "YES").sum(),
        "FTR": (df["FTR_COLLISIONS"] == "YES").sum(),
        "Property Damage": (df["PD_COLLISIONS"] == "YES").sum(),
    }
    result = pd.DataFrame(
        list(severity.items()),
        columns=["severity", "collision_count"]
    )
    return result
