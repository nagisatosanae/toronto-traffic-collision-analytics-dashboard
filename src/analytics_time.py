import pandas as pd

def get_collision_count_by_hour(df: pd.DataFrame) -> pd.DataFrame:
    """Return collision counts grouped by hour."""
    return (
        df.groupby("OCC_HOUR")
        .size()
        .reset_index(name="COUNT")
        .sort_values("OCC_HOUR")
        .reset_index(drop=True)
    )