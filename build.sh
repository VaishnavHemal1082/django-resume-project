#!/usr/bin/env bash
set -o errexit

echo "========== BUILD STARTED =========="

pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate

echo "========== CREATING SUPERUSER (if needed) =========="

python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
username = '$DJANGO_SUPERUSER_USERNAME'
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(
        username=username,
        email='$DJANGO_SUPERUSER_EMAIL',
        password='$DJANGO_SUPERUSER_PASSWORD'
    )
    print('Superuser created.')
else:
    print('Superuser already exists, skipping.')
"

echo "========== BUILD FINISHED =========="