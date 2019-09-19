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
