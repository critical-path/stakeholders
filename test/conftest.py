import json

import flask.testing
import werkzeug

import pytest
import selenium.webdriver
import selenium.webdriver.firefox.options

import stakeholders.api
import stakeholders.app
import stakeholders.db


# This registers a custom marker, `pytest.mark.browser`.

def pytest_configure(config):
    config.addinivalue_line(
        "markers", 
        "browser: Run browser tests with Selenium, Firefox, and geckodriver."
    )


# This represents the path to a database file.

@pytest.fixture
def file(tmp_path):
    yield tmp_path.joinpath("test-database.sqlite3").as_posix()


# This represents a database with a `stakeholders` table,
# a `deliverables` table, and four records.

@pytest.fixture
def db(file):
    with stakeholders.db.Database(file=file) as db:
        db.create_stakeholders_table()

        db.insert_into_stakeholders_table(**{
            "name": "stakeholder #1",
            "role": "project sponsor",
            "sentiment": "😀",
            "power": "high",
            "interest": "high",
            "approach": "monitor closely"
        })

        db.insert_into_stakeholders_table(**{
            "name": "stakeholder #2",
            "role": "customer",
            "sentiment": "😐",
            "power": "high",
            "interest": "low",
            "approach": "keep satisfied"
        })

        db.create_deliverables_table()

        db.insert_into_deliverables_table(**{
            "name": "deliverable #1",
            "kind": "interactive",
            "medium": "in-person meeting",
            "formality": "formal",
            "frequency": "daily"
        })

        db.insert_into_deliverables_table(**{
            "name": "deliverable #2",
            "kind": "push",
            "medium": "video/teleconference",
            "formality": "casual",
            "frequency": "weekly"
        })

        db.create_associations_table()

        db.insert_into_associations_table(**{
            "stakeholder_id": 1,
            "deliverable_id": 1
        })

        db.insert_into_associations_table(**{
            "stakeholder_id": 2,
            "deliverable_id": 2
        })
     
        yield db


# This represents the result of calling 
# `db.select_all_from_associations_table()`.

@pytest.fixture
def records():
    return [
        {
            "id": 1,
            "stakeholder_id": 1,
            "stakeholder_name": "stakeholder #1",
            "stakeholder_approach": "monitor closely",
            "deliverable_id": 1,
            "deliverable_name": "deliverable #1"
        },
        {
            "id": 3,
            "stakeholder_id": 1,
            "stakeholder_name": "stakeholder #1",
            "stakeholder_approach": "monitor closely",
            "deliverable_id": 2,
            "deliverable_name": "deliverable #2"
        },
        {
            "id": 2,
            "stakeholder_id": 2,
            "stakeholder_name": "stakeholder #2",
            "stakeholder_approach": "keep satisfied",
            "deliverable_id": 2,
            "deliverable_name": "deliverable #2"
        },
        {
            "id": 4,
            "stakeholder_id": 3,
            "stakeholder_name": "stakeholder #3",
            "stakeholder_approach": "keep informed",
            "deliverable_id": 1,
            "deliverable_name": "deliverable #1"
        },
        {
            "id": 5,
            "stakeholder_id": 4,
            "stakeholder_name": "stakeholder #4",
            "stakeholder_approach": "monitor",
            "deliverable_id": 1,
            "deliverable_name": "deliverable #1"
        },
        {
            "id": 6,
            "stakeholder_id": 5,
            "stakeholder_name": "stakeholder #5",
            "stakeholder_approach": "unknown",
            "deliverable_id": 1,
            "deliverable_name": "deliverable #1"
        }
    ]


# This represents an instance of the API.

@pytest.fixture
def api(file):
    yield stakeholders.api.create_api(file=file)


# This represents the API's client.
# We subclass the `werkzeug.Response` class by adding
# a `json` method.  This makes `werkzeug.Response` a
# better proxy for `requests.Response`.

@pytest.fixture
def api_client(api):
    class JSONResponse(werkzeug.Response):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def json(self):
            data = self.get_data().decode()
            return json.loads(data)

    return flask.testing.FlaskClient(api, JSONResponse)


# This represents an instance of the app.

@pytest.fixture
def app(api_client):
    yield stakeholders.app.create_app(requester=api_client)


# This represents the app's client.

@pytest.fixture
def app_client(app):
    return app.test_client()


# This represents an instance of the Firefox web browser.

@pytest.fixture
def browser():
    options = selenium.webdriver.firefox.options.Options()
    options.add_argument("--headless")

    browser = selenium.webdriver.Firefox(options=options)
    browser.implicitly_wait(5)

    yield browser

    browser.close()
