#!/bin/bash

FILE_TO_MONITOR="$1"

fswatch -o "$FILE_TO_MONITOR" | while read -r event; do
    mysql -u root < "$FILE_TO_MONITOR"
done
