{{ project_name }}
==============


## Setting up the project

Install requirements:

    pip install -r requirements.txt
    bundle install
    npm install

Setup your Python path:

    add2virtualenv .

Setup your environment:

    DJANGO_SETTINGS_MODULE={{ project_name }}.settings
    DEBUG=1
