#!/bin/bash

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
