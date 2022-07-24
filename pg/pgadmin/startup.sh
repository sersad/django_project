#!/bin/sh

# mkdir -p /var/lib/postgresql/data/
mount -t ext2 -o loop /pg_admin.img /var/lib/pgadmin
#USER pgadmin
/entrypoint.sh