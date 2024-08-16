#!/bin/sh
python manage.py makemigrations --noinput
python manage.py migrate --noinput

if [ $DEBUG = "True" ]
then
  # For local development
  python manage.py runserver 0.0.0.0:8000
else
  # For deployment
  python manage.py collectstatic --noinput
  gunicorn chessapi.wsgi:application --bind 0.0.0.0:8000
fi
