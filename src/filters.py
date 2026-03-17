import pandas as pd

def filter_by_year(df: pd.DataFrame, year: int) -> pd.DataFrame:
   result = df.copy()
   return result[result["OCC_YEAR"] == year]