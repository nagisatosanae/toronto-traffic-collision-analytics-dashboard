"""Streamlit dashboard for Toronto Traffic Collision Analytics.

Provides an interactive web interface to explore Toronto
traffic collision data with visual analytics.
"""

import streamlit as st
from src.data_loader import load_dataset
from src.clean_data import clean_collision_data
from src.analytics import analyze_collisions_by_hour, analyze_collisions_by_neighbourhood
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
    years = sorted(df["OCC_YEAR"].unique())
    selected_year = st.sidebar.selectbox("Select Year", ["All"] + list(years))

    if selected_year != "All":
        df = filter_by_year(df, selected_year)
    return df


def render_hourly_section(df):
    """Render the hourly collision analysis section."""
    st.header("Collisions by Hour of Day")
    hourly = analyze_collisions_by_hour(df)
    st.pyplot(create_hourly_chart(hourly))


def render_hotspot_section(df):
    """Render the neighbourhood hotspot section."""
    st.header("Top Collision Hotspots")
    neighbourhood = analyze_collisions_by_neighbourhood(df)
    st.pyplot(create_hotspot_chart(neighbourhood))


def main():
    """Main dashboard entry point."""
    st.title(PAGE_TITLE)

    try:
        df = load_data()
    except FileNotFoundError:
        st.error(ERROR_MSG)
        return

    df = render_sidebar(df)
    render_hourly_section(df)
    render_hotspot_section(df)


if __name__ == "__main__":
    main()
