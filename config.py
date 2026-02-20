# Configuration for APIs, Coordinates, Air Quality Limits, and Daily Restrictions

# APIs
API_KEY = 'your_api_key_here'  # Replace with your real API key
BASE_URL = 'https://api.example.com/'  # Replace with your real base URL

# Coordinates
COORDINATES = {
    'latitude': 19.4326,
    'longitude': -99.1332
}

# Air Quality Limits (example values)
AIR_QUALITY_LIMITS = {
    'good': 0,
    'moderate': 51,
    'unhealthy_for_sensitive_groups': 101,
    'unhealthy': 151,
    'very_unhealthy': 201,
    'hazardous': 301
}

# Daily Restrictions (example values)
DAILY_RESTRICTIONS = {
    'max_allowed_pm2_5': 35,  # in µg/m³
    'max_allowed_pm10': 50,   # in µg/m³
}