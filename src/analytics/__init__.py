"""Analytics package for Toronto Traffic Collision dataset.

Consolidates all analysis modules into a single package.
"""

from src.analytics.hourly import analyze_collisions_by_hour
from src.analytics.neighbourhood import analyze_collisions_by_neighbourhood
from src.analytics.vulnerable_users import analyze_vulnerable_users
from src.analytics.severity import analyze_collision_severity
