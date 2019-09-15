import collections
import json
import pytest
import stakeholders.api


ADD_STAKEHOLDER = "/api/v1/stakeholders/add"
DELETE_STAKEHOLDER = "/api/v1/stakeholders/delete"
SHOW_STAKEHOLDERS = "/api/v1/stakeholders/show"
UPDATE_STAKEHOLDER = "/api/v1/stakeholders/update"

ADD_DELIVERABLE = "/api/v1/deliverables/add"
DELETE_DELIVERABLE = "/api/v1/deliverables/delete"
SHOW_DELIVERABLES = "/api/v1/deliverables/show"
UPDATE_DELIVERABLE = "/api/v1/deliverables/update"

ADD_ASSOCIATION = "/api/v1/associations/add"
DELETE_ASSOCIATION = "/api/v1/associations/delete"
SHOW_ASSOCIATIONS = "/api/v1/associations/show"
UPDATE_ASSOCIATION = "/api/v1/associations/update"

SHOW_MANAGEMENT_PLAN = "/api/v1/management-plan/show"


# We test all of the stakeholder-related endpoints.
#
# In an ideal world, we would split this single function into multiples ones.
#
# This would require us either to save state between tests or to create
# a large number of text fixtures, neither of which we want to do.

def test_stakeholders_endpoints(api_client):
    # We send a request to the API to show all stakeholders.
    # We expect the response to contain zero stakeholders.

    response = api_client.get(SHOW_STAKEHOLDERS)
    data = json.loads(response.data.decode())

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert len(data) == 0


    # We send a request to the API to add a stakeholder.

    form_data = {
        "name": "stakeholder #1",
        "role": "project sponsor",
        "sentiment": "😀",
        "power": "high",
        "interest": "high"
    }

    response = api_client.post(ADD_STAKEHOLDER, data=form_data)
    data = response.data.decode()

    assert response.status_code == 200
    assert data == "Success"


    # We send a request to the API to add a second stakeholder.

    form_data = {
        "name": "stakeholder #2",
        "role": "customer",
        "sentiment": "😐",
        "power": "high",
        "interest": "low"
    }

    response = api_client.post(ADD_STAKEHOLDER, data=form_data)
    data = response.data.decode()

    assert response.status_code == 200
    assert data == "Success"


    # We send a request to the API to show all stakeholders.
    # We expect the response to contain both stakeholders.

    response = api_client.get(SHOW_STAKEHOLDERS)
    data = json.loads(response.data.decode())

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert len(data) == 2

    assert data[0]["id"] == 1
    assert data[0]["name"] == "stakeholder #1"
    assert data[0]["role"] == "project sponsor"
    assert data[0]["sentiment"] == "😀"
    assert data[0]["power"] == "high"
    assert data[0]["interest"] == "high"
    assert data[0]["approach"] == "monitor closely"

    assert data[1]["id"] == 2
    assert data[1]["name"] == "stakeholder #2"
    assert data[1]["role"] == "customer"
    assert data[1]["sentiment"] == "😐"
    assert data[1]["power"] == "high"
    assert data[1]["interest"] == "low"
    assert data[1]["approach"] == "keep satisfied"


    # We send a request to the API to show the first stakeholder.
    # We expect the response to contain only that stakeholder.

    response = api_client.get("{}?id=1".format(SHOW_STAKEHOLDERS))
    data = json.loads(response.data.decode())

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert len(data) == 1

    assert data[0]["id"] == 1
    assert data[0]["name"] == "stakeholder #1"
    assert data[0]["role"] == "project sponsor"
    assert data[0]["sentiment"] == "😀"
    assert data[0]["power"] == "high"
    assert data[0]["interest"] == "high"
    assert data[0]["approach"] == "monitor closely"


    # We send a request to the API to update the first stakeholder.

    form_data = {
        "id": "1",
        "name": "updated",
        "role": "updated",
        "sentiment": "updated",
        "power": "updated",
        "interest": "updated",
    }

    response = api_client.post(UPDATE_STAKEHOLDER, data=form_data)
    data = response.data.decode()

    assert response.status_code == 200
    assert data == "Success"


    # We send a request to the API to show the first stakeholder.
    # We expect the response to include our previous updates.

    response = api_client.get("{}?id=1".format(SHOW_STAKEHOLDERS))
    data = json.loads(response.data.decode())

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert len(data) == 1

    assert data[0]["id"] == 1
    assert data[0]["name"] == "updated"
    assert data[0]["role"] == "updated"
    assert data[0]["sentiment"] == "updated"
    assert data[0]["power"] == "updated"
    assert data[0]["interest"] == "updated"
    assert data[0]["approach"] == "unknown"


    # We send a request to the API to delete the first stakeholder.

    form_data = {
        "id": "1"
    }

    response = api_client.post(DELETE_STAKEHOLDER, data=form_data)
    data = response.data.decode()

    assert response.status_code == 200
    assert data == "Success"


    # We send a request to the API to delete the second stakeholder.

    form_data = {
        "id": "2"
    }

    response = api_client.post(DELETE_STAKEHOLDER, data=form_data)
    data = response.data.decode()

    assert response.status_code == 200
    assert data == "Success"


    # We send a request to the API to show all stakeholders.
    # We expect the response to contain zero stakeholders.

    response = api_client.get(SHOW_STAKEHOLDERS)
    data = json.loads(response.data.decode())

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert len(data) == 0


# We test all of the deliverable-related endpoints.
#
# In an ideal world, we would split this single function into multiples ones.
#
# This would require us either to save state between tests or to create
# a large number of text fixtures, neither of which we want to do.

def test_deliverables_endpoints(api_client):
    # We send a request to the API to show all deliverables.
    # We expect the response to contain zero deliverables.

    response = api_client.get(SHOW_DELIVERABLES)
    data = json.loads(response.data.decode())

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert len(data) == 0


    # We send a request to the API to add a deliverable.

    form_data = {
        "name": "deliverable #1",
        "kind": "interactive",
        "medium": "in-person meeting",
        "formality": "formal",
        "frequency": "daily"
    }

    response = api_client.post(ADD_DELIVERABLE, data=form_data)
    data = response.data.decode()

    assert response.status_code == 200
    assert data == "Success"


    # We send a request to the API to add a second deliverable.

    form_data = {
        "name": "deliverable #2",
        "kind": "push",
        "medium": "video/teleconference",
        "formality": "casual",
        "frequency": "weekly"
    }

    response = api_client.post(ADD_DELIVERABLE, data=form_data)
    data = response.data.decode()

    assert response.status_code == 200
    assert data == "Success"


    # We send a request to the API to show all deliverables.
    # We expect the response to contain both deliverables.

    response = api_client.get(SHOW_DELIVERABLES)
    data = json.loads(response.data.decode())

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert len(data) == 2

    assert data[0]["id"] == 1
    assert data[0]["name"] == "deliverable #1"
    assert data[0]["kind"] == "interactive"
    assert data[0]["medium"] == "in-person meeting"
    assert data[0]["formality"] == "formal"
    assert data[0]["frequency"] == "daily"

    assert data[1]["id"] == 2
    assert data[1]["name"] == "deliverable #2"
    assert data[1]["kind"] == "push"
    assert data[1]["medium"] == "video/teleconference"
    assert data[1]["formality"] == "casual"
    assert data[1]["frequency"] == "weekly"


    # We send a request to the API to show the first deliverable.
    # We expect the response to contain only that deliverable.

    response = api_client.get("{}?id=1".format(SHOW_DELIVERABLES))
    data = json.loads(response.data.decode())

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert len(data) == 1

    assert data[0]["id"] == 1
    assert data[0]["name"] == "deliverable #1"
    assert data[0]["kind"] == "interactive"
    assert data[0]["medium"] == "in-person meeting"
    assert data[0]["formality"] == "formal"
    assert data[0]["frequency"] == "daily"


    # We send a request to the API to update the first deliverable.

    form_data = {
        "id": "1",
        "name": "updated",
        "kind": "updated",
        "medium": "updated",
        "formality": "updated",
        "frequency": "updated",
    }

    response = api_client.post(UPDATE_DELIVERABLE, data=form_data)
    data = response.data.decode()

    assert response.status_code == 200
    assert data == "Success"


    # We send a request to the API to show the first deliverable.
    # We expect the response to include our previous updates.

    response = api_client.get("{}?id=1".format(SHOW_DELIVERABLES))
    data = json.loads(response.data.decode())

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert len(data) == 1

    assert data[0]["id"] == 1
    assert data[0]["name"] == "updated"
    assert data[0]["kind"] == "updated"
    assert data[0]["medium"] == "updated"
    assert data[0]["formality"] == "updated"
    assert data[0]["frequency"] == "updated"


    # We send a request to the API to delete the first deliverable.

    form_data = {
        "id": "1"
    }

    response = api_client.post(DELETE_DELIVERABLE, data=form_data)
    data = response.data.decode()

    assert response.status_code == 200
    assert data == "Success"


    # We send a request to the API to delete the second deliverable.

    form_data = {
        "id": "2"
    }

    response = api_client.post(DELETE_DELIVERABLE, data=form_data)
    data = response.data.decode()

    assert response.status_code == 200
    assert data == "Success"


    # We send a request to the API to show all deliverables.
    # We expect the response to contain zero deliverables.

    response = api_client.get(SHOW_DELIVERABLES)
    data = json.loads(response.data.decode())

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert len(data) == 0


# We test all of the association-related endpoints.
#
# In an ideal world, we would split this single function into multiples ones.
#
# This would require us either to save state between tests or to create
# a large number of text fixtures, neither of which we want to do.

def test_associations_endpoints(api_client):
    # We send a request to the API to add a stakeholder.
    # This is part of test setup.

    form_data = {
        "name": "stakeholder #1",
        "role": "project sponsor",
        "sentiment": "😀",
        "power": "high",
        "interest": "high"
    }

    response = api_client.post(ADD_STAKEHOLDER, data=form_data)
    data = response.data.decode()

    assert response.status_code == 200
    assert data == "Success"


    # We send a request to the API to add a second stakeholder.
    # This is part of test setup.

    form_data = {
        "name": "stakeholder #2",
        "role": "customer",
        "sentiment": "😐",
        "power": "high",
        "interest": "low"
    }

    response = api_client.post(ADD_STAKEHOLDER, data=form_data)
    data = response.data.decode()

    assert response.status_code == 200
    assert data == "Success"


    # We send a request to the API to add a deliverable.
    # This is part of test setup.

    form_data = {
        "name": "deliverable #1",
        "kind": "interactive",
        "medium": "in-person meeting",
        "formality": "formal",
        "frequency": "daily"
    }

    response = api_client.post(ADD_DELIVERABLE, data=form_data)
    data = response.data.decode()

    assert response.status_code == 200
    assert data == "Success"


    # We send a request to the API to add a second deliverable.
    # This is part of test setup.

    form_data = {
        "name": "deliverable #2",
        "kind": "push",
        "medium": "video/teleconference",
        "formality": "casual",
        "frequency": "weekly"
    }

    response = api_client.post(ADD_DELIVERABLE, data=form_data)
    data = response.data.decode()

    assert response.status_code == 200
    assert data == "Success"


    # We send a request to the API to show all associations.
    # We expect the response to contain zero associations.

    response = api_client.get(SHOW_ASSOCIATIONS)
    data = json.loads(response.data.decode())

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert len(data) == 0


    # We send a request to the API to add an association.

    form_data = {
        "stakeholder_id": "1",
        "deliverable_id": "1"
    }

    response = api_client.post(ADD_ASSOCIATION, data=form_data)
    data = response.data.decode()

    assert response.status_code == 200
    assert data == "Success"


    # We send a request to the API to add a second association.

    form_data = {
        "stakeholder_id": "2",
        "deliverable_id": "2"
    }

    response = api_client.post(ADD_ASSOCIATION, data=form_data)
    data = response.data.decode()

    assert response.status_code == 200
    assert data == "Success"


    # We send a request to the API to show all associations.
    # We expect the response to contain both associations.

    response = api_client.get(SHOW_ASSOCIATIONS)
    data = json.loads(response.data.decode())

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert len(data) == 2

    assert data[0]["id"] == 1
    assert data[0]["stakeholder_id"] == 1
    assert data[0]["stakeholder_name"] == "stakeholder #1"
    assert data[0]["stakeholder_approach"] == "monitor closely"
    assert data[0]["deliverable_id"] == 1
    assert data[0]["deliverable_name"] == "deliverable #1"

    assert data[1]["id"] == 2
    assert data[1]["stakeholder_id"] == 2
    assert data[1]["stakeholder_name"] == "stakeholder #2"
    assert data[1]["stakeholder_approach"] == "keep satisfied"
    assert data[1]["deliverable_id"] == 2
    assert data[1]["deliverable_name"] == "deliverable #2"


    # We send a request to the API to show the first association.
    # We expect the response to contain only that association.

    response = api_client.get("{}?id=1".format(SHOW_ASSOCIATIONS))
    data = json.loads(response.data.decode())

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert len(data) == 1

    assert data[0]["id"] == 1
    assert data[0]["stakeholder_id"] == 1
    assert data[0]["stakeholder_name"] == "stakeholder #1"
    assert data[0]["stakeholder_approach"] == "monitor closely"
    assert data[0]["deliverable_id"] == 1
    assert data[0]["deliverable_name"] == "deliverable #1"


    # We send a request to the API to update the first association.

    form_data = {
        "id": "1",
        "stakeholder_id": "1",
        "deliverable_id": "2"
    }

    response = api_client.post(UPDATE_ASSOCIATION, data=form_data)
    data = response.data.decode()

    assert response.status_code == 200
    assert data == "Success"


    # We send a request to the API to show the first association.
    # We expect the response to include our previous updates.

    response = api_client.get("{}?id=1".format(SHOW_ASSOCIATIONS))
    data = json.loads(response.data.decode())

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert len(data) == 1

    assert data[0]["id"] == 1
    assert data[0]["stakeholder_id"] == 1
    assert data[0]["stakeholder_name"] == "stakeholder #1"
    assert data[0]["stakeholder_approach"] == "monitor closely"
    assert data[0]["deliverable_id"] == 2
    assert data[0]["deliverable_name"] == "deliverable #2"


    # We send a request to the API to delete the first association.

    form_data = {
        "id": "1"
    }

    response = api_client.post(DELETE_ASSOCIATION, data=form_data)
    data = response.data.decode()

    assert response.status_code == 200
    assert data == "Success"


    # We send a request to the API to delete the second association.

    form_data = {
        "id": "2"
    }

    response = api_client.post(DELETE_ASSOCIATION, data=form_data)
    data = response.data.decode()

    assert response.status_code == 200
    assert data == "Success"


    # We send a request to the API to show all associations.
    # We expect the response to contain zero associations.

    response = api_client.get(SHOW_ASSOCIATIONS)
    data = json.loads(response.data.decode())

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert len(data) == 0


# We test the management-plan-related endpoint.
#
# In an ideal world, we would split this single function into multiples ones.
#
# This would require us either to save state between tests or to create
# a large number of text fixtures, neither of which we want to do.

def test_management_plan_endpoint(api_client):
    # We send a request to the API to add a stakeholder.
    # This is part of test setup.

    form_data = {
        "name": "stakeholder #1",
        "role": "project sponsor",
        "sentiment": "😀",
        "power": "high",
        "interest": "high"
    }

    response = api_client.post(ADD_STAKEHOLDER, data=form_data)
    data = response.data.decode()

    assert response.status_code == 200
    assert data == "Success"


    # We send a request to the API to add a second stakeholder.
    # This is part of test setup.

    form_data = {
        "name": "stakeholder #2",
        "role": "customer",
        "sentiment": "😐",
        "power": "high",
        "interest": "low"
    }

    response = api_client.post(ADD_STAKEHOLDER, data=form_data)
    data = response.data.decode()

    assert response.status_code == 200
    assert data == "Success"


    # We send a request to the API to add a deliverable.
    # This is part of test setup.

    form_data = {
        "name": "deliverable #1",
        "kind": "interactive",
        "medium": "in-person meeting",
        "formality": "formal",
        "frequency": "daily"
    }

    response = api_client.post(ADD_DELIVERABLE, data=form_data)
    data = response.data.decode()

    assert response.status_code == 200
    assert data == "Success"


    # We send a request to the API to add a second deliverable.
    # This is part of test setup.

    form_data = {
        "name": "deliverable #2",
        "kind": "push",
        "medium": "video/teleconference",
        "formality": "casual",
        "frequency": "weekly"
    }

    response = api_client.post(ADD_DELIVERABLE, data=form_data)
    data = response.data.decode()

    assert response.status_code == 200
    assert data == "Success"


    # We send a request to the API to add an association.
    # This is part of test setup.

    form_data = {
        "stakeholder_id": "1",
        "deliverable_id": "1"
    }

    response = api_client.post(ADD_ASSOCIATION, data=form_data)
    data = response.data.decode()

    assert response.status_code == 200
    assert data == "Success"


    # We send a request to the API to add a second association.
    # This is part of test setup.

    form_data = {
        "stakeholder_id": "2",
        "deliverable_id": "2"
    }

    response = api_client.post(ADD_ASSOCIATION, data=form_data)
    data = response.data.decode()

    assert response.status_code == 200
    assert data == "Success"


    # We send a request to the API to show the management plan.
    # We expect the response to contain a mapped, reduced, and sorted
    # set of associations between stakeholders and deliverables.

    response = api_client.get(SHOW_MANAGEMENT_PLAN)
    data = json.loads(response.data.decode(), object_pairs_hook=collections.OrderedDict)

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert len(data) == 5

    assert data == collections.OrderedDict({
        "monitor closely": {
            "1": {
                "name": "stakeholder #1",
                "1": {
                    "name": "deliverable #1",
                }
            },
        },
        "keep satisfied": {
            "2": {
                "name": "stakeholder #2",
                "2": {
                   "name": "deliverable #2"
               }
            }
        },
        "keep informed": {},
        "monitor": {},
        "unknown": {}
    })


    # We send a request to the API to delete the first association.

    form_data = {
        "id": "1"
    }

    response = api_client.post(DELETE_ASSOCIATION, data=form_data)
    data = response.data.decode()

    assert response.status_code == 200
    assert data == "Success"


    # We send a request to the API to delete the second association.

    form_data = {
        "id": "2"
    }

    response = api_client.post(DELETE_ASSOCIATION, data=form_data)
    data = response.data.decode()

    assert response.status_code == 200
    assert data == "Success"


    # We send a request to the API to show the management plan.
    # We expect the response to contain a dict with five keys but no values.

    response = api_client.get(SHOW_MANAGEMENT_PLAN)
    data = json.loads(response.data.decode(), object_pairs_hook=collections.OrderedDict)

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert len(data) == 5

    assert data == collections.OrderedDict({
        "monitor closely": {},
        "keep satisfied": {},
        "keep informed": {},
        "monitor": {},
        "unknown": {}
    })
