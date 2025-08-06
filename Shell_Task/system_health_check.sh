#!/bin/bash

# Get current date
DATE=$(date '+%Y-%m-%d')

# Log running processes
LOG_FILE="process_log_$DATE.log"
ps aux > "$LOG_FILE"

# Check for high memory usage (>30%)
HIGH_MEM_LOG="high_mem_processes.log"
HIGH_MEM_PROCESSES=$(ps aux --sort=-%mem | awk '$4 > 30')

if [ ! -z "$HIGH_MEM_PROCESSES" ]; then
  echo "⚠️  Warning: Processes using more than 30% memory found!"
  echo "$HIGH_MEM_PROCESSES" >> "$HIGH_MEM_LOG"
fi

# Check disk space on root
DISK_USAGE=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')

if [ "$DISK_USAGE" -gt 80 ]; then
  echo "⚠️  Warning: Disk usage on / is above 80% (${DISK_USAGE}%)"
fi

# Summary
TOTAL_PROCESSES=$(ps aux | wc -l)
HIGH_MEM_COUNT=$(echo "$HIGH_MEM_PROCESSES" | wc -l)

echo "----- Summary -----"
echo "Total running processes      : $TOTAL_PROCESSES"
echo "Processes >30% memory usage  : $HIGH_MEM_COUNT"
echo "Disk usage on /              : ${DISK_USAGE}%"
