"""Configuration settings for the EV Research application."""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
NREL_API_KEY = os.getenv('NREL_API_KEY')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# API Endpoints
NREL_BASE_URL = "https://developer.nrel.gov/api/alt-fuel-stations/v1"
NREL_STATION_SEARCH_ENDPOINT = f"{NREL_BASE_URL}/nearest.json"

# Gemini Model Settings
GEMINI_MODEL = "gemini-2.5-flash-preview-04-17"
GEMINI_FALLBACK_MODEL = "gemini-2.5-pro-preview-03-25"
DEFAULT_TEMPERATURE = 0.7

# Report Generation Settings
DEFAULT_REPORT_FORMAT = "markdown"
SUPPORTED_FORMATS = ["markdown", "pdf", "docx"]
