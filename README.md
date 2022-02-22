Load the files under ./ldap to the LDAP server before testing.

This repo contains Python scripts to test a runninig version of MOSIP.  

Modified for testing.



Script to start docker DB:
```#!/bin/sh
# Postgres 12 is probably higher for current MOSIP version.  Need to use
# lower version
# Run psql as 
# psql -h localhost -U postgres
# password: mosip
docker run --rm --name pg-docker -e POSTGRES_PASSWORD=mosip -d -p5432:5432 -v /home/puneet/docker/volumes/postgres:/var/lib/postgresql/data postgres:12```

