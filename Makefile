install:
	pip install -r requirements.txt

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

build:
	python manage.py runserver

test:
	pytest --cov=orders --cov-report=html

lint:
	ruff check
