## Quickstart

```bash
mkvirtualenv `basename $PWD`
pip install Django
django-admin startproject --template=../crccheck-django-boilerplate/app/ \
  <app_name> -e py,rst,in
```

Can't use a url because we have several templates under one tgz (for now)
