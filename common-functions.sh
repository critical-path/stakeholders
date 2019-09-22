#!/bin/bash


DATABASE_FILE="test-database.sqlite3"
LOG_FILE="geckodriver.log"


function check-database-file {
  test -e ${DATABASE_FILE}

  if [[ $? == 0 ]]; then
    rm ${DATABASE_FILE}
  fi
}


function check-log-file {
  test -e ${LOG_FILE}

  if [[ $? == 0 ]]; then
    ln -s -f /dev/null ${LOG_FILE}
  else
    ln -s /dev/null ${LOG_FILE}
  fi
}


function start-gunicorn {
  gunicorn --bind=0.0.0.0:8079\
           --workers=2\
           "stakeholders.api:create_api(file='test-database.sqlite3')" &

  gunicorn --bind=0.0.0.0:8080\
           --workers=2\
           "stakeholders.app:create_app()" &
}


function stop-gunicorn {
  pkill gunicorn
}


function run-tests {
  pytest -v -m "browser"
}
