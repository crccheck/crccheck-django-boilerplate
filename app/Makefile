PROJECT=./example_project
MANAGE=python $(PROJECT)/manage.py

help:
	@echo "make commands:"
	@echo "  make help    - this help"
	@echo "  make clean   - remove temporary files in .gitignore"
	@echo "  make test    - run test suite"
	@echo "  make resetdb - drop and recreate the database"


clean:
	find . -name "*.pyc" -delete
	find . -name ".DS_Store" -delete
	rm -rf MANIFEST
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info


test:
	$(MANAGE) test {{ project_name }}


# as an alternative, you can reset your entire database with:
# python $(PROJECT)/manage.py reset_db --router=default --noinput
resetdb:
	$(MANAGE) sqlclear {{ project_name }} | $(MANAGE) dbshell
	$(MANAGE) syncdb --noinput


.PHONY: help clean test resetdb
