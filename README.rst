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

To install it without test-related dependencies, run the following command from your shell.

.. code-block:: console

   [user@host ~]$ git clone git@github.com:critical-path/stakeholders.git
   [user@host ~]$ cd stakeholders
   [user@host stakeholders]$ sudo pip install .

(If necessary, replace :code:`pip` with :code:`pip3`.)


Starting stakeholders
=====================

With Docker (preferred)
-----------------------

To start stakeholders with Docker the first time, run the following command from your shell.

.. code-block:: console

   [user@host stakeholders]$ docker-compose up --build

After the first time, run the following command from your shell.  (This will restart the container rather than build it from scratch, preserving your progress.)

.. code-block:: console

   [user@host stakeholders]$ docker-compose up

Without Docker
--------------

To start stakeholders without Docker, run the following commands from your shell.

.. code-block:: console

   [user@host stakeholders]$ chmod +x ./start-api-and-app.sh
   [user@host stakeholders]$ ./start-api-and-app.sh


Using stakeholders
==================

Point your browser to any of the following URLs.

* :code:`http://localhost:8080/`
* :code:`http://localhost:8080/home`
* :code:`http://localhost:8080/index`

Then, add one or more stakeholders.

Next, add one or more deliverables.

Finally, add one or more associations between stakeholders and deliverables.  This will add content to your stakeholder management plan.


Notes on stakeholders
=====================

stakeholders does not enforce constraints on the uniqueness of stakeholders, deliverables, or associations.  This is to avoid unnecessary complexity in the code.


Testing stakeholders
====================

To conduct testing, run the following command from your shell.

.. code-block:: console

   [user@host stakeholders]$ pytest --cov --cov-report=term-missing
