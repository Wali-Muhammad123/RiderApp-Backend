# Dockerfile
FROM python:3.9-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

# install nginx
RUN apt-get update && apt-get install nginx curl jq -y --no-install-recommends gdal-bin
COPY nginx/nginx.conf /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

WORKDIR /app
COPY requirements.txt ./
# copy source and install dependencies

RUN pip install -r requirements.txt

ARG MODE=production
RUN ([ "$MODE" != "production" ] && pip install -r requirements_dev.txt) || echo "Production mode"
# Copy source
COPY . .
ENV MODE=${MODE}
RUN chmod +x /app/scripts/entrypoint.sh
# start server
EXPOSE 80
STOPSIGNAL SIGTERM
ENTRYPOINT [ "/app/scripts/entrypoint.sh" ]
