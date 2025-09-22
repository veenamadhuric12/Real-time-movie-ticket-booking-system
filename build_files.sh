#!/usr/bin/env bash

# exit immediately on errors
set -e

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running migrations..."
python manage.py makemigrations --no-input
python manage.py migrate --no-input

echo "Collecting static files..."
python manage.py collectstatic --no-input
