import pytest


BASE = "http://localhost:8080"
INDEX = "{}/".format(BASE)


# These tests use the same database, so they share state.

@pytest.mark.browser()
def test_use_navbar(browser):
    # Navigate to '/'.

    browser.get(INDEX)


    # Find and click 'li', a drop-down menu.

    browser.find_element_by_id("stakeholders").click()


    # Find and click `a`, navigating to `/stakeholders`.

    browser.find_element_by_css_selector("[href='/stakeholders']").click()


    # Find and click `li`, navigating back to '/'.

    browser.find_element_by_id("home").click()


    # Find and click 'li', a drop-down menu.

    browser.find_element_by_id("stakeholders").click()


    # Find and click `a`, navigating to `/stakeholders/add`.

    browser.find_element_by_css_selector("[href='/stakeholders/add']").click()


    # Find and click `li`, navigating back to '/'.

    browser.find_element_by_id("home").click()


    # Find and click 'li', a drop-down menu.

    browser.find_element_by_id("deliverables").click()


    # Find and click `a`, navigating to `/deliverables`.

    browser.find_element_by_css_selector("[href='/deliverables']").click()


    # Find and click `li`, navigating back to '/'.

    browser.find_element_by_id("home").click()


    # Find and click 'li', a drop-down menu.

    browser.find_element_by_id("deliverables").click()


    # Find and click `a`, navigating to `/deliverables/add`.

    browser.find_element_by_css_selector("[href='/deliverables/add']").click()


    # Find and click `li`, navigating back to '/'.

    browser.find_element_by_id("home").click()


    # Find and click 'li', a drop-down menu.

    browser.find_element_by_id("associations").click()


    # Find and click `a`, navigating to `/associations`.

    browser.find_element_by_css_selector("[href='/associations']").click()


    # Find and click `li`, navigating back to '/'.

    browser.find_element_by_id("home").click()


    # Find and click 'li', a drop-down menu.

    browser.find_element_by_id("associations").click()


    # Find and click `a`, navigating to `/associations/add`.

    browser.find_element_by_css_selector("[href='/associations/add']").click()


    # Find and click `li`, navigating back to '/'.

    browser.find_element_by_id("home").click()


    # Find and click 'li', navigating to `/management-plan`.

    browser.find_element_by_id("management-plan").click()


    # Find and click `li`, navigating back to '/'.

    browser.find_element_by_id("home").click()


@pytest.mark.browser()
def test_visit_index(browser):
    # Navigate to '/'.

    browser.get(INDEX)


@pytest.mark.browser()
def test_add_stakeholder_one(browser):
    # Navigate to `/`.

    browser.get(INDEX)


    # Find and click 'li', a drop-down menu.

    browser.find_element_by_id("stakeholders").click()


    # Find and click `a`, navigating to `/stakeholders/add`.

    browser.find_element_by_css_selector("[href='/stakeholders/add']").click()


    # Find and use each `input` form control.

    browser.find_element_by_id("name").send_keys("stakeholder #1")

    browser.find_element_by_id("role").send_keys("project sponsor")


    # Find and use each `select` form control (via `option`).
    # First, click every `option`.
    # Then, click particular ones (happy, high power, high interest).

    options = browser.find_elements_by_tag_name("option")

    for option in options:
        option.click()

    options[0].click()
    options[3].click()
    options[5].click()


    # Find and use the `button` form control, adding a stakeholder
    # and navigating to `/stakeholders`.

    browser.find_element_by_css_selector("[type='submit']").click()


@pytest.mark.browser()
def test_add_stakeholder_two(browser):
    # Navigate to `/`.

    browser.get(INDEX)


    # Find and click 'li', a drop-down menu.

    browser.find_element_by_id("stakeholders").click()


    # Find and click `a`, navigating to `/stakeholders/add`.

    browser.find_element_by_css_selector("[href='/stakeholders/add']").click()


    # Find and use each `input` form control.

    browser.find_element_by_id("name").send_keys("stakeholder #2")

    browser.find_element_by_id("role").send_keys("customer")


    # Find and use each `select` form control (via `option`).
    # First, click every `option`.
    # Then, click particular ones (neutral, high power, low interest).

    options = browser.find_elements_by_tag_name("option")

    for option in options:
        option.click()

    options[1].click()
    options[3].click()
    options[6].click()


    # Find and use the `button` form control, adding a stakeholder
    # and navigating to `/stakeholders`.

    browser.find_element_by_css_selector("[type='submit']").click()


@pytest.mark.browser()
def test_add_stakeholder_three(browser):
    # Navigate to `/`.

    browser.get(INDEX)


    # Find and click 'li', a drop-down menu.

    browser.find_element_by_id("stakeholders").click()


    # Find and click `a`, navigating to `/stakeholders/add`.

    browser.find_element_by_css_selector("[href='/stakeholders/add']").click()


    # Find and use each `input` form control.

    browser.find_element_by_id("name").send_keys("stakeholder #3")

    browser.find_element_by_id("role").send_keys("end-user")


    # Find and use each `select` form control (via `option`).
    # First, click every `option`.
    # Then, click particular ones (unhappy, low power, high interest).

    options = browser.find_elements_by_tag_name("option")

    for option in options:
        option.click()

    options[2].click()
    options[4].click()
    options[5].click()


    # Find and use the `button` form control, adding a stakeholder
    # and navigating to `/stakeholders`.

    browser.find_element_by_css_selector("[type='submit']").click()


@pytest.mark.browser()
def test_add_stakeholder_four(browser):
    # Navigate to `/`.

    browser.get(INDEX)


    # Find and click 'li', a drop-down menu.

    browser.find_element_by_id("stakeholders").click()


    # Find and click `a`, navigating to `/stakeholders/add`.

    browser.find_element_by_css_selector("[href='/stakeholders/add']").click()


    # Find and use each `input` form control.

    browser.find_element_by_id("name").send_keys("stakeholder #4")

    browser.find_element_by_id("role").send_keys("general public")


    # Find and use each `select` form control (via `option`).
    # First, click every `option`.
    # Then, click particular ones (happy, low power, low interest).

    options = browser.find_elements_by_tag_name("option")

    for option in options:
        option.click()

    options[0].click()
    options[4].click()
    options[6].click()


    # Find and use the `button` form control, adding a stakeholder
    # and navigating to `/stakeholders`.

    browser.find_element_by_css_selector("[type='submit']").click()


@pytest.mark.browser()
def test_add_deliverable(browser):
    # Navigate to `/`.

    browser.get(INDEX)


    # Find and click 'li', a drop-down menu.

    browser.find_element_by_id("deliverables").click()


    # Find and click `a`, navigating to `/deliverables/add`.

    browser.find_element_by_css_selector("[href='/deliverables/add']").click()


    # Find and use the `input` form control.

    browser.find_element_by_id("name").send_keys("deliverable #1")


    # Find and use each `select` form control (via `option`).
    # First, click every `option`.
    # Then, click particular ones (push, in-person meeting, formal, daily).

    options = browser.find_elements_by_tag_name("option")

    for option in options:
        option.click()

    options[0].click()
    options[3].click()
    options[10].click()
    options[12].click()


    # Find and use the `button` form control, adding a deliverable
    # and navigating to `/deliverables`.

    browser.find_element_by_css_selector("[type='submit']").click()


@pytest.mark.browser()
def test_add_association_one(browser):
    # Navigate to `/`.

    browser.get(INDEX)


    # Find and click 'li', a drop-down menu.

    browser.find_element_by_id("associations").click()


    # Find and click `a`, navigating to `/associations/add`.

    browser.find_element_by_css_selector("[href='/associations/add']").click()


    # Find and use each `select` form control (via `option`).
    # First, click every `option`.
    # Then, click particular ones (stakeholder #1, deliverable #1).

    options = browser.find_elements_by_tag_name("option")

    for option in options:
        option.click()

    options[0].click()
    options[4].click()


    # Find and use the `button` form control, adding an association
    # and navigating to `/deliverables`.

    browser.find_element_by_css_selector("[type='submit']").click()


@pytest.mark.browser()
def test_add_association_two(browser):
    # Navigate to `/`.

    browser.get(INDEX)


    # Find and click 'li', a drop-down menu.

    browser.find_element_by_id("associations").click()


    # Find and click `a`, navigating to `/associations/add`.

    browser.find_element_by_css_selector("[href='/associations/add']").click()


    # Find and use each `select` form control (via `option`).
    # First, click every `option`.
    # Then, click particular ones (stakeholder #2, deliverable #1).

    options = browser.find_elements_by_tag_name("option")

    for option in options:
        option.click()

    options[1].click()
    options[4].click()


    # Find and use the `button` form control, adding an association
    # and navigating to `/deliverables`.

    browser.find_element_by_css_selector("[type='submit']").click()


@pytest.mark.browser()
def test_add_association_three(browser):
    # Navigate to `/`.

    browser.get(INDEX)


    # Find and click 'li', a drop-down menu.

    browser.find_element_by_id("associations").click()


    # Find and click `a`, navigating to `/associations/add`.

    browser.find_element_by_css_selector("[href='/associations/add']").click()


    # Find and use each `select` form control (via `option`).
    # First, click every `option`.
    # Then, click particular ones (stakeholder #3, deliverable #1).

    options = browser.find_elements_by_tag_name("option")

    for option in options:
        option.click()

    options[2].click()
    options[4].click()


    # Find and use the `button` form control, adding an association
    # and navigating to `/deliverables`.

    browser.find_element_by_css_selector("[type='submit']").click()


@pytest.mark.browser()
def test_add_association_four(browser):
    # Navigate to `/`.

    browser.get(INDEX)


    # Find and click 'li', a drop-down menu.

    browser.find_element_by_id("associations").click()


    # Find and click `a`, navigating to `/associations/add`.

    browser.find_element_by_css_selector("[href='/associations/add']").click()


    # Find and use each `select` form control (via `option`).
    # First, click every `option`.
    # Then, click particular ones (stakeholder #4, deliverable #1).

    options = browser.find_elements_by_tag_name("option")

    for option in options:
        option.click()

    options[3].click()
    options[4].click()


    # Find and use the `button` form control, adding an association
    # and navigating to `/deliverables`.

    browser.find_element_by_css_selector("[type='submit']").click()


@pytest.mark.browser()
def test_visit_management_plan(browser):
    # Navigate to '/'.

    browser.get(INDEX)


    # Find and click 'li', navigating to `/management-plan`.

    browser.find_element_by_id("management-plan").click()


@pytest.mark.browser()
def test_follow_links_in_association(browser):
    # Navigate to `/`.

    browser.get(INDEX)


    # Find and click 'li', a drop-down menu.

    browser.find_element_by_id("associations").click()


    # Find and click `a`, navigating to `/associations`.

    browser.find_element_by_css_selector("[href='/associations']").click()


    # Find and click `a`, navigating to /stakeholders?id=1`.

    browser.find_elements_by_css_selector("[href='/stakeholders?id=1']")[0]\
           .click()


    # Find and click 'li', a drop-down menu.

    browser.find_element_by_id("associations").click()


    # Find and click `a`, navigating to `/associations`.

    browser.find_element_by_css_selector("[href='/associations']").click()


    # Find and click `a`, navigating to /deliverables?id=1`.

    browser.find_elements_by_css_selector("[href='/deliverables?id=1']")[0]\
           .click()


@pytest.mark.browser()
def test_follow_links_in_management_plan(browser):
    # Navigate to `/`.

    browser.get(INDEX)


    # Find and click 'li', navigating to `/management-plan`.

    browser.find_element_by_id("management-plan").click()


    # Find and click `a`, navigating to /stakeholders?id=1`.

    browser.find_elements_by_css_selector("[href='/stakeholders?id=1']")[0]\
           .click()


    # Find and click 'li', navigating to `/management-plan`.

    browser.find_element_by_id("management-plan").click()


    # Find and click `a`, navigating to /deliverables?id=1`.

    browser.find_elements_by_css_selector("[href='/deliverables?id=1']")[0]\
           .click()


@pytest.mark.browser()
def test_update_stakeholder_one(browser):
    # Navigate to `/`.

    browser.get(INDEX)


    # Find and click 'li', a drop-down menu.

    browser.find_element_by_id("stakeholders").click()


    # Find and click `a`, navigating to `/stakeholders`.

    browser.find_element_by_css_selector("[href='/stakeholders']").click()


    # Find and use `button`, navigating to `/stakeholders/update?id=1`.

    browser.find_element_by_id("update-stakeholder-1")\
           .find_element_by_css_selector("[type='submit']")\
           .click()


    # Find and use each `input` form control.

    browser.find_element_by_id("name").send_keys("updated")

    browser.find_element_by_id("role").send_keys("updated")


    # Find and use each `select` form control (via `option`).
    # First, click every `option`.
    # Then, click particular ones (neutral, low power, low interest).

    options = browser.find_elements_by_tag_name("option")

    for option in options:
        option.click()

    options[1].click()
    options[4].click()
    options[6].click()


    # Find and use the `button` form control, updating a stakeholder
    # and navigating to `/stakeholders`.

    browser.find_element_by_css_selector("[type='submit']").click()


@pytest.mark.browser()
def test_update_deliverable(browser):
    # Navigate to `/`.

    browser.get(INDEX)


    # Find and click 'li', a drop-down menu.

    browser.find_element_by_id("deliverables").click()


    # Find and click `a`, navigating to `/deliverables`.

    browser.find_element_by_css_selector("[href='/deliverables']").click()


    # Find and use `button`, navigating to `/deliverables/update?id=1`.

    browser.find_element_by_id("update-deliverable-1")\
           .find_element_by_css_selector("[type='submit']")\
           .click()


    # Find and use the `input` form control.

    browser.find_element_by_id("name").send_keys("updated")


    # Find and use each `select` form control (via `option`).
    # First, click every `option`.
    # Then, click particular ones (pull, videoteleconference, casual, weekly).

    options = browser.find_elements_by_tag_name("option")

    for option in options:
        option.click()

    options[1].click()
    options[4].click()
    options[11].click()
    options[13].click()


    # Find and use the `button` form control, updating a deliverable
    # and navigating to `/deliverables`.

    browser.find_element_by_css_selector("[type='submit']").click()


@pytest.mark.browser()
def test_update_association_one(browser):
    # Navigate to `/`.

    browser.get(INDEX)


    # Find and click 'li', a drop-down menu.

    browser.find_element_by_id("associations").click()


    # Find and click `a`, navigating to `/associations`.

    browser.find_element_by_css_selector("[href='/associations']").click()


    # Find and use `button`, navigating to `/associations/update?id=1`.

    browser.find_element_by_id("update-association-1")\
           .find_element_by_css_selector("[type='submit']")\
           .click()


    # Find and use each `select` form control (via `option`).
    # First, click every `option`.
    # Then, click particular ones (stakeholder #2, deliverable #1).

    options = browser.find_elements_by_tag_name("option")

    for option in options:
        option.click()

    options[1].click()
    options[4].click()


    # Find and use the `button` form control, updating a deliverable
    # and navigating to `/deliverables`.

    browser.find_element_by_css_selector("[type='submit']").click()


@pytest.mark.browser()
def test_delete_association_one(browser):
    # Navigate to `/`.

    browser.get(INDEX)


    # Find and click 'li', a drop-down menu.

    browser.find_element_by_id("associations").click()


    # Find and click `a`, navigating to `/associations`.

    browser.find_element_by_css_selector("[href='/associations']").click()


    # Find and use `button`, deleting an association.

    browser.find_element_by_id("delete-association-1")\
           .find_element_by_css_selector("[type='submit']")\
           .click()


@pytest.mark.browser()
def test_delete_association_two(browser):
    # Navigate to `/`.

    browser.get(INDEX)


    # Find and click 'li', a drop-down menu.

    browser.find_element_by_id("associations").click()


    # Find and click `a`, navigating to `/associations`.

    browser.find_element_by_css_selector("[href='/associations']").click()


    # Find and use `button`, deleting an association.

    browser.find_element_by_id("delete-association-2")\
           .find_element_by_css_selector("[type='submit']")\
           .click()


@pytest.mark.browser()
def test_delete_association_three(browser):
    # Navigate to `/`.

    browser.get(INDEX)


    # Find and click 'li', a drop-down menu.

    browser.find_element_by_id("associations").click()


    # Find and click `a`, navigating to `/associations`.

    browser.find_element_by_css_selector("[href='/associations']").click()


    # Find and use `button`, deleting an association.

    browser.find_element_by_id("delete-association-3")\
           .find_element_by_css_selector("[type='submit']")\
           .click()


@pytest.mark.browser()
def test_delete_association_four(browser):
    # Navigate to `/`.

    browser.get(INDEX)


    # Find and click 'li', a drop-down menu.

    browser.find_element_by_id("associations").click()


    # Find and click `a`, navigating to `/associations`.

    browser.find_element_by_css_selector("[href='/associations']").click()


    # Find and use `button`, deleting an association.

    browser.find_element_by_id("delete-association-4")\
           .find_element_by_css_selector("[type='submit']")\
           .click()


@pytest.mark.browser()
def test_delete_deliverable(browser):
    # Navigate to `/`.

    browser.get(INDEX)


    # Find and click 'li', a drop-down menu.

    browser.find_element_by_id("deliverables").click()


    # Find and click `a`, navigating to `/deliverables`.

    browser.find_element_by_css_selector("[href='/deliverables']").click()


    # Find and use `button`, deleting a deliverable.

    browser.find_element_by_id("delete-deliverable-1")\
           .find_element_by_css_selector("[type='submit']")\
           .click()


@pytest.mark.browser()
def test_delete_stakeholder_one(browser):
    # Navigate to `/`.

    browser.get(INDEX)


    # Find and click 'li', a drop-down menu.

    browser.find_element_by_id("stakeholders").click()


    # Find and click `a`, navigating to `/stakeholders`.

    browser.find_element_by_css_selector("[href='/stakeholders']").click()


    # Find and use `button`, deleting a stakeholder.

    browser.find_element_by_id("delete-stakeholder-1")\
           .find_element_by_css_selector("[type='submit']")\
           .click()


@pytest.mark.browser()
def test_delete_stakeholder_two(browser):
    # Navigate to `/`.

    browser.get(INDEX)


    # Find and click 'li', a drop-down menu.

    browser.find_element_by_id("stakeholders").click()


    # Find and click `a`, navigating to `/stakeholders`.

    browser.find_element_by_css_selector("[href='/stakeholders']").click()


    # Find and use `button`, deleting a stakeholder.

    browser.find_element_by_id("delete-stakeholder-2")\
           .find_element_by_css_selector("[type='submit']")\
           .click()


@pytest.mark.browser()
def test_delete_stakeholder_three(browser):
    # Navigate to `/`.

    browser.get(INDEX)


    # Find and click 'li', a drop-down menu.

    browser.find_element_by_id("stakeholders").click()


    # Find and click `a`, navigating to `/stakeholders`.

    browser.find_element_by_css_selector("[href='/stakeholders']").click()


    # Find and use `button`, deleting a stakeholder.

    browser.find_element_by_id("delete-stakeholder-3")\
           .find_element_by_css_selector("[type='submit']")\
           .click()


@pytest.mark.browser()
def test_delete_stakeholder_four(browser):
    # Navigate to `/`.

    browser.get(INDEX)


    # Find and click 'li', a drop-down menu.

    browser.find_element_by_id("stakeholders").click()


    # Find and click `a`, navigating to `/stakeholders`.

    browser.find_element_by_css_selector("[href='/stakeholders']").click()


    # Find and use `button`, deleting a stakeholder.

    browser.find_element_by_id("delete-stakeholder-4")\
           .find_element_by_css_selector("[type='submit']")\
           .click()
