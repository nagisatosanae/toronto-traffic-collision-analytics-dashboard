"""Neighbourhood collision hotspot visualization module."""

import pandas as pd
import matplotlib.pyplot as plt


def create_hotspot_chart(df: pd.DataFrame, top_n: int = 10) -> plt.Figure:
    """Create a horizontal bar chart showing top collision neighbourhoods."""
    top = df.head(top_n)
    fig, ax = plt.subplots()
    ax.barh(top["NEIGHBOURHOOD_158"], top["collision_count"])
    ax.set_title("Top Collision Hotspots by Neighbourhood")
    ax.invert_yaxis()
    return fig
