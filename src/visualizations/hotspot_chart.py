"""Neighbourhood collision hotspot visualization module.

Generates horizontal bar charts for identifying high-risk
collision areas by neighbourhood.
"""

import pandas as pd
import matplotlib.pyplot as plt

TITLE = "Top Collision Hotspots by Neighbourhood"
X_LABEL = "Number of Collisions"
Y_LABEL = "Neighbourhood"
BAR_COLOR = "#F44336"


def create_hotspot_chart(df: pd.DataFrame, top_n: int = 10) -> plt.Figure:
    """Create a horizontal bar chart of top collision neighbourhoods.

    Args:
        df: DataFrame with columns [NEIGHBOURHOOD_158, collision_count],
            sorted by collision_count descending.
        top_n: Number of top neighbourhoods to display.

    Returns:
        matplotlib Figure object containing the horizontal bar chart.
    """
    top = df.head(top_n)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(top["NEIGHBOURHOOD_158"], top["collision_count"], color=BAR_COLOR)
    ax.set_title(TITLE)
    ax.set_xlabel(X_LABEL)
    ax.set_ylabel(Y_LABEL)
    ax.invert_yaxis()
    fig.tight_layout()
    return fig
