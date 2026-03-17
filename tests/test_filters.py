import pandas as pd
from src.filters import filter_by_year
from src.filters import filter_by_severity


def test_filter_by_year_returns_only_selected_year():
    df = pd.DataFrame({
        "OCC_YEAR": [2022, 2023, 2023],
        "VALUE": [10, 20, 30]
    })

    result = filter_by_year(df, 2023)

    assert len(result) == 2
    assert set(result["VALUE"]) == {20, 30}

def test_filter_by_severity_returns_only_selected_level():
    df = pd.DataFrame({
        "ACCLASS": ["Fatal", "Non-Fatal", "Fatal"],
        "VALUE": [1, 2, 3]
    })

    result = filter_by_severity(df, "Fatal")

    assert len(result) == 2