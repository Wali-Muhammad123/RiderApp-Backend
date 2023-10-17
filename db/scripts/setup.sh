#!/bin/bash
set -e
POSTGRES="psql --username ${POSTGRES_USER}"

echo "Creating database role: rider-app with password $POSTGRES_PASSWORD"
$POSTGRES <<-EOSQL
CREATE USER rider_app WITH ENCRYPTED PASSWORD '$POSTGRES_PASSWORD';
CREATE DATABASE riderapp;
GRANT ALL PRIVILEGES ON DATABASE riderapp TO rider_app;
CREATE EXTENSION postgis;
EOSQL
echo "Created role: rider_app with password $POSTGRES_PASSWORD"