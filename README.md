"# toronto-traffic-collision-analytics-dashboard" 
"# toronto-traffic-collision-analytics-dashboard" 
# Toronto Traffic Collision Analytics Tool

A Python-based analytics tool for analyzing Toronto traffic collision data. Built using Agile methodology with two one-week sprints.

## Project Overview

This tool loads, cleans, and analyzes the Toronto Traffic Collisions Open Dataset to provide meaningful insights such as:
- Collision frequency by hour of day
- High-risk neighbourhoods
- Collision severity patterns
- Involvement of pedestrians, cyclists, and other road users

## Tech Stack

- **Language**: Python 3.10+
- **Dashboard**: Streamlit
- **Testing**: pytest
- **Data Processing**: pandas
- **Visualization**: matplotlib / plotly

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nagisatosanae/toronto-traffic-collision-analytics-dashboard.git
   cd toronto-traffic-collision-analytics-dashboard
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate        # macOS/Linux
   venv\Scripts\activate           # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Place the dataset file in the `data/` directory.

## Running the Application

### Run the Streamlit Dashboard
```bash
streamlit run app.py
```

### Run Tests
```bash
pytest tests/ -v
```

## Dataset

The dataset (`Traffic_Collisions_Open_Data.csv`) contains Toronto traffic collision records with the following key fields:

| Column | Description |
|--------|-------------|
| OCC_DATE | Date of occurrence |
| OCC_HOUR | Hour of occurrence (0-23) |
| OCC_YEAR | Year of occurrence |
| NEIGHBOURHOOD_158 | Neighbourhood name |
| FATALITIES | Number of fatalities |
| INJURY_COLLISIONS | Whether injuries occurred |
| AUTOMOBILE | Automobile involvement |
| BICYCLE | Bicycle involvement |
| PEDESTRIAN | Pedestrian involvement |
| MOTORCYCLE | Motorcycle involvement |


```