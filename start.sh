#!/bin/bash

# Run the main Python script
echo "Running LinPEAS..."
python3 callLinpeas.py

#Prompt user for input
read -p "Enter your input from 1 to 3: " user_input

echo "AI output..."
python3 ai.py "$user_input"

# Run the cleanup Python script
echo "Cleaning up LinPEAS files..."
python3 delete.py

echo "All tasks completed."
