.. image:: https://travis-ci.com/critical-path/stakeholders.svg?branch=master
   :target: https://travis-ci.com/critical-path/stakeholders

.. image:: https://coveralls.io/repos/github/critical-path/stakeholders/badge.svg?branch=master
   :target: https://coveralls.io/github/critical-path/stakeholders?branch=master

.. image:: https://readthedocs.org/projects/stakeholders/badge/?version=latest
   :target: https://stakeholders.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

Introduction
============

Stakeholder management is critical to project management.  Inspired by the Project Management Body of Knowledge, this app helps project teams to perform the principal tasks associated with managing stakeholders.


Installing stakeholders
=======================

stakeholders is available on GitHub at https://github.com/critical-path/stakeholders.

If you do not have pip version 18.1 or higher, then run the following command from your shell.

.. code-block:: console

   [user@host ~]$ sudo pip install --upgrade pip

To install stakeholders with test-related dependencies, run the following commands from your shell.

.. code-block:: console

   [user@host ~]$ git clone git@github.com:critical-path/stakeholders.git
   [user@host ~]$ cd stakeholders
   [user@host stakeholders]$ sudo pip install --editable .[test]

To install it without test-related dependencies, run the following commands from your shell.

.. code-block:: console

   [user@host ~]$ git clone git@github.com:critical-path/stakeholders.git
   [user@host ~]$ cd stakeholders
   [user@host stakeholders]$ sudo pip install .

(If necessary, replace :code:`pip` with :code:`pip3`.)


Starting stakeholders
=====================

To start stakeholders, run the following commands from your shell.

.. code-block:: console

   [user@host stakeholders]$ chmod +x ./start-api-and-app.sh
   [user@host stakeholders]$ ./start-api-and-app.sh


Using stakeholders
==================

Using stakeholders is easy!

View home page
--------------

Point your browser to any of the following URLs.

* :code:`http://localhost:8080/`
* :code:`http://localhost:8080/home`
* :code:`http://localhost:8080/index`

Add stakeholders
----------------

In the navbar, select :code:`stakeholders` and then :code:`add`.

Use the form to identify and evaluate a stakeholder.  Enter the stakeholder's name, role, sentiment toward your project, level of power, and level of interest in your project.  Then click on the :code:`add` button.

Repeat this process as many times as necessary.

Show stakeholders
-----------------

In the navbar, select :code:`stakeholders` and then :code:`show/update/delete`.

Your stakeholders appear here, sorted by their unique identifiers.  Each stakeholder has a management approach, which is a function of that stakeholder's levels of power and interest.

=============== ======= ======== ======
Approach        Power   Interest Flag
=============== ======= ======== ======
Monitor closely high    high     red
Keep satisfied  high    low      orange
Keep informed   low     high     green
Monitor         low     low      blue
Unknown         invalid invalid  gray
=============== ======= ======== ======

Add deliverables
----------------

In the navbar, select :code:`deliverables` and then :code:`add`.

Use the form to identify a deliverable, where a deliverable is a reporting requirement.  Enter the deliverable's name, kind (type), medium, level of formality, and frequency.  Then click on the :code:`add` button.

Repeat this process as many times as necessary.

Show deliverables
-----------------

In the navbar, select :code:`deliverables` and then :code:`show/update/delete`.

Your deliverables appear here, sorted by their unique identifiers.

Add associations
----------------

In the navbar, select :code:`associations` and then :code:`add`.

Use the form to identify an association, where an association is the assignment of a deliverable to a stakeholder.  Enter a stakeholder and a deliverable appropriate for that stakeholder.  Then click on the :code:`add` button.

Repeat this process as many times as necessary.  (It is possible to assign multiple deliverables to the same stakeholder as well as to assign the same deliverable to multiple stakeholders.)

Show associations
-----------------

In the navbar, select :code:`associations` and then :code:`show/update/delete`.

Your associations appear here, sorted by their unique identifiers.

View management plan
--------------------

In the navbar, select :code:`management-plan`.

Your associations appear here, sorted first by management approach, then by stakeholders' unique identifiers, and then by deliverables' unique identifiers.

This is your stakeholder management plan - the whole purpose of this app! 

Make updates
------------

In the navbar, select :code:`stakeholders`, :code:`deliverables`, or :code:`associations` and then :code:`show/update/delete`.

Find a stakeholder, deliverable, or association and then click on its :code:`update` or :code:`delete` button.


Notes on stakeholders
=====================

stakeholders does not enforce constraints on the uniqueness of stakeholders, deliverables, or associations.  This is to avoid unnecessary complexity in the code.


Testing stakeholders
====================

To execute tests that do not require a web browser, run the following command from your shell.

.. code-block:: console

   [user@host stakeholders]$ pytest -m "not browser" --cov --cov-report=term-missing

To execute tests that require a web browser, run the following commands from your shell.  (Be sure to install Firefox and geckodriver first, however.)

.. code-block:: console

   [user@host stakeholders]$ chmod +x ./run-browser-tests.sh
   [user@host stakeholders]$ ./run-browser-tests.sh
