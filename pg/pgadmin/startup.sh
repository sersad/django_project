#!/bin/sh

# mkdir -p /var/lib/postgresql/data/
mount -t ext2 -o loop pgadmin.img /var/lib/pgadmin
#USER pgadmin
/entrypoint.sh