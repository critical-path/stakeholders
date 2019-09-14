import pytest


# These are all cursory tests, intended simply to 
# validate whether the app returns HTML.

# We test `/`, `/home`, and `/index` with a `GET` request.

@pytest.mark.parametrize("url", ["/", "/home", "/index"])
def test_index_page_get(url, app_client):
    response = app_client.get(url)
    headers = response.headers
    data = response.data.decode()

    assert response.status_code == 200
    assert headers["Content-Type"] == "text/html; charset=utf-8"
    assert "<title>home</title>" in data


# We test `/stakeholders` with a `GET` request.

@pytest.mark.parametrize("url", ["/stakeholders", "/stakeholders?id=1"])
def test_stakeholders_page_get(url, app_client):
    response = app_client.get(url)
    headers = response.headers
    data = response.data.decode()

    assert response.status_code == 200
    assert headers["Content-Type"] == "text/html; charset=utf-8"
    assert "<title>stakeholders</title>" in data


# We test `/stakeholders/add` with a `GET` request.

def test_add_stakeholder_get(app_client):
    response = app_client.get("/stakeholders/add")
    data = response.data.decode()
    headers = response.headers

    assert response.status_code == 200
    assert headers["Content-Type"] == "text/html; charset=utf-8"
    assert "<title>add stakeholder</title>" in data


# We test `/stakeholders/add` with a `POST` request
# and whether it redirects to `/stakeholders`.

def test_add_stakeholder_post(app_client):
    form_data = {
        "name": "stakeholder #1",
        "role": "project sponsor",
        "sentiment": "😀",
        "power": "high",
        "interest": "high"
    }

    response = app_client.post(
        "/stakeholders/add", 
        data=form_data, 
        follow_redirects=True
    )

    data = response.data.decode()
    headers = response.headers

    assert response.status_code == 200
    assert headers["Content-Type"] == "text/html; charset=utf-8"
    assert "<title>stakeholders</title>" in data


# We test `/stakeholders/update` with a `GET` request
# and whether it redirects to `/stakeholders` if no 
# `id` query parameter is present.

def test_update_stakeholder_get(app_client):
    response = app_client.get(
        "/stakeholders/update",
        follow_redirects=True
    )

    data = response.data.decode()
    headers = response.headers

    assert response.status_code == 200
    assert headers["Content-Type"] == "text/html; charset=utf-8"
    assert "<title>stakeholders</title>" in data


# We test `stakeholders/update` with a `GET` request
# and the `id` query parameter.

def test_update_stakeholder_get_with_query_parameter(app_client):
    response = app_client.get("/stakeholders/update?id=1")
    data = response.data.decode()
    headers = response.headers

    assert response.status_code == 200
    assert headers["Content-Type"] == "text/html; charset=utf-8"
    assert "<title>update stakeholder</title>" in data
 

# We test `/stakeholders/update` with a `POST` request
# and whether it redirects to `/stakeholders`. 

def test_update_stakeholder_post(app_client):
    form_data = {
        "id": "1",
        "name": "updated",
        "role": "project sponsor",
        "sentiment": "😀",
        "power": "high",
        "interest": "high"
    }

    response = app_client.post(
        "/stakeholders/update", 
        data=form_data, 
        follow_redirects=True
    )

    data = response.data.decode()
    headers = response.headers

    assert response.status_code == 200
    assert headers["Content-Type"] == "text/html; charset=utf-8"
    assert "<title>stakeholders</title>" in data


# We test `/stakeholders/delete` with a `POST` request
# and whether it redirects to `/stakeholders`. 

def test_delete_stakeholder_post(app_client):
    form_data = {
        "id": "1"
    }

    response = app_client.post(
        "/stakeholders/delete", 
        data=form_data, 
        follow_redirects=True
    )

    data = response.data.decode()
    headers = response.headers

    assert response.status_code == 200
    assert headers["Content-Type"] == "text/html; charset=utf-8"
    assert "<title>stakeholders</title>" in data


# We test `/deliverables` with a `GET` request.

@pytest.mark.parametrize("url", ["/deliverables", "/deliverables?id=1"])
def test_deliverables_page_get(url, app_client):
    response = app_client.get(url)
    headers = response.headers
    data = response.data.decode()

    assert response.status_code == 200
    assert headers["Content-Type"] == "text/html; charset=utf-8"
    assert "<title>deliverables</title>" in data


# We test `/deliverables/add` with a `GET` request.

def test_add_deliverable_get(app_client):
    response = app_client.get("/deliverables/add")
    data = response.data.decode()
    headers = response.headers

    assert response.status_code == 200
    assert headers["Content-Type"] == "text/html; charset=utf-8"
    assert "<title>add deliverable</title>" in data


# We test `/deliverables/add` with a `POST` request
# and whether it redirects to `/deliverables`.

def test_add_deliverable_post(app_client):
    form_data = {
        "name": "deliverable #1",
        "kind": "interactive",
        "medium": "in-person meeting",
        "formality": "formal",
        "frequency": "daily"
    }

    response = app_client.post(
        "/deliverables/add", 
        data=form_data, 
        follow_redirects=True
    )

    data = response.data.decode()
    headers = response.headers

    assert response.status_code == 200
    assert headers["Content-Type"] == "text/html; charset=utf-8"
    assert "<title>deliverables</title>" in data


# We test `/deliverables/update` with a `GET` request
# and whether it redirects to `/deliverables` if no 
# `id` query parameter is present.

def test_update_deliverable_get(app_client):
    response = app_client.get(
        "/deliverables/update",
        follow_redirects=True
    )

    data = response.data.decode()
    headers = response.headers

    assert response.status_code == 200
    assert headers["Content-Type"] == "text/html; charset=utf-8"
    assert "<title>deliverables</title>" in data


# We test `/deliverables/update` with a `GET` request
# and the `id` query parameter.

def test_update_deliverable_get_with_query_parameter(app_client):
    response = app_client.get("/deliverables/update?id=1")
    data = response.data.decode()
    headers = response.headers

    assert response.status_code == 200
    assert headers["Content-Type"] == "text/html; charset=utf-8"
    assert "<title>update deliverable</title>" in data


# We test `/deliverables/update` with a `POST` request
# and whether it redirects to `/deliverables`.

def test_update_deliverable_post(app_client):
    form_data = {
        "id": "1",
        "name": "updated",
        "kind": "interactive",
        "medium": "in-person meeting",
        "formality": "formal",
        "frequency": "daily"
    }

    response = app_client.post(
        "/deliverables/update", 
        data=form_data, 
        follow_redirects=True
    )

    data = response.data.decode()
    headers = response.headers

    assert response.status_code == 200
    assert headers["Content-Type"] == "text/html; charset=utf-8"
    assert "<title>deliverables</title>" in data


# We test `/deliverables/delete` with a `POST` request
# and whether it to `/deliverables`.

def test_delete_deliverable_post(app_client):
    form_data = {
        "id": "1"
    }

    response = app_client.post(
        "/deliverables/delete", 
        data=form_data, 
        follow_redirects=True
    )

    data = response.data.decode()
    headers = response.headers

    assert response.status_code == 200
    assert headers["Content-Type"] == "text/html; charset=utf-8"
    assert "<title>deliverables</title>" in data


# We test `/associations` with a `GET` request.

@pytest.mark.parametrize("url", ["/associations", "/associations?id=1"])
def test_associations_page_get(url, app_client):
    response = app_client.get(url)
    headers = response.headers
    data = response.data.decode()

    assert response.status_code == 200
    assert headers["Content-Type"] == "text/html; charset=utf-8"
    assert "<title>associations</title>" in data


# We test `/associations/add` with a `GET` request.

def test_add_association_get(app_client):
    response = app_client.get("/associations/add")
    data = response.data.decode()
    headers = response.headers

    assert response.status_code == 200
    assert headers["Content-Type"] == "text/html; charset=utf-8"
    assert "<title>add association</title>" in data


# We test `/associations/add` with a `POST` request
# and whether it redirects to `/associations`.

def test_add_association_post(app_client):
    form_data = {
        "stakeholder_id": "1",
        "deliverable_id": "1"
    }

    response = app_client.post(
        "/associations/add", 
        data=form_data, 
        follow_redirects=True
    )

    data = response.data.decode()
    headers = response.headers

    assert response.status_code == 200
    assert headers["Content-Type"] == "text/html; charset=utf-8"
    assert "<title>associations</title>" in data


# We test `/associations/update` with a `GET` request
# and whether it redirects to `/associations` if no 
# `id` query parameter is present.

def test_update_association_get(app_client):
    response = app_client.get(
        "/associations/update",
        follow_redirects=True
    )

    data = response.data.decode()
    headers = response.headers

    assert response.status_code == 200
    assert headers["Content-Type"] == "text/html; charset=utf-8"
    assert "<title>associations</title>" in data


# We test `/associations/update` with a `GET` request
# and the `id` query parameter.

def test_update_association_get_with_query_parameter(app_client):
    response = app_client.get("/associations/update?id=1")
    data = response.data.decode()
    headers = response.headers

    assert response.status_code == 200
    assert headers["Content-Type"] == "text/html; charset=utf-8"
    assert "<title>update association</title>" in data


# We test the endpoint for updating an association
# and whether it redirects to the associations page.

def test_update_association_post(app_client):
    form_data = {
        "id": "1",
        "stakeholder_id": "2",
        "deliverable_id": "1"
    }

    response = app_client.post(
        "/associations/update",
        data=form_data,
        follow_redirects=True
    )

    data = response.data.decode()
    headers = response.headers

    assert response.status_code == 200
    assert headers["Content-Type"] == "text/html; charset=utf-8"
    assert "<title>associations</title>" in data


# We test `/associations/delete` with a `POST` request
# and whether it redirects to `/associations`.

def test_delete_association_post(app_client):
    form_data = {
        "id": "1"
    }

    response = app_client.post(
        "/associations/delete", 
        data=form_data, 
        follow_redirects=True
    )

    data = response.data.decode()
    headers = response.headers

    assert response.status_code == 200
    assert headers["Content-Type"] == "text/html; charset=utf-8"
    assert "<title>associations</title>" in data


# We test `/management-plan` with a `GET` request.

def test_management_plan_page_get(app_client):
    response = app_client.get("/management-plan")
    headers = response.headers
    data = response.data.decode()

    assert response.status_code == 200
    assert headers["Content-Type"] == "text/html; charset=utf-8"
    assert "<title>management plan</title>" in data
