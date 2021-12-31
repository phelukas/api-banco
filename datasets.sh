#!/bin/bash
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata banco_dataset.json
python manage.py loaddata pessoa_dataset.json
python manage.py loaddata cliente_dataset.json
python manage.py runserver 0.0.0.0:8000
