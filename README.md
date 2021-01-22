## Django-PostgreSQL-Nginx-Docker-Letsencrypt.
 
Docker compose project base with Django, PosgreSQL, Nginx, Gunicorn and Certbot.<br>
Production and Development setup use gunicorn and nginx.<br>
Thanks to [django-docker-setup]("https://github.com/ermissa/django-docker-setup"). 

## Setup Project

Before starting to run this project ***docker*** and ***docker-compose*** should be installed on your computer.

## Installation

- Docker Installation: https://docs.docker.com/v17.12/install/
- Docker Compose Installation: https://docs.docker.com/compose/install/

## Configurations

- Copy project/env_sample to project.env. You can use .env as is for dev, but NOT for production.
```
cp ./project/env_sample project/.env
```

- Replace ***example.com*** domain names in *data/nginx/conf_ssl.d/nginx.conf* and *init-letsencrypt* folders with your domain name(s).

You can replace these names by using search and replace feature in your IDE or editor.

## Run Project

#### Run project for development or production without Certbot:

```
docker-compose up
```

#### Run project for production environment with Certbot

You can get your SSL certificates from Let's Encrypt by running *init-letsencrypt.sh* script. 


```
chmod u+x init-letsencrypt.sh && /bin/bash init-letsencrypt.sh
```

This script will also start your containers. In case you down your containers, you can restart them by following command,

```
docker-compose -f docker-compose.prod.ssl up
```