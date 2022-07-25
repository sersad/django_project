#!/bin/sh

mount -t ext2 -o loop /pgadmin.img /var/lib/pgadmin
/entrypoint.sh