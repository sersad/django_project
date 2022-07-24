#!/bin/sh

# mkdir -p /var/lib/postgresql/data/
mount -t ext2 -o loop /pg_data.img /var/lib/postgresql/data/
docker-entrypoint.sh postgres