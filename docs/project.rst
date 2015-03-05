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


Django Project Layout
---------------------

Here's the layout of a fictional Django project called "elderberry"::

    ├─ elderberry
    │  ├─ apps/
    │  ├─ libs/
    │  ├─ settings.py
    │  ├─ urls.py
    │  └─ wsgi.py
    ├─ .env
    ├─ Makefile
    ├─ Procfile
    ├─ manage.py
    ├─ package.json
    └─ requirements.txt


``.env``
''''''''
I store private configuration in an ``.env`` file. It usually looks something
like::

    DJANGO_SETTINGS_MODULE=elderberry.settings
    DATABASE_URL=postgres://docker@elderberry-db1/elderberry_dev

``Makefile`` / Task runner
''''''''''''''''''''''

I use ``make`` as my general task runner. For bigger projects, I like `Invoke
<http://invoke.readthedocs.org/en/latest/>`_

My ``makefile`` commands are:

* **help** -- So when I type ``make``, I get a help instead of accidentally
  running a task
* **clean** -- A kill 'em all approach to deleting all transient state in the
  project
* **test** -- Always make ``make test`` a thing
* **resetdb** -- Have some way to blow away and recreate the database

``Procfile``
''''''''''''
For Heroku support.

``manage.py``
'''''''''''''
This is the one Django file I leave in the root because Heroku's default Python
buildpack will automatically run ``collectstatic`` for you if ``manage.py`` is
in the root.

``package.json``
''''''''''''''''
JavasScript requirements. I use `Grunt <http://gruntjs.com/>`_ for compiling
static media. It just works, has good support, and good documentation. I use
CoffeeScript syntax for my Gruntfiles because it's terser, and so I don't have
to mess with trailing commas. This also means git diffs are more readable.

``requirements.txt``
''''''''''''''''''''
I use one requirements file containing production, dev, testing, and ci
requirements. For a bigger project, I would split these up so each environment
only installs what it needs. For this simple project, I just throw everything
into one file. Everything is pinned to a specific version to prevent pulling a
breaking change.

``elderberry/settings.py``
''''''''''''''''''''''''''
I use a single ``settings.py`` file, not a settings module. Logic for different
environments are done with environment variables.

``elderberry/apps/``
''''''''''''''''''''
All internal Django apps go here. This means that your project will be full
Based on research into other Django project layouts, and the `django-skel <http
://django-skel.readthedocs.org/en/latest/layout/>`_ project. If it's in your
``INSTALLED_APPS``, it goes in the ``apps/`` directory.

``elderberry/libs/``
''''''''''''''''''''
I have a ``libs/`` directory like `django-skel`_ too, except I use it as a
dumping ground for Python code that's local to the project, but not in
``INSTALLED_APPS``. That usually means it's full of little utilities, but there
can be Django views here too (just nothing with models). Think of this as a
``site-packages`` inside your project.

``app/static_src/``
'''''''''''''''''''
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
* Gruntfile.coffee
* ``whitenoise``
* Bower
* Need to specify buildpack_url for heroku
* required .env
