A simple Django 1.7 project
===========================

Design Considerations
---------------------

Almost everything is optimized for *simplicity*. If you're maintaining dozens
of Django sites, you don't want to have to wade through a lot of files. The
Django project is designed to be deployable-to `Heroku
<https://devcenter.heroku.com/articles/getting-started-with-django>`_.


Django Project Layout
---------------------

Here's the layout of a fictional Django project called "elderberry" with one
app called "camelot"::

    ├─elderberry
    │ ├─apps/
    │ │ └─camelot
    │ │   ├─static/camelot
    │ │   │ ├─app.css
    │ │   │ └─app.js
    │ │   ├─static_src
    │ │   │ ├─js
    │ │   │ └─sass
    │ │   ├─templates/camelot
    │ │   │ └─index.html
    │ │   ├─tests/
    │ │   │ ├─test_models.py
    │ │   │ └─test_views.py
    │ │   ├─factories.py
    │ │   ├─models.py
    │ │   ├─urls.py
    │ │   └─views.py
    │ ├─libs/
    │ ├─settings.py
    │ ├─urls.py
    │ └─wsgi.py
    ├─.env
    ├─LICENSE
    ├─Makefile
    ├─Procfile
    ├─README.md
    ├─manage.py
    ├─package.json
    └─requirements.txt

If it looks really complicated for a "simple" project, I think so too. I'm
considering changing things up. In particuar, the apps folder makes for very
long import statements and might be confusing with the new Django app registry.


``.env``
''''''''
I store private configuration in an ``.env`` file. It usually looks something
like::

    DJANGO_SETTINGS_MODULE=elderberry.settings
    DATABASE_URL=postgres://docker@elderberry-db1/elderberry_dev

``LICENSE``
'''''''''''
I default to Apache. I hear it has better patent clauses.

``Makefile`` / Task runner
''''''''''''''''''''''

I use ``make`` as my general task runner. For bigger projects, I add `Invoke
<http://invoke.readthedocs.org/en/latest/>`_ too.

My ``makefile`` commands are:

* **help** -- So when I type ``make``, I get a help instead of accidentally
  running a task
* **clean** -- A kill 'em all approach to deleting all transient state in the
  project
* **test** -- Always make ``make test`` a thing
* **resetdb** -- Have some way to blow away and recreate the database

``Procfile``
''''''''''''
For Heroku support. You'll notice I use waitress instead of gunicorn like the
Heroku docs say to use.

`waitress vs gunicorn <https://github.com/etianen/django-herokuapp/issues/9#issuecomment-14165240>`_

``README.md``
'''''''''''''
I use Markdown because I don't like using ReStructured Text. Projects are never
published to PyPI, so I can use the format I prefer.

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

Notable requirements:

* **dj-database-url** -- pluck database settings from the environment
* **project-runpy** -- my own meta package of utilities:

  * **env** -- get environment variables without type casting boilerplate
  * **ColorizingStreamHandler** -- friendlier console logging
  * **ReadableSqlFilter** -- for debugging sql statements in the console log

* **django-extensions** -- more utilites I find useful
* **whitenoise** -- for serving staticfiles
* **waitress** -- lightweight wsgi server instead of nginx/gunicorn
* **factory-boy** -- makes it easier to set up tests

``elderberry/settings.py``
''''''''''''''''''''''''''
I use a single ``settings.py`` file, not a settings module. Logic for different
environments are done with environment variables.

``elderberry/urls.py``
''''''''''''''''''''''
I almost always add a namespace to my includes, even if my project only has one
app. Odds are, you're probably adding a namespace to your URL names one way or
another. You might as well do it the way the developers intended. *TODO:
favicon.ico and robots.txt*

``elderberry/wsgi.py``
''''''''''''''''''''''
This is the standard Django wsgi.py with ``whitenoise`` to serve static media.
If you've read the Heroku Django guide, it recommends dj-static, but my
personal experience is that whitenoise is much better.

`django-developers discussion <https://groups.google.com/d/msgid/django-developers/9B11AB1B-2850-401D-97BA-FB7C73268672%40gmail.com>`_

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

``elderberry/apps/camelot/static_src/``
'''''''''''''''''''''''''''''''''''''''
I keep my SASS and JS files in ``static_src/`` directories, and `Grunt`_
compiles them into the typical ``static/`` directory. There are many reasons
why I split them apart:

1. This establishes a separation between "source" files developers workon and
   "dist" files that are meant to be served.
2. This keeps dev files from getting into the production asset pipeline. They
   don't get collected, don't get hashed, and don't clutter my deploy logs.

The ``static/`` directory is in ``.gitignore`` so compiled files stay out of
source control. Version pinning in ``package.json`` makes it so everyone
generates the same output. For Heroku, the compiled files are force added to
the source, but only for Heroku. For deployment elsewhere, the Dockerfile also
builds and collects staticfiles.

TODO
----

* Add coverage
* Gruntfile.coffee
* Bower
* Need to specify buildpack_url for heroku
