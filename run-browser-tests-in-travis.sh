#!/bin/bash

# Download geckodriver.
wget --quiet https://github.com/mozilla/geckodriver/releases/download/v0.25.0/geckodriver-v0.25.0-linux64.tar.gz

# Extract geckodriver.
tar -xvf geckodriver-v0.25.0-linux64.tar.gz

# Add geckodriver to PATH environment variable.
export PATH=$PATH:$TRAVIS_BUILD_DIR

# Start xvfb.
xvfb-run make test

# Import common functions.
source common-functions.sh

# Check database file.
check-database-file

# Check log file.
check-log-file

# Start gunicorn.
start-gunicorn

# Run browser tests.
run-tests

# Stop gunicorn.
stop-gunicorn

# Check database file again.
check-database-file
