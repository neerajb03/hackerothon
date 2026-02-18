#!/bin/bash

ARCHIVE_DEST="/tmp"
INTERVAL=60 

while true; do
    USAGE=$(df -h / | awk 'NR==2 {print $5}' | sed "s/%//")

    if (( USAGE >= 90 )); then
        echo "Disk usage at $USAGE%"

        TIMESTAMP=$(date +%Y%m%d_%H%M%S)
        

    fi

