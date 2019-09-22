#!/bin/bash

echo "Starting the API in the background..."
gunicorn --bind=0.0.0.0:8079 --workers=2 "stakeholders.api:create_api()" &

echo "Starting the app in the foreground..."
gunicorn --bind=0.0.0.0:8080 --workers=2 "stakeholders.app:create_app()"
