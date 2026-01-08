#!/usr/bin/env bash

echo "Refreshing DB"
echo "" > vrinda-cart.db

echo "Log is refreshed for good reference"
echo "" > ../app.log

echo "Applying schema to DB"
sqlite3 vrinda-cart.db < schema.sql
