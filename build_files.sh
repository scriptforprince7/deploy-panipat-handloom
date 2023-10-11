#!/bin/bash

# Exit on error
set -e

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Run Django collectstatic command
echo "Running collectstatic..."
python3.9 manage.py collectstatic

