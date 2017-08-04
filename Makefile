check:
	@pep8 --statistics --show-source --show-pep8

test: check
	@pip install -r requirements_dev.txt
	@py.test maria/ --create-db --flakes --pep8

dev:
	@pip install --upgrade pip
	@pip install -r requirements_dev.txt
	@python maria/manage.py migrate
	@python maria/manage.py runserver 0.0.0.0:8000
	@echo "Running server in dev mode"

.PHONY: check test dev
