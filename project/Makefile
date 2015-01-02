MANAGE=python manage.py


help:
	@echo "make commands:"
	@echo "  make help    - this help"
	@echo "  make clean   - remove temporary files"
	@echo "  make test    - run test suite"
	@echo "  make resetdb - delete and recreate the database"


clean:
	find . -name "*.pyc" -delete
	find . -name ".DS_Store" -delete
	rm -rf MANIFEST
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info


test:
	ENVIRONMENT=test $(MANAGE) test


resetdb:
	$(MANAGE) reset_db --noinput
	$(MANAGE) migrate --noinput
