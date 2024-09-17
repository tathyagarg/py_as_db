.. seaturtle_db documentation master file, created by
   sphinx-quickstart on Tue Sep 17 13:34:39 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

seaturtle_db - Using Python files as a database
===============================================

Release v\ |version| (:doc:`/user/install`)

.. image:: https://img.shields.io/github/license/tathyagarg/seaturtle_db
    :alt: MIT Licensed

.. image:: https://img.shields.io/github/commit-activity/t/tathyagarg/seaturtle_db
    :target: https://github.com/tathyagarg/seaturtle_db
    :alt: Total GitHub commits to `seaturtle_db`

**seaturtle_db** is a Python library to make databases in the form of python files. Obviously, this is just a joke and serves little to no practical benefits over other databasing software. This won't stop me from making this project way over the top.

.. note::
    This project is under active development

Ever wanted to use python files instead of json? Ever wanted to use python files instead of SQL databases? No? I don't care. You can do that now:
    >>> import seaturtle_db as pydb
    >>> db = pydb.Database('my_awesome_database')
    >>> db.create_record('foo')
    >>> db.update_record('foo', {'my_favorite_number': 4})
    >>> db.read_record('foo')
    {'my_favorite_number': 4}

Obviously (not) superior to every other databasing software out there.
:ref:`Install <install>` it. Now.

For the user
------------

Everything you need as a user to get started with this horrendous method of storing data.

.. toctree::
   :maxdepth: 2

   user/install
   user/examples
   user/docs
