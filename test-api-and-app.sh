#!/bin/bash

echo -e "Preparing for tests...\n"

if [[ -f test-database.sqlite3 ]]; then 
    rm test-database.sqlite3;
fi

echo -e "Starting the test API in the background...\n"
gunicorn --bind=0.0.0.0:8079\
         --workers=2\
         "stakeholders.api:create_api(file='test-database.sqlite3')" &

echo -e "Starting the test app in the foreground...\n"
gunicorn --bind=0.0.0.0:8080\
         --workers=2\
         "stakeholders.app:create_app()"
