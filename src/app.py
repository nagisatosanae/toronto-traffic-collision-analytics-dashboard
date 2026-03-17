"""Streamlit dashboard for Toronto Traffic Collision Analytics."""

import streamlit as st
from src.data_loader import load_dataset
from src.clean_data import clean_collision_data
from src.analytics import analyze_collisions_by_hour
from src.neighbourhood_analytics import analyze_collisions_by_neighbourhood
from src.hourly_visualization import create_hourly_chart
from src.hotspot_visualization import create_hotspot_chart
from src.filters import filter_by_year


def main():
    """Main dashboard entry point."""
    st.title("Toronto Traffic Collision Analytics")

    try:
        df = load_dataset()
        df = clean_collision_data(df)
    except FileNotFoundError:
        st.error("Dataset not found. Place CSV in data/ folder.")
        return

    years = sorted(df["OCC_YEAR"].unique())
    selected_year = st.sidebar.selectbox("Select Year", ["All"] + list(years))

    if selected_year != "All":
        df = filter_by_year(df, selected_year)

    st.header("Collisions by Hour of Day")
    hourly = analyze_collisions_by_hour(df)
    st.pyplot(create_hourly_chart(hourly))

    st.header("Top Collision Hotspots")
    neighbourhood = analyze_collisions_by_neighbourhood(df)
    st.pyplot(create_hotspot_chart(neighbourhood))


if __name__ == "__main__":
    main()
