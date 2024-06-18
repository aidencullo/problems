#!/bin/bash

FILE_TO_MONITOR="query.sql"

fswatch -o "$FILE_TO_MONITOR" | while read -r event; do
    mysql -u root < query.sql
done
