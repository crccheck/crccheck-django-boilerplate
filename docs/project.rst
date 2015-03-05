A simple Django 1.7 project
===========================

Design Considerations
---------------------

Almost everything is optimized for *simplicity*. If you're maintaining dozens
of Django sites, you don't want to have to wade through a lot of files. The
Django project is designed to be deployable-to `Heroku
<https://devcenter.heroku.com/articles/getting-started-with-django>`_.


Project README
--------------

I use Markdown because I don't like using ReStructured Text. Projects are never
published to PyPI, so I can use the format I prefer.


Project License
---------------

I default to Apache. I hear it has better patent clauses.


Requirements
------------

* **Python** -- one ``requirements.txt`` containing production, dev, and
  testing, etc. For a bigger project, I would split these up so each
  environment only installs what it needs. Everything is pinned to a specific
  version to prevent pulling a breaking change.
* **Node** -- Defined by ``package.json``. I use `Grunt <http://gruntjs.com/>`_
  for compiling static media. It just works, has good support, and good
  documentation. I use CoffeeScript syntax for my Gruntfiles because it's
  terser, and so I don't have to mess with trailing commas.


Task Runner
-----------

I use ``make`` as my general task runner. For bigger projects, I like `Invoke
<http://invoke.readthedocs.org/en/latest/>`_

My ``makefile`` commands are:

* **help** -- So when I type ``make``, I get a help instead of accidentally
  running a task
* **clean** -- A kill 'em all approach to deleting all transient state in the
  project
* **test** -- Always make ``make test`` a thing
* **resetdb** -- Have some way to blow away and recreate the database


Settings
--------

I use a single ``settings.py`` file, not a settings module. Logic for different
environments are done with environment variables.


Project Layout
--------------

``apps/``
'''''''''

Based on research into other Django project layouts, and the `django-skel <http
://django-skel.readthedocs.org/en/latest/layout/>`_ project. If it's in your
``INSTALLED_APPS``, it goes in the ``apps/`` directory.

``libs/``
'''''''''

I have a ``libs/`` directory like `django-skel`_ too, except I reserve it for
Python code that's local to the project, but not in your ``INSTALLED_APPS``.
That usually means it's full of little utilities, but there can be Django views
here too, just nothing with models.


``static_src/``
'''''''''''''''
I keep my SASS and JS files in ``static_src/`` directories, and `Grunt`_
compiles them into the typical ``static/`` directory. There are many reasons
why I split them apart:

1. This establishes a separation between "source" files and "dist" files that
   are meant to be served.
2. This keeps a lot of unnecessary dev files from getting into the production
   Django asset pipeline. They don't get collected, don't get hashed, and don't
   clutter my deploy logs.


TODO
----

* Add coverage
* Procfile
* Gruntfile.coffee
* ``whitenoise``
* Bower
* Need to specify buildpack_url for heroku
* required .env
