VERSION=0.0.0

PROJECT=./example_project
MANAGE=python $(PROJECT)/manage.py


help:
	@echo "make commands:"
	@echo "  make help    - this help"
	@echo "  make clean   - remove temporary files in .gitignore"
	@echo "  make test    - run test suite"
	@echo "  make release - drop and recreate the database"


clean:
	find . -name "*.pyc" -delete
	find . -name ".DS_Store" -delete
	rm -rf *.egg
	rm -rf *.egg-info
	rm -rf __pycache__
	rm -rf build
	rm -rf dist
	rm -rf MANIFEST

test:
	$(MANAGE) test {{ project_name }}


# as an alternative, you can reset your entire database with:
# python $(PROJECT)/manage.py reset_db --router=default --noinput
resetdb:
	$(MANAGE) sqlclear {{ project_name }} | $(MANAGE) dbshell
	$(MANAGE) syncdb --noinput


.PHONY: help clean test resetdb


# Release Instructions:
#
# 1. bump version number at the top of this file
# 2. `make release`
#
# If this doesn't work, make sure you have wheels installed:
#     pip install wheel
release:
	@sed -i -r /version/s/[0-9.]+/$(VERSION)/ setup.py
	@git commit -am "bump version to v$(VERSION)"
	@git tag v$(VERSION)
	python setup.py sdist bdist_wheel upload
