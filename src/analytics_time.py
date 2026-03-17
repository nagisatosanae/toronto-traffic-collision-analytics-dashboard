import pandas as pd


def get_collision_count_by_hour(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("OCC_HOUR")
        .size()
        .reset_index(name="COUNT")
    )