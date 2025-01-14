#!/bin/bash

# First, change to the script's directory
cd "$(dirname "$0")"

echo "Downloading Models..."

# Use simple arrays instead of associative arrays for better compatibility
urls=(
    "https://github.com/dnhkng/GlaDOS/releases/download/0.1/glados.onnx"
    "https://github.com/dnhkng/GlaDOS/releases/download/0.1/phomenizer_en.onnx"
)
files=(
    "glados/models/glados.onnx"
    "glados/models/phomenizer_en.onnx"
)

# Loop through arrays by index
for i in "${!urls[@]}"; do
    echo "Checking file: ${files[$i]}"
    if [ -f "${files[$i]}" ]; then
        echo "File ${files[$i]} already exists."
    else
        echo "File ${files[$i]} does not exist. Downloading..."
        mkdir -p "$(dirname "${files[$i]}")" # Create the directory if it doesn't exist
        curl -L "${urls[$i]}" --output "${files[$i]}"
        if [ -f "${files[$i]}" ]; then
            echo "Download successful."
        else
            echo "Download failed."
        fi
    fi
done

echo "Downloads Complete!"

# Keep the terminal window open to see any errors
echo "Press any key to close..."
read -n 1