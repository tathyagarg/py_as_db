.. _docs:

Documentation
=============

The actual specifications of the objects in this project.

Database
--------

.. autoclass:: seaturtle_db.Database

.. automethod:: seaturtle_db.Database.verify_database_existence

.. automethod:: seaturtle_db.Database.create_record

.. automethod:: seaturtle_db.Database.read_record

.. automethod:: seaturtle_db.Database.update_record

.. automethod:: seaturtle_db.Database.delete_record

Exceptions
----------

.. autoexception:: seaturtle_db.NotFoundError

.. autoexception:: seaturtle_db.DatabaseNotFoundError

.. autoexception:: seaturtle_db.RecordNotFoundError

.. autoexception:: seaturtle_db.RecordAlreadyExists