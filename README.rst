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

To execute tests that do not require a web browser, run the following command from your shell.

.. code-block:: console

   [user@host stakeholders]$ pytest -m "not browser" --cov --cov-report=term-missing

To execute tests that require a web browser, run the following commands from your shell.  (Be sure to install Firefox and geckodriver first, however.)

.. code-block:: console

   [user@host stakeholders]$ chmod +x ./test-api-and-app.sh
   [user@host stakeholders]$ ./test-api-and-app.sh
   [user@host stakeholders]$ pytest -m "browser"
