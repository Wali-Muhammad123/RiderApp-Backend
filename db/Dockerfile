# Use the official PostgreSQL image as a parent image
FROM postgres:14
# Optionally set environment variables
ENV POSTGIS_VERSION 3

# Copy the setup script
COPY ./scripts/setup.sh /docker-entrypoint-initdb.d/setup.sh

# Update the package list, install the PostGIS extension, and clean the cache
RUN apt-get update \
    && apt-get install -y postgresql-14-postgis-${POSTGIS_VERSION} \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && chmod +x /docker-entrypoint-initdb.d/setup.sh
