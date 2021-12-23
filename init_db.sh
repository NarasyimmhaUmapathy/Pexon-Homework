#!/bin/bash
INSTANCE_NAME="postgres-nara"
PG_PASS="postgres"
PG_IMAGE="postgres"

# Pull image
docker pull $PG_IMAGE

# Run image instance in detached mode
docker run --name $INSTANCE_NAME -e POSTGRES_PASSWORD=$PG_PASS -d $PG_IMAGE
python create_table.py