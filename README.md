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

## Project Structure

```
project/
├── src/
│   ├── __init__.py
│   ├── data_loader.py          # Data loading and validation
│   ├── data_cleaner.py         # Data cleaning and preprocessing
│   ├── analytics.py            # Analysis functions
│   └── visualizations.py       # Chart and plot generation
├── tests/
│   ├── test_data_loader.py
│   ├── test_data_cleaner.py
│   ├── test_analytics.py
│   └── test_visualizations.py
├── data/
│   └── Traffic_Collisions_Open_Data.csv
├── app.py                      # Streamlit dashboard
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-org>/<repo-name>.git
   cd <repo-name>
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

4. Download the dataset and place it in the `data/` directory:
   ```
   data/Traffic_Collisions_Open_Data.csv
   ```
   > [!WARNING]
   > The CSV file (~142 MB) is not included in the repository due to GitHub's file size limit. Each team member must manually place the dataset in the `data/` folder before running the application.

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

> [!IMPORTANT]
> The dataset file (`Traffic_Collisions_Open_Data.csv`, ~142 MB) is **not included** in this repository because it exceeds GitHub's 100 MB file size limit.

> [!NOTE]
> **For developers:** After cloning the repo, download the CSV and place it at `data/Traffic_Collisions_Open_Data.csv` before running the application or tests. The `data/` folder is git-ignored.

The dataset contains Toronto traffic collision records with the following key fields:

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

## Agile Project Management

- **Project Board**: [Taiga Project Link]
- **Sprints**: 2 one-week sprints
- **Sprint 1**: Data loading, cleaning, and basic analytics
- **Sprint 2**: Dashboard, visualizations, and refinements

## Team Members

- [Member 1 Name] - [Role]
- [Member 2 Name] - [Role]
- [Member 3 Name] - [Role]
