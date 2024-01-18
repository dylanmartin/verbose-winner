#!/bin/bash

# This script will launch other scripts from different directories concurrently

# Define an array of directories
directories=("Server" "Site1" "Site2" "Admin")

# Loop through each directory and execute the launch.sh script in the background
for dir in "${directories[@]}"; do
    (
        echo "Launching script in $dir"
        cd "$dir" && ./launch.sh &
    ) || {
        echo "Failed to execute script in $dir"
    }
done

# Wait for all background processes to finish
wait

echo "All scripts have been launched."
