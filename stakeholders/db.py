"""
This module contains the Database class.
"""


import sqlite3


class Database():
    """
    The `Database` class.
    """

    def __init__(
        self, 
        file="stakeholders.sqlite3"
    ):
        """
        Instantiates a `Database` object.

        Parameters
        ----------
        file : str
            The name of the database file
            (`stakeholders.sqlite3` by default).
        """

        self.file = file
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.close()

    def __repr__(self):
        return "Database(file='{}')".format(self.file)

    def __str__(self):
        return self.file

    def open(self):
        """
        Opens a connection to the database.
        """

        self.connection = sqlite3.connect(self.file)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def close(self):
        """
        Closes the connection to the database.
        """

        self.connection.commit()
        self.cursor.close()

    def create_stakeholders_table(self):
        """
        Creates the `stakeholders` table.
        """

        statement = """CREATE TABLE IF NOT EXISTS stakeholders (
                           id        INTEGER PRIMARY KEY AUTOINCREMENT,
                           name      TEXT    NOT NULL,
                           role      TEXT    NOT NULL,
                           sentiment TEXT    NOT NULL,
                           power     TEXT    NOT NULL,
                           interest  TEXT    NOT NULL,
                           approach  TEXT    NOT NULL
                       );"""

        self.cursor.execute(statement)

    def create_deliverables_table(self):
        """
        Creates the `deliverables` table.
        """

        statement = """CREATE TABLE IF NOT EXISTS deliverables (
                           id        INTEGER PRIMARY KEY AUTOINCREMENT,
                           name      TEXT    NOT NULL,
                           kind      TEXT    NOT NULL,
                           medium    TEXT    NOT NULL,
                           formality TEXT    NOT NULL,
                           frequency TEXT    NOT NULL
                       );"""

        self.cursor.execute(statement)

    def create_associations_table(self):
        """
        Creates the `associations` table.
        """

        statement = """CREATE TABLE IF NOT EXISTS associations  (
                           id             INTEGER PRIMARY KEY AUTOINCREMENT,
                           stakeholder_id INTEGER NOT NULL,
                           deliverable_id INTEGER NOT NULL
                       );"""

        self.cursor.execute(statement)

    def drop_stakeholders_table(self):
        """
        Drops the `stakeholders` table.
        """

        statement = """DROP TABLE IF EXISTS stakeholders;"""

        self.cursor.execute(statement)

    def drop_deliverables_table(self):
        """
        Drops the `deliverables` table.
        """

        statement = """DROP TABLE IF EXISTS deliverables;"""

        self.cursor.execute(statement)

    def drop_associations_table(self):
        """
        Drops the `associations` table.
        """

        statement = """DROP TABLE IF EXISTS associations;"""

        self.cursor.execute(statement)

    def insert_into_stakeholders_table(
        self, 
        name=None, 
        role=None, 
        sentiment=None,
        power=None, 
        interest=None,
        approach=None
    ):
        """
        Inserts a record into the `stakeholders` table,
        where the record represents a stakeholder.

        Parameters
        ----------
        name : str
            The stakeholder's name.

        role : str
            The stakeholder's role.

        sentiment : str
            The stakeholder's sentiment.

        power : str
            The stakeholder's level of power.

        interest : str
            The stakeholder's level of interest.

        approach : str
            The approach to managing this stakeholder.
        """

        statement = """INSERT INTO stakeholders 
                       (name, role, sentiment, power, interest, approach)    
                            VALUES (?, ?, ?, ?, ?, ?);"""

        self.cursor.execute(
            statement, 
            (name, role, sentiment, power, interest, approach,)
        )

    def insert_into_deliverables_table(
        self, 
        name=None, 
        kind=None, 
        medium=None,
        formality=None,
        frequency=None
    ):
        """
        Inserts a record into the `deliverables` table,
        where the record represents a deliverable.

        Parameters
        ----------
        name : str
            The deliverable's name.

        kind : str
            The deliverable's kind.

        medium : str
            The deliverable's medium.

        formality : str
            The deliverable's level of formality.

        frequency : str
            The deliverable's frequency.
        """

        statement = """INSERT INTO deliverables 
                       (name, kind, medium, formality, frequency)
                            VALUES (?, ?, ?, ?, ?);"""

        self.cursor.execute(
            statement, 
            (name, kind, medium, formality, frequency,)
        )

    def insert_into_associations_table(
        self, 
        stakeholder_id=None, 
        deliverable_id=None
    ):
        """
        Inserts a record into the `associations` table,
        where a record represents a relationship between a
        stakeholder and a deliverable.

        Parameters
        ----------
        stakeholder_id : int
            A stakeholder's unique `id` as found in
            the `stakeholders` table.

        deliverable_id : int
            A deliverable's unique `id` as found in
            the `deliverables` table.
        """

        statement = """INSERT INTO associations 
                       (stakeholder_id, deliverable_id)    
                            VALUES (?, ?);"""

        self.cursor.execute(
            statement, 
            (stakeholder_id, deliverable_id,)
        )

    def select_all_from_stakeholders_table(self):
        """
        Selects all records and fields from the `stakeholders` table.

        Returns
        -------
        list
            A list of records.
        """

        statement = """SELECT id,
                              name,
                              role,
                              sentiment,
                              power,
                              interest,
                              approach
                         FROM stakeholders;"""

        records = self.cursor.execute(statement).fetchall()

        return list(
            map(
                lambda record: dict(zip(record.keys(), record)), records
            )
        )

    def select_all_from_deliverables_table(self):
        """
        Selects all records and fields from the `deliverables` table.

        Returns
        -------
        list
            A list of records.
        """

        statement = """SELECT id,
                              name,
                              kind,
                              medium,
                              formality,
                              frequency
                         FROM deliverables;"""

        records = self.cursor.execute(statement).fetchall()

        return list(
            map(
                lambda record: dict(zip(record.keys(), record)), records
            )
        )

    def select_all_from_associations_table(self):
        """
        Selects all records and fields from the `associations` table.

        Returns
        -------
        list
            A list of records.
        """

        statement = """SELECT associations.id,
                              associations.stakeholder_id, 
                              stakeholders.name AS stakeholder_name,
                              stakeholders.approach AS stakeholder_approach,
                              associations.deliverable_id, 
                              deliverables.name AS deliverable_name
                         FROM stakeholders,
                              deliverables
                         JOIN associations 
                           ON stakeholders.id = associations.stakeholder_id
                          AND deliverables.id = associations.deliverable_id
                     ORDER BY associations.stakeholder_id,
                              associations.deliverable_id;"""

        records = self.cursor.execute(statement).fetchall()

        return list(
            map(
                lambda record: dict(zip(record.keys(), record)), records
            )
        )

    def select_from_stakeholders_table(
        self, 
        id=None
    ):
        """
        Selects one record and all fields from the `stakeholders` table.

        Parameters
        ----------
        id : str
            A stakeholder's unique `id` as found in
            the `stakeholders` table.

        Returns
        -------
        list
            A list with one record.
        """

        statement = """SELECT id,
                              name,
                              role,
                              sentiment,
                              power,
                              interest,
                              approach
                         FROM stakeholders
                        WHERE id = ?;"""

        records = self.cursor.execute(statement, (id,)).fetchall()

        return list(
            map(
                lambda record: dict(zip(record.keys(), record)), records
            )
        )

    def select_from_deliverables_table(
        self, 
        id=None
    ):
        """
        Selects one record and all fields from the `deliverables` table.

        Parameters
        ----------
        id : int
            A deliverable's unique `id` as found in
            the `deliverables` table.

        Returns
        -------
        list
            A list with one record.
        """

        statement = """SELECT id,
                              name,
                              kind,
                              medium,
                              formality,
                              frequency
                         FROM deliverables
                        WHERE id = ?;"""

        records = self.cursor.execute(statement, (id,)).fetchall()

        return list(
            map(
                lambda record: dict(zip(record.keys(), record)), records
            )
        )

    def select_from_associations_table(
        self,
        id=None
    ):
        """
        Selects one record and all fields from the `associations` table.

        Parameters
        ----------
        id : int
            An association's unique `id` as found in
            the `associations` table.

        Returns
        -------
        A list with one record.
        """

        statement = """SELECT associations.id, 
                              associations.stakeholder_id, 
                              stakeholders.name AS stakeholder_name,
                              stakeholders.approach AS stakeholder_approach, 
                              associations.deliverable_id, 
                              deliverables.name AS deliverable_name
                         FROM stakeholders,
                              deliverables
                         JOIN associations 
                           ON stakeholders.id = associations.stakeholder_id
                          AND deliverables.id = associations.deliverable_id
                        WHERE associations.id = ?;"""

        records = self.cursor.execute(statement, (id,)).fetchall()

        return list(
            map(
                lambda record: dict(zip(record.keys(), record)), records
            )
        )

    def update_stakeholders_table(
        self,
        id=None,
        name=None,
        role=None,
        sentiment=None,
        power=None,
        interest=None,
        approach=None
    ):
        """
        Updates a record in the `stakeholders` table.

        Parameters
        ----------
        id : str
            A stakeholder's unique `id` as found in
            the `stakeholders` table.

        name : str
            The stakeholder's name.

        role : str
            The stakeholder's role.

        sentiment : str
            The stakeholder's sentiment.

        power : str
            The stakeholder's level of power.

        interest : str
            The stakeholder's level of interest.

        approach : str
            The approach to managing this stakeholder.
        """

        statement = """UPDATE stakeholders
                          SET name = ?,
                              role = ?,
                              sentiment = ?,
                              power = ?,
                              interest = ?,
                              approach = ?
                        WHERE id = ?;""";

        self.cursor.execute(
            statement, 
            (name, role, sentiment, power, interest, approach, id,)
        )

    def update_deliverables_table(
        self,
        id=None,
        name=None,
        kind=None,
        medium=None,
        formality=None,
        frequency=None
    ):
        """
        Updates a record in the `deliverables` table.

        Parameters
        ----------
        id : int
            A deliverable's unique `id` as found in
            the `deliverables` table.

        name : str
            The deliverable's name.

        kind : str
            The deliverable's kind.

        medium : str
            The deliverable's medium.

        formality : str
            The deliverable's level of formality.

        frequency : str
            The deliverable's frequency.
        """

        statement = """UPDATE deliverables
                          SET name = ?,
                              kind = ?,
                              medium = ?,
                              formality = ?,
                              frequency = ?
                        WHERE id = ?;"""

        self.cursor.execute(
            statement, 
            (name, kind, medium, formality, frequency, id,)
        )

    def update_associations_table(
        self,
        id=None,
        stakeholder_id=None,
        deliverable_id=None
    ):
        """
        Updates a record in the `associations` table.

        Parameters
        ----------
        id : int
            An association's unique `id` as found in
            the `associations` table.

        stakeholder_id : int
            A stakeholder's unique `id` as found in
            the `stakeholders` table.

        deliverable_id : int
            A deliverable's unique `id` as found in
            the `deliverables` table.
        """

        statement = """UPDATE associations
                          SET stakeholder_id = ?,
                              deliverable_id = ?
                        WHERE id = ?;"""

        self.cursor.execute(
            statement,
            (stakeholder_id, deliverable_id, id,)
        )

    def delete_from_stakeholders_table(self, id=None):
        """
        Deletes a record from the `stakeholders` table.

        Parameters
        ----------
        id : str
            A stakeholder's unique `id` as found in
            the `stakeholders` table.
        """

        statement = """DELETE FROM stakeholders
                             WHERE id = ?;"""

        self.cursor.execute(statement, (id,))

    def delete_from_deliverables_table(self, id=None):
        """
        Deletes a record from the `deliverables` table.

        Parameters
        ----------
        id : str
            A deliverable's unique `id` as found in
            the `deliverables` table.
        """

        statement = """DELETE FROM deliverables
                             WHERE id = ?;"""

        self.cursor.execute(statement, (id,))

    def delete_from_associations_table(self, id=None):
        """
        Deletes a record from the `associations` table.

        Parameters
        ----------
        id : str
            An association's unique `id` as found in
            the `associations` table.
        """

        statement = """DELETE FROM associations
                             WHERE id = ?;"""

        self.cursor.execute(statement, (id,))
