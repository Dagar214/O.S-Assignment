# Batch Processing Simulation
# OS Lab Assignment 4 – Task 1
# This script executes multiple Python files sequentially

import subprocess

# List of Python scripts to execute
scripts = ['script1.py', 'script2.py', 'script3.py']

print("Starting Batch Processing...\n")

for script in scripts:
    print(f"Executing {script}...")
    subprocess.call(['python3', script])
    print(f"{script} execution completed.\n")

print("Batch Processing Completed.")
