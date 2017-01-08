.PHONY: run

run:
	python manage.py runserver

clean_pyc:
	find . -name \*.pyc -delete
	find . -name \*.pyo -delete

celery:
	celery -A api.celery_app worker -B -l INFO
