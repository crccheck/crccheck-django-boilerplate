## Quickstart App

1. download/clone this someplace local
2. start off in your new app's directory

```bash
mkvirtualenv `basename $PWD`
pip install Django
/path/to/crccheck-django-boilerplate/build_app <app_name>
git init
git commit -m "initial commit" --allow-empty
git add .
git commit -m "initial project structure"
pip install -r requirements.txt
```

## Quickstart Project

Run this from your project base, change `$project_name` to a valid project
name. This will create a directory with the template contents in a new
directory of the same name.

```bash
mkvirtualenv $project_name
pip install Django
django-admin startproject \
  --template=https://github.com/crccheck/crccheck-dj-project-boilerplate/archive/master.zip \
  --extension=md,json,gitignore,coffee $project_name
cd $project_name
git init
git commit -m "initial commit (empty)" --allow-empty
```
