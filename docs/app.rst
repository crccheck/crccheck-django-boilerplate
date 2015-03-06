A Django app
============

A Django project is build by combining apps together. This document will go
over what a typical one of my apps looks like.

My Django apps tend to like this (for an app named "camelot")::

    ├─management/commands
    ├─scripts
    │ └─...
    ├─static/camelot
    │ ├─app.css
    │ └─app.js
    ├─static_src
    │ ├─js
    │ └─sass
    ├─templates/camelot
    │ └─index.html
    ├─tests/
    │ ├─test_models.py
    │ └─test_urls.py
    │ └─test_utils.py
    │ └─test_views.py
    ├─admin.py
    ├─apps.py
    ├─factories.py
    ├─models.py
    ├─urls.py
    ├─utils.py
    └─views.py


``admin.py``
''''''''''''
Django admin support.

``apps.py``
'''''''''''
Django 1.7 `App registry <https://docs.djangoproject.com/en/1.7/ref/applications/>`_
config support.

``factories.py``
''''''''''''''''
I use `Factory Boy <http://factoryboy.readthedocs.org/en/latest/index.html>`_
for all my projects to help write more readable tests.

``models.py``
'''''''''''''
Django models.

``urls.py``
'''''''''''
Your URL patterns.

``utils.py``
''''''''''''
Dumping ground for random code.

``views.py``
''''''''''''
Django views.

``management/commands``
'''''''''''''''''''''''
Django management commands.

``scripts/``
''''''''''''
Scripts to be run from the command line. This code usually isn't covered by
test coverage, and is usually just a thin wrapper around code in utils. These
are different from management commands because management commands need to be
run after the app is incorporated into a project, but scripts may be an
esoteric task you need to do in development.

``static/{{ app_name }}``
'''''''''''''''''''''''
CSS/JS/images, and other static assets you may need to render with the
templates. Namespaced so they don't get clobbered when static files are
collected. If the integration project needs to override an asset, it's
namespaced in the project so developers know what it's for.

``static_src``
''''''''''''''
SCSS/Sass/LESS/CoffeeScript/JSX/etc. to ∞ can go here. It can take many,
sometimes hundreds of files to generate one CSS file. There's no point in
subjecting the deploy or integration project to the source files when they only
need the end result. The static directory becomes much simpler because it only
has (usually) one CSS and one JS and the images.

``templates/{{ app_name }}``
''''''''''''''''''''''''''''
Just like the static directory, templates need to be namespaced for the same
reasons.

``tests/``
''''''''''
The ``startapp`` command will create a ``tests.py`` file, but I always use a
module to organize tests better. I create my tests in the same order as the
original code so I can browse them side-by-side. My views tests tend to be unit
tests, while my ``urls.py`` use the test client to hit the url route, the view,
and the template. I usually check the response code, the number of queries it
takes to render a page, and headers (especially ``Vary`` and ``Cache-Control``).
