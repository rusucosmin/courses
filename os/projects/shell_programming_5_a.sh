#!/bin/bash
ps aux | tail -n +2 | awk '{print $1}' | sort | uniq -c | sort -n -r
