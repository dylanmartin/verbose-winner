#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
NVFL_OVERSEER_HEARTBEAT_TIMEOUT=10 AUTHZ_FILE=$DIR/privilege.yml gunicorn -c $DIR/gunicorn.conf.py --keyfile $DIR/overseer.key --certfile $DIR/overseer.crt --ca-certs $DIR/rootCA.pem
