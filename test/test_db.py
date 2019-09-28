import sqlite3
import pytest
import stakeholders.db


def test_repr(file):
    with stakeholders.db.Database(file=file) as db:
        assert repr(db) == "Database(file='{}')".format(file)


def test_str(file, capsys):
    with stakeholders.db.Database(file=file) as db:
        print(db)
        stdout, stderr = capsys.readouterr()
        assert stdout == "{}".format(file) + "\n"


# We try to select all records from the `stakeholders` table 
# before actually creating it.
# We expect SQLite to raise an exception.

def test_create_stakeholders_table_error(file):
    with pytest.raises(sqlite3.OperationalError) as exception:
        with stakeholders.db.Database(file=file) as db:
            db.select_all_from_stakeholders_table()

    assert "no such table: stakeholders" == str(exception.value)


# We create the `stakeholders` table.
# We then select all records.
# We expect `results` to have a length of zero.

def test_create_stakeholders_table(file):
    with stakeholders.db.Database(file=file) as db:
        db.create_stakeholders_table()
        results = db.select_all_from_stakeholders_table()

    assert len(results) == 0


# We drop the `stakeholders` table.
# We then try to select all records.
# We expect SQLite to raise an exception.
# (We use the `db` fixture here.)

def test_drop_stakeholders_table(db):
    with pytest.raises(sqlite3.OperationalError) as exception:
        db.drop_stakeholders_table()
        db.select_all_from_stakeholders_table()

    assert "no such table: stakeholders" == str(exception.value)


# We select all records from the `stakeholders` table.
# We expect `results` to have a length of two.
# (We use the `db` fixture here.)

def test_select_all_from_stakeholders_table(db):
    results = db.select_all_from_stakeholders_table()
    assert len(results) == 2


# We select one record from the `stakeholders` table.
# We expect `results` to have a length of one and
# for that record to be the correct one.
# (We use the `db` fixture here.)

def test_select_from_stakeholders_table(db):
    results = db.select_from_stakeholders_table(id=1)
    assert len(results) == 1
    assert results[0]["id"] == 1
    assert results[0]["name"] == "stakeholder #1"
    assert results[0]["role"] == "project sponsor"
    assert results[0]["sentiment"] == "😀"
    assert results[0]["power"] == "high"
    assert results[0]["interest"] == "high"
    assert results[0]["approach"] == "monitor closely"


# We insert a record into the `stakeholders` table.
# We then select all records.
# We expect `results` to have a length of three.
# (We use the `db` fixture here.)

def test_insert_into_stakeholders_table(db):
    db.insert_into_stakeholders_table(**{
        "name": "stakeholder #3",
        "role": "end-user",
        "sentiment": "😀",
        "power": "low",
        "interest": "high",
        "approach": "keep informed"
    })
 
    results = db.select_all_from_stakeholders_table()
    assert len(results) == 3


# We update a record in the `stakeholders` table.
# We then select that record and evaluate its fields.
# (We use the `db` fixture here.)

def test_update_stakeholders_table(db):
    db.update_stakeholders_table(**{
        "id": 1,
        "name": "updated",
        "role": "updated",
        "sentiment": "updated",
        "power": "updated",
        "interest": "updated",
        "approach": "updated",
    })

    results = db.select_from_stakeholders_table(id=1)
    assert len(results) == 1
    assert results[0]["id"] == 1
    assert results[0]["name"] == "updated"
    assert results[0]["role"] == "updated"
    assert results[0]["sentiment"] == "updated"
    assert results[0]["power"] == "updated"
    assert results[0]["interest"] == "updated"
    assert results[0]["approach"] == "updated"


# We delete a record fom the `stakeholders` table.
# We then select all records.
# We expect `results` to have length of one.
# (We use the `db` fixture here.)

def test_delete_from_stakeholders_table(db):
    db.delete_from_stakeholders_table(id="1")
    results = db.select_all_from_stakeholders_table()
    assert len(results) == 1


# We try to select all records from the `deliverables` table 
# before actually creating it.
# We expect SQLite to raise an exception.

def test_create_deliverables_table_error(file):
    with pytest.raises(sqlite3.OperationalError) as exception:
        with stakeholders.db.Database(file=file) as db:
            db.select_all_from_deliverables_table()

    assert "no such table: deliverables" == str(exception.value)


# We create the `deliverables` table.
# We then select all records.
# We expect `results` to have a length of zero.

def test_create_deliverables_table(file):
    with stakeholders.db.Database(file=file) as db:
        db.create_deliverables_table()
        results = db.select_all_from_deliverables_table()

    assert len(results) == 0


# We drop the `deliverables` table.
# We then try to select all records.
# We expect SQLite to raise an exception.
# (We use the `db` fixture here.)

def test_drop_deliverables_table(db):
    with pytest.raises(sqlite3.OperationalError) as exception:
        db.drop_deliverables_table()
        db.select_all_from_deliverables_table()

    assert "no such table: deliverables" == str(exception.value)


# We select all records from the `deliverables` table.
# We expect `results` to have a length of two.
# (We use the `db` fixture here.)

def test_select_all_from_deliverables_table(db):
    results = db.select_all_from_deliverables_table()
    assert len(results) == 2


# We select one record from the `deliverables` table.
# We expect `results` to have a length of one and
# for that record to be the correct one.
# (We use the `db` fixture here.)

def test_select_from_deliverables_table(db):
    results = db.select_from_deliverables_table(id=1)
    assert len(results) == 1
    assert results[0]["id"] == 1
    assert results[0]["name"] == "deliverable #1"
    assert results[0]["kind"] == "interactive"
    assert results[0]["medium"] == "in-person meeting"
    assert results[0]["formality"] == "formal"
    assert results[0]["frequency"] == "daily"


# We insert a record into the `deliverables` table.
# We then select all records.
# We expect `results` to have a length of three.
# (We use the `db` fixture here.)

def test_insert_into_deliverables_table(db):
    db.insert_into_deliverables_table(**{
        "name": "deliverable #3",
        "kind": "pull",
        "medium": "online collaboration tool",
        "formality": "casual",
        "frequency": "monthly"
    })
 
    results = db.select_all_from_deliverables_table()
    assert len(results) == 3


# We update a record in the `deliverables` table.
# We then select that record and evaluate its fields.
# (We use the `db` fixture here.)

def test_update_deliverables_table(db):
    db.update_deliverables_table(**{
        "id": 1,
        "name": "updated",
        "kind": "updated",
        "medium": "updated",
        "formality": "updated",
        "frequency": "updated"
    })

    results = db.select_from_deliverables_table(id=1)
    assert len(results) == 1
    assert results[0]["id"] == 1
    assert results[0]["name"] == "updated"
    assert results[0]["kind"] == "updated"
    assert results[0]["medium"] == "updated"
    assert results[0]["formality"] == "updated"
    assert results[0]["frequency"] == "updated"


# We delete a record fom the `deliverables` table.
# We then select all records.
# We expect `results` to have length of one.
# (We use the `db` fixture here.)

def test_delete_from_deliverables_table(db):
    db.delete_from_deliverables_table(id="1")
    results = db.select_all_from_deliverables_table()
    assert len(results) == 1


# We try to select all records from the `associations` table
# before actually creating it.
# We expect SQLite to raise an exception.
# (This `SELECT` statement requires the `stakeholders` and 
# `deliverables` tables, so we create them at the beginning of the test.)

def test_create_associations_table_error(file):
    with pytest.raises(sqlite3.OperationalError) as exception:
        with stakeholders.db.Database(file=file) as db:
            db.create_stakeholders_table()
            db.create_deliverables_table()
            db.select_all_from_associations_table()

    assert "no such table: associations" == str(exception.value)


# We create the `associations` table.
# We then select all records.
# We expect `results` to have a length of zero.
# (This `SELECT` statement requires the `stakeholders` and 
# `deliverables` tables, so we create them at the beginning of the test.)

def test_create_associations_table(file):
    with stakeholders.db.Database(file=file) as db:
        db.create_stakeholders_table()
        db.create_deliverables_table()
        db.create_associations_table()
        results = db.select_all_from_associations_table()

    assert len(results) == 0


# We drop the `associations` table.
# We then try to select all records.
# We expect SQLite to raise an exception.
# (We use the `db` fixture here.)

def test_drop_associations_table(db):
    with pytest.raises(sqlite3.OperationalError) as exception:
        db.drop_associations_table()
        db.select_all_from_associations_table()

    assert "no such table: associations" == str(exception.value)


# We select all records from the `associations` table.
# We expect `results` to have a length of two.
# (We use the `db` fixture here.)

def test_select_all_from_associations_table(db):
    results = db.select_all_from_associations_table()
    assert len(results) == 2


# We select one record from the `associations` table.
# We expect `results` to have a length of one and
# for that record to be the correct one.
# (We use the `db` fixture here.)

def test_select_from_associations_table(db):
    results = db.select_from_associations_table(id=1)
    assert len(results) == 1
    assert results[0]["id"] == 1
    assert results[0]["stakeholder_id"] == 1
    assert results[0]["stakeholder_name"] == "stakeholder #1"
    assert results[0]["stakeholder_approach"] == "monitor closely"
    assert results[0]["deliverable_id"] == 1
    assert results[0]["deliverable_name"] == "deliverable #1"


# We insert a record into the `associations` table.
# We then select all records.
# We expect `results` to have a length of three.
# (We use the `db` fixture here.)

def test_insert_into_associations_table(db):
    db.insert_into_associations_table(**{
        "stakeholder_id": 1,
        "deliverable_id": 2
    })
 
    results = db.select_all_from_associations_table()
    assert len(results) == 3


# We update a record in the `associations` table.
# We then select that record and evaluate its fields.
# (We use the `db` fixture here.)

def test_update_associations_table(db):
    db.update_associations_table(**{
        "id": 1,
        "stakeholder_id": 1,
        "deliverable_id": 2
    })

    results = db.select_from_associations_table(id=1)
    assert len(results) == 1
    assert results[0]["id"] == 1
    assert results[0]["stakeholder_id"] == 1
    assert results[0]["deliverable_id"] == 2


# We delete a record fom the `associations` table.
# We then select all records.
# We expect `results` to have length of one.
# (We use the `db` fixture here.)

def test_delete_from_associations_table(db):
    db.delete_from_associations_table(id="1")
    results = db.select_all_from_associations_table()
    assert len(results) == 1
