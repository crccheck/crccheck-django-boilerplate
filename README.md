## Quickstart

```bash
mkvirtualenv `basename $PWD`
pip install Django
# TODO move all this out
# http://www.just-one-liners.com/communication/45187
export DJ_NAME=<app name>
django-admin startproject $DJ_NAME . \
  --template=../crccheck-django-boilerplate/app/ \
  -e py,rst,in
\mv app_name $DJ_NAME
```
