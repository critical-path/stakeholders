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
