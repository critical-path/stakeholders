Testing stakeholders
====================

To execute tests that do not require a web browser, run the following command from your shell.

.. code-block:: console

   [user@host stakeholders]$ pytest -m "not browser" --cov --cov-report=term-missing

To execute tests that require a web browser, run the following commands from your shell.  (Be sure to install Firefox and geckodriver first, however.)

.. code-block:: console

   [user@host stakeholders]$ chmod +x ./run-browser-tests.sh
   [user@host stakeholders]$ ./run-browser-tests.sh
