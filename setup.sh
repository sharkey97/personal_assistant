#!/bin/bash

echo "Setup starting..."

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/Scripts/activate
# If running these commands individually, run the below instead
# source venv/Scripts/activate

# Install dependencies
pip install -r requirements.txt

# Copy environment variables template
cp .env.example .env

echo "Setup is complete. You can now run the application with 'python main.py'."
