.. _examples:

Examples
========

Making a database
-----------------
In this library, a database is just a directory. Here's how you can make a database::

    >>> import py_database as pydb

    >>> db_name: str = "my_awesome_database"

    # Creates the directory if it does not already exist, and initializes the database object.
    >>> db = pydb.Database(db_name)

It's as simple as that.

Making a record
---------------
Large chunks of data are seperated through "records", which are the python files which actually hold the database's data. It's very simple to make a record::

    # You don't have to include the `.py` file extension in your record name
    >>> record_name: str = "foo"

    # Creates a record if it doesn't already exist, and overwrites it if it does.
    >>> db.create_record(record_name, overwrite=True)
