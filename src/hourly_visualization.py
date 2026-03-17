"""Hourly collision trend visualization module.

Generates bar charts for collision trends by hour of day.
"""

import pandas as pd
import matplotlib.pyplot as plt

TITLE = "Collisions by Hour of Day"
X_LABEL = "Hour (0-23)"
Y_LABEL = "Number of Collisions"
BAR_COLOR = "#2196F3"


def create_hourly_chart(df: pd.DataFrame) -> plt.Figure:
    """Create a bar chart showing collisions by hour of day.

    Args:
        df: DataFrame with columns [OCC_HOUR, collision_count].

    Returns:
        matplotlib Figure object containing the bar chart.
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(df["OCC_HOUR"], df["collision_count"], color=BAR_COLOR)
    ax.set_title(TITLE)
    ax.set_xlabel(X_LABEL)
    ax.set_ylabel(Y_LABEL)
    ax.set_xticks(range(24))
    fig.tight_layout()
    return fig
