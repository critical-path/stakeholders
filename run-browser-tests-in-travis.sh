#!/bin/bash

# Install geckodriver.

export PATH=$PATH:$TRAVIS_BUILD_DIR

wget https://github.com/mozilla/geckodriver/releases/download/v0.25.0/geckodriver-v0.25.0-linux64.tar.gz

tar -xvf geckodriver-v0.25.0-linux64.tar.gz


# Start xvfb.

xvfb-run --server-args="-screen 0 1024x768x24" make test


# Start gunicorn in the background.

gunicorn --bind=0.0.0.0:8079 --workers=2 "stakeholders.api:create_api(file='test-database.sqlite3')" &

gunicorn --bind=0.0.0.0:8080 --workers=2 "stakeholders.app:create_app()" &


# Run tests.

pytest -v -m "browser"


# Stop gunicorn.

pkill gunicorn
