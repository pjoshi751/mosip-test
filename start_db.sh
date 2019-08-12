#!/bin/sh
# Postgres 12 is probably higher for current MOSIP version.  Need to use
# lower version
# Run psql as 
# psql -h localhost -U postgres
# password: mosip
docker run --rm --name pg-docker -e POSTGRES_PASSWORD=mosip -d -p5432:5432 -v /home/puneet/docker/volumes/postgres:/var/lib/postgresql/data postgres:12
