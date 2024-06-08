#!/bin/bash

echo "Watching $1 for changes"

fswatch -o "$1" | while read -r event; do
    mysql -u root < "$1"
done
