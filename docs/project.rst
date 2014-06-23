A Simple Django 1.7 Project
===========================

Design Considerations
---------------------

Almost everything is optimized for *simplicity*. If you're maintaining dozens
of Django sites, you don't want to have to wade through a lot of files. The
Django project is designed to be deployable-to `Heroku
<https://devcenter.heroku.com/articles/getting-started-with-django>`_.


Project Readme
--------------

Is written in Markdown because I don't like using ReStructured Text. Projects
are never published to PyPI, so I can use the format I like.


Project License
---------------

I default to Apache. I hear it has better patent clauses.


Requirements
------------

**Python**: one ``requirements.txt`` containing production, dev, and testing,
etc. Normally, I would split these up, but for the simple approach, I use
something simpler (hah!).

**Node**: I use `Grunt <http://gruntjs.com/>`_ for compiling static media. It
just works, has good support, and good documentation. The requirements are
specified in ``package.json``.

**Ruby**: I use `SASS <http://sass-lang.com/>`_ for compiling css.
Specifically, I use SASS and not SCSS because I can fit more lines of code in
one screen because SASS doesn't use braces. In addition, I use SASS 3.3 because
sourcemaps greatly improve the speed of writing CSS.


Task Runner
-----------

I use ``make`` as my general task runner. For bigger projects, I like `Invoke
<http://invoke.readthedocs.org/en/latest/>`_

My ``makefile`` commands are: *TODO*


Settings
--------

I use a single ``settings.py`` file, not a settings module. Logic for different
environments are done with enironment variables.


Project Layout
--------------

``apps``
^^^^^^^^

Based on research into other Django project layouts, and the `django-skel <http
://django-skel.readthedocs.org/en/latest/layout/>`_ project. If it's in your
``INSTALLED_APPS``, it goes in the ``apps/`` directory.

``libs``
^^^^^^^^

I have a ``libs/`` directory like `django-skel`_ too, except I reserve it for
Python code that's local to the project, but not in your ``INSTALLED_APPS``.
That usually means it's full of little utilities, but there can be Django views
here too, just nothing with models.


TODO
----

* Add coverage
* Procfile
* Grunfile.coffee
* ``whitenoise``
* Bower
* Need to specify buildpack_url for heroku
* required .env
