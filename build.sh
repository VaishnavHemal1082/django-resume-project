#!/usr/bin/env bash
set -o errexit

echo "========== BUILD STARTED =========="

pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate

echo "========== CREATING SUPERUSER =========="

python manage.py createsuperuser --noinput --verbosity 3

echo "========== BUILD FINISHED =========="