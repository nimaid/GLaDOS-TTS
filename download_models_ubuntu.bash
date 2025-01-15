#!/bin/bash

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

# Check if curl is installed
if ! command -v curl &> /dev/null; then
    echo "curl is not installed. Installing curl..."
    sudo apt-get update
    sudo apt-get install -y curl
fi

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