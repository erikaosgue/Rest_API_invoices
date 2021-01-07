#!/bin/bash

echo "Creating database and user ..."

cat "create_database.sql" | sudo mysql

echo "Success!"