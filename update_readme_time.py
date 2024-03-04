#!/usr/bin/env python3
import datetime
import subprocess

# Get the current time
current_time = datetime.datetime.now().strftime('%Y-%m-%d--%H-%M-%S')
print(current_time)

# Append the current time to README.md
with open('README.md', 'a') as file:
    file.write(f'\n\nLast updated: {current_time}\n')

# Add README.md to the staging area
subprocess.run(['git', 'add', 'README.md'])
