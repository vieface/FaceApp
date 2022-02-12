#!/usr/bin/env bash
while true
do
    python3 run.py --video_src 1
    echo "exitcode: $?"
    echo "Auto restart on failure"
    time=$(date +"%T %d-%m-%Y")
    echo "${time}"
    echo ""
    sleep 5s
done
