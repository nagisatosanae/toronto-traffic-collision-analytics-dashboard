import pandas as pd
from src.clean_data import (
    handle_missing_values,
    convert_data_types,
    remove_invalid_or_duplicate_records,
    clean_collision_data
)


def test_handle_missing_values_removes_missing_date_time():
    df = pd.DataFrame({
        "DATE": ["2024-01-01", None],
        "TIME": ["08:00", "09:00"],
        "NEIGHBOURHOOD": ["North York", None]
    })

    result = handle_missing_values(df)

    assert len(result) == 1
    assert result.iloc[0]["DATE"] == "2024-01-01"


def test_handle_missing_values_fills_neighbourhood():
    df = pd.DataFrame({
        "DATE": ["2024-01-01"],
        "TIME": ["08:00"],
        "NEIGHBOURHOOD": [None]
    })

    result = handle_missing_values(df)

    assert result.iloc[0]["NEIGHBOURHOOD"] == "Unknown"


def test_convert_data_types():
    df = pd.DataFrame({
        "DATE": ["2024-01-01"],
        "TIME": ["08:30"],
        "INJURIES": ["2"],
        "FATALITIES": ["0"]
    })

    result = convert_data_types(df)

    assert pd.api.types.is_datetime64_any_dtype(result["DATE"])
    assert pd.api.types.is_datetime64_any_dtype(result["TIME"])
    assert pd.api.types.is_numeric_dtype(result["INJURIES"])


def test_remove_invalid_or_duplicate_records():
    df = pd.DataFrame({
        "DATE": [pd.Timestamp("2024-01-01"), pd.Timestamp("2024-01-01"), pd.NaT],
        "TIME": [pd.Timestamp("2024-01-01 08:00"), pd.Timestamp("2024-01-01 08:00"), pd.Timestamp("2024-01-01 09:00")]
    })

    result = remove_invalid_or_duplicate_records(df)

    assert len(result) == 1


def test_clean_collision_pipeline():
    df = pd.DataFrame({
        "DATE": ["2024-01-01", "invalid"],
        "TIME": ["08:00", "09:00"],
        "NEIGHBOURHOOD": [None, "Downtown"],
        "INJURIES": ["1", "2"],
        "FATALITIES": ["0", "0"]
    })

    result = clean_collision_data(df)

    assert len(result) == 1
