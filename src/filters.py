import pandas as pd


def filter_by_year(df: pd.DataFrame, year: int) -> pd.DataFrame:
    """Return rows that match the selected year."""
    return df[df["OCC_YEAR"] == year]