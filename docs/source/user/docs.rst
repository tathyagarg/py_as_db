.. _docs:

Documentation
=============

The actual specifications of the objects in this project.

Database
--------

.. autoclass:: py_as_db.Database

.. automethod:: py_as_db.Database.verify_database_existence

.. automethod:: py_as_db.Database.create_record

.. automethod:: py_as_db.Database.read_record

.. automethod:: py_as_db.Database.update_record

.. automethod:: py_as_db.Database.delete_record

Exceptions
----------

.. autoexception:: py_as_db.NotFoundError

.. autoexception:: py_as_db.DatabaseNotFoundError

.. autoexception:: py_as_db.RecordNotFoundError

.. autoexception:: py_as_db.RecordAlreadyExists