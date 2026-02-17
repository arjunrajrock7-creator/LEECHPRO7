#!/bin/bash

# Fetch the latest tracker list
echo "📥 Fetching tracker list..."
tracker_list=$(curl -Ns https://ngosang.github.io/trackerslist/trackers_all_http.txt | awk '$0' | tr '\n\n' ',')

# Start aria2 with the config file and append trackers
echo "🚀 Starting Aria2 Daemon..."
aria2c --conf-path=aria2.conf --bt-tracker="[$tracker_list]"
