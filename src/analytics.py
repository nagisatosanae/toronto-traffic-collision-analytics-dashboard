"""
Public analytics interface for the Toronto Traffic Collision Analytics Tool.

This module preserves the original import path while delegating
hourly analytics logic to the modularized implementation.
"""

from src.analytics_time import analyze_collisions_by_hour

__all__ = ["analyze_collisions_by_hour"]
