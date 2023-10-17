#!/usr/bin/env sh
set -e

if [ "$MODE" = "production" ]; then
    echo "Running in production mode with SQL"
    if [ a = 1 ]; then
      echo "Cannot start application. Secrets not found"
      exit 1
    else
      echo "Injecting secrets"
      $( echo "$APP_ENV" | jq -r 'keys[] as $k | "export \($k)=\(.[$k])"' )
      touch .env
      echo "$APP_ENV" | jq -r 'keys[] as $k | "\($k)=\(.[$k])"' > .env
    fi
else
      if [ "$MODE" = "dev" ]; then
        if [ -f .env.docker.dev ]; then
          cat .env.docker.dev > .env
          export $(cat .env | xargs)
        else
          echo ".env.docker.dev file not found. Create .env.docker.ci file to continue"
          exit 1
        fi
     elif [ "$MODE" = "test" ]; then
        if [ -f .env.docker.ci ]; then
          cat .env.docker.ci > .env
          export $(cat .env | xargs)
        else
          echo ".env.docker.ci file not found. Create .env.docker.ci file to continue"
          exit 1
        fi
      else
         echo "Unknown mode"
         exit 1
     fi

fi

echo "Running database migration"
(python manage.py makemigrations) && (python manage.py migrate)
echo "Database migration completed"
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] && [ -n "$DJANGO_SUPERUSER_EMAIL" ]; then
    echo "Checking if Django superuser exists"

    # Check if superuser already exists
    EXISTS=$(echo "from django.contrib.auth import get_user_model; User = get_user_model(); print(User.objects.filter(email='$DJANGO_SUPERUSER_EMAIL').exists())" | python manage.py shell)

    if [ "$EXISTS" = "False" ]; then
        echo "Creating Django superuser"
        python manage.py createsuperuser --noinput --first_name $DJANGO_SUPERUSER_USERNAME --last_name $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL --role "admin"
        echo "from django.contrib.auth import get_user_model; User = get_user_model(); user = User.objects.get(email='$DJANGO_SUPERUSER_EMAIL'); user.set_password('$DJANGO_SUPERUSER_PASSWORD'); user.save()" | python manage.py shell
        echo "Django superuser created"
    else
        echo "Django superuser already exists. Skipping creation."
    fi
fi
#echo "Running Population Scripts"
#(python manage.py populate_onboarding) && (python manage.py simulate) && (python manage.py fix_dates) && (python manage.py employer_following)
#echo "Population Scripts completed"

if [ -z "$MODE" ] || [ "$MODE" != "test" ] || [ "$MODE" = "production" ]; then
  echo "Starting Nginx"
  (gunicorn tribaja.wsgi:application  --bind 0.0.0.0:8000) & nginx -g "daemon off;"
  echo "Stopped Nginx"
else
  echo "Executing command: $@"
  exec "$@"
fi