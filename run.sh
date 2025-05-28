#!/bin/bash

# Setup script for MindCrafter with backend-only Gemini API integration

# Create and activate virtual environment
echo "Setting up Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Start the application
echo "Starting the application..."
echo "The application will be available at http://localhost:5000"
echo "Press Ctrl+C to stop the server"
python app.py
