import pandas as pd
from src.analytics_time import get_collision_count_by_hour


def test_get_collision_count_by_hour_basic():
    df = pd.DataFrame({
        "OCC_HOUR": [1, 1, 2]
    })

    result = get_collision_count_by_hour(df)

    assert result["COUNT"].sum() == 3