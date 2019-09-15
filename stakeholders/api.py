"""
This module contains the API and API factory.
"""


import json
import flask
import stakeholders.db
import stakeholders.utils


def create_api(file="./stakeholders.sqlite3"):
    """
    This is the API factory.  It returns an instance of the API.

    Parameters
    ----------
    file : str
        The name of the database file
        (`stakeholders.sqlite3` by default).

    Returns
    -------
    api : Flask application object
        An instance of the API as a Flask application object.
    """

    api = flask.Flask(__name__)


    @api.route("/api/v1/stakeholders/add", methods=["POST"])
    def add_stakeholder():
        """
        This is the endpoint for adding a stakeholder.

        It accepts a `POST` request.

        It returns a status code (`200`) and a message (`Success`).
        """

        # We open a connection to the database and create the
        # `stakeholders` table if it does not already exist.

        with stakeholders.db.Database(file=file) as db:
            db.create_stakeholders_table()

            # We extract the values of `power` and `interest`
            # from the body of the request and compute
            # the approach for managing this stakeholder.

            approach = stakeholders.utils.compute_approach(
                flask.request.form.get("power"), 
                flask.request.form.get("interest")
            )

            # We create a dict with information on the stakeholder.

            stakeholder = {
                "name": flask.request.form.get("name"),
                "role": flask.request.form.get("role"),
                "sentiment": flask.request.form.get("sentiment"),
                "power": flask.request.form.get("power"),
                "interest": flask.request.form.get("interest"),
                "approach": approach
            }

            # We insert a record into the `stakeholders` table.

            db.insert_into_stakeholders_table(**stakeholder)

            # We return a `200` status code and a `Success` message.

            return (
                "Success", 
                200
            )


    @api.route("/api/v1/stakeholders/show")
    def show_stakeholders():
        """
        This is the endpoint for showing stakeholders.

        It accepts a `GET` request.

        It returns a status code (`200`) and records serialized as JSON.
        """

        # We open a connection to the database and create the
        # `stakeholders` table if it does not already exist.

        with stakeholders.db.Database(file=file) as db:
            db.create_stakeholders_table()

            # If it exists, then we obtain the value of the `id`
            # query parameter.

            id = flask.request.args.get("id")

            # If there is no `id`, then we select all records
            # from the `stakeholders` table.
            #
            # Otherwise, we select a single record
            # from the `stakeholders` table.
 
            if id is None:
                results = db.select_all_from_stakeholders_table()
            else:
                results = db.select_from_stakeholders_table(id=id)
         
            # We return a `200` status code and records serialized
            # as JSON.

            return (
                json.dumps(results), 
                200, 
                {"Content-Type": "application/json"}
            )


    @api.route("/api/v1/stakeholders/update", methods=["POST"])
    def update_stakeholder():
        """
        This is the endpoint for updating a stakeholder.

        It accepts a `POST` request.

        It returns a status code (`200`) and a message (`Success`).
        """

        # We open a connection to the database and create the
        # `stakeholders` table if it does not already exist.

        with stakeholders.db.Database(file=file) as db:
            db.create_stakeholders_table()

            # We extract the values of `power` and `interest`
            # from the body of the request and compute
            # the approach for managing this stakeholder.

            approach = stakeholders.utils.compute_approach(
                flask.request.form.get("power"), 
                flask.request.form.get("interest")
            )

            # We create a dict with information on the stakeholder.

            stakeholder = {
                "id": flask.request.form.get("id"),
                "name": flask.request.form.get("name"),
                "role": flask.request.form.get("role"),
                "sentiment": flask.request.form.get("sentiment"),
                "power": flask.request.form.get("power"),
                "interest": flask.request.form.get("interest"),
                "approach": approach
            }

            # We update a record in the `stakeholders` table.

            db.update_stakeholders_table(**stakeholder)

            # We return a `200` status code and a `Success` message.

            return (
                "Success", 
                200
            )


    @api.route("/api/v1/stakeholders/delete", methods=["POST"])
    def delete_stakeholder():
        """
        This is the endpoint for deleting a stakeholder.

        It accepts a `POST` request.

        It returns a status code (`200`) and a message (`Success`).
        """

        # We open a connection to the database and create the
        # `stakeholders` table if it does not already exist.
        #
        # We delete a record from the `stakeholders` table.

        with stakeholders.db.Database(file=file) as db:
            db.create_stakeholders_table()
            db.delete_from_stakeholders_table(**flask.request.form.to_dict())

            # We return a `200` status code and a `Success` message.

            return (
                "Success", 
                200
            )


    @api.route("/api/v1/deliverables/add", methods=["POST"])
    def add_deliverable():
        """
        This is the endpoint for adding a deliverable.

        It accepts a `POST` request.

        It returns a status code (`200`) and a message (`Success`).
        """

        # We open a connection to the database and create the
        # `deliverables` table if it does not already exist.
        #
        # We insert a record into the `deliverables` table.

        with stakeholders.db.Database(file=file) as db:
            db.create_deliverables_table()
            db.insert_into_deliverables_table(**flask.request.form.to_dict())

            # We return a `200` status code and a `Success` message.

            return (
                "Success", 
                200
            )


    @api.route("/api/v1/deliverables/show")
    def show_deliverables():
        """
        This is the endpoint for showing deliverables.

        It accepts a `GET` request.

        It returns a status code (`200`) and records serialized as JSON.
        """

        # We open a connection to the database and create the
        # `deliverables` table if it does not already exist.
 
        with stakeholders.db.Database(file=file) as db:
            db.create_deliverables_table()

            # If it exists, then we obtain the value of the `id`
            # query parameter.

            id = flask.request.args.get("id")

            # If there is no `id`, then we select all records
            # from the `deliverables` table.
            #
            # Otherwise, we select a single record
            # from the `deliverables` table.

            if id is None:
                results = db.select_all_from_deliverables_table()
            else:
                results = db.select_from_deliverables_table(id=id)

            # We return a `200` status code and records serialized
            # as JSON.

            return (
                json.dumps(results), 
                200, 
                {"Content-Type": "application/json"}
            )


    @api.route("/api/v1/deliverables/update", methods=["POST"])
    def update_deliverable():
        """
        This is the endpoint for updating a deliverable.

        It accepts a `POST` request.

        It returns a status code (`200`) and a message (`Success`).
        """

        # We open a connection to the database and create the
        # `deliverables` table if it does not already exist.
        #
        # We update a record in the `deliverables` table.

        with stakeholders.db.Database(file=file) as db:
            db.create_deliverables_table()
            db.update_deliverables_table(**flask.request.form.to_dict())

            # We return a `200` status code and a `Success` message.

            return (
                "Success", 
                200
            )


    @api.route("/api/v1/deliverables/delete", methods=["POST"])
    def delete_deliverable():
        """
        This is the endpoint for deleting a deliverable.

        It accepts a `POST` request.

        It returns a status code (`200`) and a message (`Success`).
        """

        # We open a connection to the database and create the
        # `deliverables` table if it does not already exist.
        #
        # We delete a record from the `deliverables` table.

        with stakeholders.db.Database(file=file) as db:
            db.create_deliverables_table()
            db.delete_from_deliverables_table(**flask.request.form.to_dict())

            # We return a `200` status code and a `Success` message.

            return (
                "Success", 
                200
            )


    @api.route("/api/v1/associations/add", methods=["POST"])
    def add_association():
        """
        This is the endpoint for adding an association.

        It accepts a `POST` request.

        It returns a status code (`200`) and a message (`Success`).
        """

        # We open a connection to the database and create the
        # `stakeholders`, `deliverables`, and `associations` tables 
        # if they do not already exist.
        #
        # We insert a record into the `associations` table.

        with stakeholders.db.Database(file=file) as db:
            db.create_stakeholders_table()
            db.create_deliverables_table()
            db.create_associations_table()
            db.insert_into_associations_table(**flask.request.form.to_dict())

            # We return a `200` status code and a `Success` message.

            return (
                "Success", 
                200
            )


    @api.route("/api/v1/associations/show")
    def show_associations():
        """
        This is the endpoint for showing associations.

        It accepts a `GET` request.

        It returns a status code (`200`) and records serialized as JSON.
        """

        # We open a connection to the database and create the
        # `stakeholders`, `deliverables`, and `associations` tables 
        # if they do not already exist.

        with stakeholders.db.Database(file=file) as db:
            db.create_stakeholders_table()
            db.create_deliverables_table()
            db.create_associations_table()

            # If it exists, then we obtain the value of the `id`
            # query parameter.

            id = flask.request.args.get("id")

            # If there is no `id`, then we select all records
            # from the `associations` table.
            #
            # Otherwise, we select a single record
            # from the `associations` table.

            if id is None:
                results = db.select_all_from_associations_table()
            else:
                results = db.select_from_associations_table(id=id)

            # We return a `200` status code and records serialized
            # as JSON.

            return (
                json.dumps(results), 
                200, 
                {"Content-Type": "application/json"}
            )


    @api.route("/api/v1/associations/update", methods=["POST"])
    def update_association():
        """
        This is the endpoint for updating an association.

        It accepts a `POST` request.

        It returns a status code (`200`) and a message (`Success`).
        """

        # We open a connection to the database and create the
        # `stakeholders`, `deliverables`, and `associations` tables 
        # if they do not already exist.
        #
        # We update a record in the `associations` table.

        with stakeholders.db.Database(file=file) as db:
            db.create_stakeholders_table()
            db.create_deliverables_table()
            db.create_associations_table()
            db.update_associations_table(**flask.request.form.to_dict())

            # We return a `200` status code and a `Success` message.

            return (
                "Success", 
                200
            )


    @api.route("/api/v1/associations/delete", methods=["POST"])
    def delete_association():
        """
        This is the endpoint for deleting an association.

        It accepts a `POST` request.

        It returns a status code (`200`) and a message (`Success`).
        """

        # We open a connection to the database and create the
        # `stakeholders`, `deliverables`, and `associations` tables 
        # if they do not already exist.
        #
        # We delete a record from the `associations` table.

        with stakeholders.db.Database(file=file) as db:
            db.create_stakeholders_table()
            db.create_deliverables_table()
            db.create_associations_table()
            db.delete_from_associations_table(**flask.request.form.to_dict())

            # We return a `200` status code and a `Success` message.

            return (
                "Success", 
                200
            )


    @api.route("/api/v1/management-plan/show")
    def show_management_plan():
        # We open a connection to the database and create the
        # `stakeholders`, `deliverables`, and `associations` tables 
        # if they do not already exist.

        with stakeholders.db.Database(file=file) as db:
            db.create_stakeholders_table()
            db.create_deliverables_table()
            db.create_associations_table()    

            # We request all records from the `associations` table.

            results = db.select_all_from_associations_table()

            # We map, reduce, and sort these records.

            mapped_reduced_sorted = stakeholders.utils.sort(
                stakeholders.utils.map_reduce(results)
            )

            # We return a `200` status code and records serialized
            # as JSON.

            return (
                json.dumps(mapped_reduced_sorted), 
                200, 
                {"Content-Type": "application/json"}
            )


    return api
