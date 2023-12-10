.PHONY: superuser
superuser:
	python manage.py createsuperuser

.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: migrations
migrations:
	python manage.py makemigrations

.PHONY: migrate
migrate:
	python manage.py migrate

.PHONY: shell
shell:
	python manage.py shell

.PHONY: dbshell
dbshell:
	python manage.py dbshell

.PHONY: run-server
run-server:
	python3 manage.py runserver 
