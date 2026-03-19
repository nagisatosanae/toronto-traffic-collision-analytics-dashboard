"""Streamlit dashboard for Toronto Traffic Collision Analytics.

Provides an interactive web interface to explore Toronto
traffic collision data with visual analytics.
"""

import streamlit as st
import matplotlib.pyplot as plt
from src.data_loader import load_dataset
from src.clean_data import clean_collision_data
from src.analytics import (
    analyze_collisions_by_hour,
    analyze_collisions_by_neighbourhood,
    analyze_collision_severity,
    analyze_vulnerable_users,
)
from src.visualizations import create_hourly_chart, create_hotspot_chart
from src.filters import filter_by_year

PAGE_TITLE = "Toronto Traffic Collision Analytics"
ERROR_MSG = "Dataset not found. Please place the CSV file in the data/ folder."


def load_data():
    """Load and clean the dataset."""
    df = load_dataset()
    df = clean_collision_data(df)
    return df


def render_sidebar(df):
    """Render sidebar filters and return filtered DataFrame."""
    st.sidebar.header("Filters")
    years = sorted(df["OCC_YEAR"].unique())
    selected_year = st.sidebar.selectbox("Select Year", ["All"] + list(years))

    if selected_year != "All":
        df = filter_by_year(df, selected_year)

    st.sidebar.markdown("---")
    st.sidebar.markdown(f"**Total Records:** {len(df):,}")
    return df


def render_overview(df):
    """Render the overview metrics."""
    total = len(df)
    fatal = (df["FATALITIES"] > 0).sum()
    injury = (df["INJURY_COLLISIONS"] == "YES").sum()
    pedestrian = (df["PEDESTRIAN"] == "YES").sum()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Collisions", f"{total:,}")
    col2.metric("Fatal", f"{fatal:,}")
    col3.metric("Injury", f"{injury:,}")
    col4.metric("Pedestrian", f"{pedestrian:,}")


def render_hourly_section(df):
    """Render the hourly collision analysis section."""
    hourly = analyze_collisions_by_hour(df)
    st.pyplot(create_hourly_chart(hourly))


def render_hotspot_section(df):
    """Render the neighbourhood hotspot section."""
    neighbourhood = analyze_collisions_by_neighbourhood(df)
    st.pyplot(create_hotspot_chart(neighbourhood))


def render_severity_section(df):
    """Render the collision severity breakdown."""
    severity = analyze_collision_severity(df)
    fig, ax = plt.subplots(figsize=(6, 4))
    colors = ["#d32f2f", "#ff9800", "#ffc107", "#4caf50"]
    ax.bar(severity["severity"], severity["collision_count"], color=colors)
    ax.set_title("Collision Severity Breakdown")
    ax.set_ylabel("Number of Collisions")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    st.pyplot(fig)


def render_vulnerable_users_section(df):
    """Render the pedestrian and cyclist analysis."""
    users = analyze_vulnerable_users(df)
    fig, ax = plt.subplots(figsize=(4, 4))
    colors = ["#1976d2", "#388e3c"]
    ax.pie(
        users["collision_count"],
        labels=users["user_type"],
        autopct="%1.1f%%",
        colors=colors,
        startangle=90,
    )
    ax.set_title("Pedestrian vs Cyclist Collisions")
    plt.tight_layout()
    st.pyplot(fig)


def main():
    """Main dashboard entry point."""
    st.set_page_config(page_title=PAGE_TITLE, layout="wide")
    st.title(PAGE_TITLE)

    try:
        df = load_data()
    except FileNotFoundError:
        st.error(ERROR_MSG)
        return

    df = render_sidebar(df)

    # Overview metrics
    render_overview(df)
    st.markdown("---")

    # Tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "Hourly Analysis",
        "Neighbourhood Hotspots",
        "Severity Breakdown",
        "Vulnerable Road Users",
    ])

    with tab1:
        render_hourly_section(df)

    with tab2:
        render_hotspot_section(df)

    with tab3:
        render_severity_section(df)

    with tab4:
        render_vulnerable_users_section(df)


if __name__ == "__main__":
    main()
