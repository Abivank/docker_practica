#!/bin/sh
cat /README.md
echo
exec docker-entrypoint.sh "$@"