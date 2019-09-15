"""
This module contains the app and app factory.
"""


import flask
import requests


def create_app(requester=requests, host="localhost", port="8079"):
    """
    This is the app factory.  It returns an instance of the app.

    The app is the intermediary between the API and the end-user's
    web browser.

    Parameters
    ----------
    requester : Python library 
        The library used to send requests to the API
        (`requests` for production and `flask.testing.FlaskClient`
        for testing).

        We need this contrivance only so we can use
        Flask's `testing` module for unit testing.
 
    host : str
        The name of the host on which the API runs
        (`localhost` by default).

        The app sends requests to the API's endpoints,
        and this forms part of the base URI.

    port : str
        The port on which the API listens
        (`8079` by default).

        The app sends requests to the API's endpoints,
        and this forms part of the base URI.

    Returns
    -------
    app : Flask application object
        An instance of the app as a Flask application object.
    """

    API = "http://{}:{}".format(host, port)

    ADD_STAKEHOLDER = "{}/api/v1/stakeholders/add".format(API)
    DELETE_STAKEHOLDER = "{}/api/v1/stakeholders/delete".format(API)
    SHOW_STAKEHOLDERS = "{}/api/v1/stakeholders/show".format(API)
    UPDATE_STAKEHOLDER = "{}/api/v1/stakeholders/update".format(API)

    ADD_DELIVERABLE = "{}/api/v1/deliverables/add".format(API)
    DELETE_DELIVERABLE = "{}/api/v1/deliverables/delete".format(API)
    SHOW_DELIVERABLES = "{}/api/v1/deliverables/show".format(API)
    UPDATE_DELIVERABLE = "{}/api/v1/deliverables/update".format(API)

    ADD_ASSOCIATION = "{}/api/v1/associations/add".format(API)
    DELETE_ASSOCIATION = "{}/api/v1/associations/delete".format(API)
    SHOW_ASSOCIATIONS = "{}/api/v1/associations/show".format(API)
    UPDATE_ASSOCIATION = "{}/api/v1/associations/update".format(API)

    SHOW_MANAGEMENT_PLAN = "{}/api/v1/management-plan/show".format(API)


    app = flask.Flask(__name__)


    @app.route("/")
    @app.route("/home")
    @app.route("/index")
    def index():
        """
        This is the endpoint for the index.

        It accepts a `GET` request.  It returns HTML.
        """

        return flask.render_template("index.html")


    @app.route("/stakeholders")
    def show_stakeholders():
        """
        This is the endpoint for showing stakeholders.

        It accepts a `GET` request.  It returns HTML.
        """

        # If it exists, then we attempt to obtain the value of the `id`
        # query parameter.

        id = flask.request.args.get("id")

        # If there is no `id`, then we request all stakeholders
        # from the API.
        #
        # Otherwise, we request a single stakeholder from the
        # API.

        if id is None:
            response = requester.get(SHOW_STAKEHOLDERS)

        else:
            response = requester.get(
                "{}?id={}".format(SHOW_STAKEHOLDERS, id)
            )

        # We return `show-stakeholders.html`. 

        return flask.render_template(
            "show-stakeholders.html", 
            data=response.json()
        )


    @app.route("/stakeholders/add", methods=["GET", "POST"])
    def add_stakeholder():
        """
        This is the endpoint for adding a stakeholder.

        It accepts a `GET` or a `POST` request.  It returns HTML.
        """

        # On receiving a `GET` request, we return
        # `add-stakeholder.html`, which contains a form for 
        # adding a stakeholder.

        if flask.request.method == "GET":
            return flask.render_template("add-stakeholder.html")

        # On receiving a `POST` request, we forward the
        # form data in the body of the request to the API.
        # This contains the end-user's request to add a stakeholder.
        #
        # We then redirect the end-user to `/stakeholders`.

        else:
            requester.post(
                ADD_STAKEHOLDER, 
                data=flask.request.form
            )

            return flask.redirect(
                flask.url_for("show_stakeholders")
            )


    @app.route("/stakeholders/delete", methods=["POST"])
    def delete_stakeholder():
        """
        This is the endpoint for deleting stakeholder.

        It accepts a `POST` request.  It returns HTML.
        """

        # On receiving a `POST` request, we forward the
        # form data in the body of the request to the API.
        # This contains the end-user's request to delete a stakeholder.

        requester.post(
            DELETE_STAKEHOLDER, 
            data=flask.request.form
        )

        # We redirect the end-user to `/stakeholders`.

        return flask.redirect(
            flask.url_for("show_stakeholders")
        )


    @app.route("/stakeholders/update", methods=["GET", "POST"])
    def update_stakeholder():
        """
        This is the endpoint for updating a stakeholder.

        It accepts a `GET` or a `POST` request.  It returns HTML.
        """

        # On receiving a `GET` request, we attempt to obtain the
        # value of the `id` query parameter.
        #
        # If there is no `id`, then we redirect the end-user to
        # `/stakeholders`.
        #
        # Otherwise, we request a single stakeholder from the
        # API.
        #
        # We then return `update-stakeholder.html`.

        if flask.request.method == "GET":
            id = flask.request.args.get("id")

            if id is None:
                return flask.redirect(
                    flask.url_for("show_stakeholders")
                )

            else:
                response = requester.get(
                    "{}?id={}".format(SHOW_STAKEHOLDERS, id)
                )

                return flask.render_template(
                    "update-stakeholder.html", 
                    data=response.json()
                )

        # On receiving a `POST` request, we forward the
        # form data in the body of the request to the API.
        # This contains the end-user's request to update a stakeholder.
        #
        # We then redirect the end-user to `/stakeholders`.

        else:
            requester.post(
                UPDATE_STAKEHOLDER, 
                data=flask.request.form
            )

            return flask.redirect(
                flask.url_for("show_stakeholders")
            )


    @app.route("/deliverables")
    def show_deliverables():
        """
        This is the endpoint for showing deliverables.

        It accepts a `GET` request.  It returns HTML.
        """

        # If it exists, then we attempt to obtain the value of the `id`
        # query parameter.

        id = flask.request.args.get("id")

        # If there is no `id`, then we request all deliverables
        # from the API.
        #
        # Otherwise, we request a single deliverable from the
        # API.

        if id is None:
            response = requester.get(SHOW_DELIVERABLES)

        else:
            response = requester.get(
                "{}?id={}".format(SHOW_DELIVERABLES, id)
            )

        # We return `show-deliverables.html`.

        return flask.render_template(
            "show-deliverables.html", 
            data=response.json()
        )


    @app.route("/deliverables/add", methods=["GET", "POST"])
    def add_deliverable():
        """
        This is the endpoint for adding a deliverable.

        It accepts a `GET` or a `POST` request.  It returns HTML.
        """

        # On receiving a `GET` request, we return
        # `add-deliverable.html`, which contains a form for 
        # adding a deliverable.

        if flask.request.method == "GET":
            return flask.render_template("add-deliverable.html")

        # On receiving a `POST` request, we forward the
        # form data in the body of the request to the API.
        # This contains the end-user's request to add a deliverable.
        #
        # We then redirect the end-user to `/deliverables`.

        else:
            requester.post(
                ADD_DELIVERABLE, 
                data=flask.request.form
            )

            return flask.redirect(
                flask.url_for("show_deliverables")
            )


    @app.route("/deliverables/delete", methods=["POST"])
    def delete_deliverable():
        """
        This is the endpoint for deleting a deliverable.

        It accepts a `POST` request.  It returns HTML.
        """

        # On receiving a `POST` request, we forward the
        # form data in the body of the request to the API.
        # This contains the end-user's request to delete a stakeholder.

        requester.post(
            DELETE_DELIVERABLE, 
            data=flask.request.form
        )

        # We redirect the end-user to `/deliverables`.

        return flask.redirect(
            flask.url_for("show_deliverables")
        )


    @app.route("/deliverables/update", methods=["GET", "POST"])
    def update_deliverable():
        """
        This is the endpoint for updating a deliverable.

        It accepts a `GET` or a `POST` request.  It returns HTML.
        """

        # On receiving a `GET` request, we attempt to obtain the
        # value of the `id` query parameter.
        #
        # If there is no `id`, then we redirect the end-user to
        # `/deliverables`.
        #
        # Otherwise, we request a single deliverable from the
        # API.
        #
        # We then return `update-deliverable.html`.

        if flask.request.method == "GET":
            id = flask.request.args.get("id")

            if id is None:
                return flask.redirect(
                    flask.url_for("show_deliverables")
                )

            else:
                response = requester.get(
                    "{}?id={}".format(SHOW_DELIVERABLES, id)
                )

                return flask.render_template(
                    "update-deliverable.html", 
                    data=response.json()
                )

        # On receiving a `POST` request, we forward the
        # form data in the body of the request to the API.
        # This contains the end-user's request to update a deliverable.
        #
        # We then redirect the end-user to `/deliverables`.

        else:
            requester.post(
                UPDATE_DELIVERABLE, 
                data=flask.request.form
            )

            return flask.redirect(
                flask.url_for("show_deliverables")
            )


    @app.route("/associations")
    def show_associations():
        """
        This is the endpoint for showing associations.

        It accepts a `GET` request.  It returns HTML.
        """

        # If it exists, then we attempt to obtain the value of the `id`
        # query parameter.

        id = flask.request.args.get("id")

        # If there is no `id`, then we request all associations
        # from the API.
        #
        # Otherwise, we request a single association from the
        # API.

        if id is None:
            response = requester.get(SHOW_ASSOCIATIONS)

        else:
            response = requester.get(
                "{}?id={}".format(SHOW_ASSOCIATIONS, id)
            )

        # We return `show-associations.html`.

        return flask.render_template(
            "show-associations.html", 
            data=response.json()
        )


    @app.route("/associations/add", methods=["GET", "POST"])
    def add_association():
        """
        This is the endpoint for adding an association.

        It accepts a `GET` or a `POST` request.  It returns HTML.
        """

        # On receiving a `GET` request, we request stakeholders
        # and deliverables from the API.
        #
        # We then return `add-association.html`.

        if flask.request.method == "GET":
            stakeholders = requester.get(SHOW_STAKEHOLDERS)
            deliverables = requester.get(SHOW_DELIVERABLES)

            responses = {
                "stakeholders": stakeholders.json(),
                "deliverables": deliverables.json(),
            }

            return flask.render_template(
                "add-association.html",
                data=responses
            )

        # On receiving a `POST` request, we forward the
        # form data in the body of the request to the API.
        # This contains the end-user's request to add an association.
        #
        # We then redirect the end-user to `/associations`.

        else:
            requester.post(
                ADD_ASSOCIATION, 
                data=flask.request.form
            )

            return flask.redirect(
                flask.url_for("show_associations")
            )


    @app.route("/associations/delete", methods=["POST"])
    def delete_association():
        """
        This is the endpoint for deleting an association.

        It accepts a `POST` request.  It returns HTML.
        """

        # On receiving a `POST` request, we forward the
        # form data in the body of the request to the API.
        # This contains the end-user's request to delete an association.

        requester.post(
            DELETE_ASSOCIATION, 
            data=flask.request.form
        )

        # We redirect the end-user to `/associations`.

        return flask.redirect(
            flask.url_for("show_associations")
        )


    @app.route("/associations/update", methods=["GET", "POST"])
    def update_association():
        """
        This is the endpoint for updating an association.

        It accepts a `GET` or a `POST` request.  It returns HTML.
        """

        # On receiving a `GET` request, we attempt to obtain the
        # value of the `id` query parameter.
        #
        # If there is no `id`, then we redirect the end-user to
        # `/associations`.
        #
        # Otherwise, we request all stakeholders, all deliverables, 
        # and a single association from the API.
        #
        # We then return `update-association.html`.

        if flask.request.method == "GET":
            id = flask.request.args.get("id")

            if id is None:
                return flask.redirect(
                    flask.url_for("show_associations")
                )

            else:
                stakeholders = requester.get(SHOW_STAKEHOLDERS)
                deliverables = requester.get(SHOW_DELIVERABLES)
                associations = requester.get(
                    "{}?id={}".format(SHOW_ASSOCIATIONS, id)
                )

                responses = {
                    "stakeholders": stakeholders.json(),
                    "deliverables": deliverables.json(),
                    "associations": associations.json()
                }

                return flask.render_template(
                    "update-association.html", 
                    data=responses
                )

        # On receiving a `POST` request, we forward the
        # form data in the body of the request to the API.
        # This contains the end-user's request to update an association.
        #
        # We then redirect the end-user to `/associations`.

        else:
            requester.post(
                UPDATE_ASSOCIATION, 
                data=flask.request.form
            )

            return flask.redirect(
                flask.url_for("show_associations")
            )


    @app.route("/management-plan")
    def show_management_plan():
        """
        This is the endpoint for showing the management plan.

        It accepts a `GET` request.  It returns HTML.
        """

        # We request the management plan from the API.

        response = requester.get(SHOW_MANAGEMENT_PLAN)

        # We then return `show-management-plan.html`.

        return flask.render_template(
            "show-management-plan.html",
            data=response.json()
        )


    return app
