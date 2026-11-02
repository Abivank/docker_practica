#!/bin/sh
cat /README.md
exec docker-entrypoint.sh "$@"
