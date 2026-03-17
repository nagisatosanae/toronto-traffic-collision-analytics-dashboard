"""Hourly collision trend visualization module."""

import pandas as pd
import matplotlib.pyplot as plt


def create_hourly_chart(df: pd.DataFrame) -> plt.Figure:
    """Create a bar chart showing collisions by hour."""
    fig, ax = plt.subplots()
    ax.bar(df["OCC_HOUR"], df["collision_count"])
    ax.set_title("Collisions by Hour of Day")
    ax.set_xlabel("Hour")
    ax.set_ylabel("Number of Collisions")
    return fig
