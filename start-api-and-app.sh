#!/bin/bash

echo -e "Starting the API in the background...\n"
gunicorn --bind=0.0.0.0:8079\
         --workers=2\
         "stakeholders.api:create_api()" &

echo -e "Starting the app in the foreground...\n"
gunicorn --bind=0.0.0.0:8080\
         --workers=2\
         "stakeholders.app:create_app()"
