MANAGE=python manage.py


help:
	@echo "Help:"
	@echo "--------------------------------------------------"
	@echo "clean    remove temporary files"
	@echo "test     run test suite"
	@echo "resetdb  delete and recreate the database"

clean:
	rm -rf MANIFEST
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	find . -name "*.pyc" -delete
	find . -name ".DS_Store" -delete

test:
	ENVIRONMENT=test $(MANAGE) test

resetdb:
	$(MANAGE) reset_db --noinput
	$(MANAGE) migrate --noinput
