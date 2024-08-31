#!/bin/sh

if [ "$DBSCHEMA" = "mysql+mysqlconnector" ]
then
    echo "Waiting for MySQL..."

    while ! nc -z "$DBHOST" "$DBPORT"; do
      sleep 0.1
    done

    echo "MySQL started"
fi

echo "Running migrations"
alembic -c /app/alembic.ini upgrade head

echo "Starting main application"
exec "$@"