import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Gemini API Configuration
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', 'AIzaSyA_nC4vPgqyX-_h92QXYTdMdPFwAQJMmxs')  # Default API key for this project
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is not set") 