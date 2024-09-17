.. _docs:

Documentation
=============

The actual specifications of the objects in this project.

Database
--------

.. autoclass:: py_database.Database

.. automethod:: py_database.Database.verify_database_existence

.. automethod:: py_database.Database.create_record

.. automethod:: py_database.Database.read_record

.. automethod:: py_database.Database.update_record

.. automethod:: py_database.Database.delete_record

Exceptions
----------

.. autoexception:: py_database.NotFoundError

.. autoexception:: py_database.DatabaseNotFoundError

.. autoexception:: py_database.RecordNotFoundError

.. autoexception:: py_database.RecordAlreadyExists