import pandas as pd


def handle_missing_values(df):
    """
    Task #16
    Handle missing values in important columns
    """

    df = df.copy()

    # remove rows where DATE or TIME is missing
    required_columns = ["DATE", "TIME"]

    for col in required_columns:
        if col in df.columns:
            df = df[df[col].notna()]

    # fill neighbourhood with Unknown if missing
    if "NEIGHBOURHOOD" in df.columns:
        df["NEIGHBOURHOOD"] = df["NEIGHBOURHOOD"].fillna("Unknown")

    return df


def convert_data_types(df):
    """
    Task #17
    Convert date, time and numeric columns
    """

    df = df.copy()

    # convert DATE column
    if "DATE" in df.columns:
        df["DATE"] = pd.to_datetime(df["DATE"], errors="coerce")

    # convert TIME column
    if "TIME" in df.columns:
        df["TIME"] = pd.to_datetime(df["TIME"], errors="coerce")

    # convert numeric fields if they exist
    numeric_columns = ["INJURIES", "FATALITIES"]

    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


def remove_invalid_or_duplicate_records(df):
    """
    Task #18
    Remove duplicate and invalid records
    """

    df = df.copy()

    # remove duplicate rows
    df = df.drop_duplicates()

    # remove rows where date conversion failed
    if "DATE" in df.columns:
        df = df[df["DATE"].notna()]

    return df


def clean_collision_data(df):
    """
    Main cleaning pipeline
    """

    df = handle_missing_values(df)
    df = convert_data_types(df)
    df = remove_invalid_or_duplicate_records(df)

    return df