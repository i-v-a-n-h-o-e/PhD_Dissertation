#!/usr/bin/env python3
import datetime
import subprocess
import re

#debag hook
print("Pre-commit hook python script have been run")

# Get the current time
current_time = datetime.datetime.now().strftime('%Y-%m-%d--%H-%M-%S')

# Read the existing content of README.md
with open('README.md', 'r') as file:
    content = file.read()

# Define a pattern to find the "Last updated" line
pattern = re.compile(r'Last updated: .*?\n', re.DOTALL)

# Replace the old "Last updated" line with the new one
timestamp_content = pattern.sub(f'Last updated: {current_time}\n', content)

# Define a pattern to find the link to YYYY-MM-DD--HH-MM-SS_Dissertation.pdf
pattern = re.compile(r'\d{4}-\d{2}-\d{2}--\d{2}-\d{2}-\d{2}_Dissertation.pdf')

# Replace the old "Last updated" line with the new one
filename_content = pattern.sub(f'{current_time}_Dissertation.pdf', timestamp_content)

# Write the updated content back to README.md
with open('README.md', 'w') as file:
    file.write(filename_content)

with open('main.tex', 'r') as file:
    content = file.read()

# Define a pattern to find the watermark [YYYY-MM-DD--HH-MM-SS]
pattern = r'textbf\{(\d{4}-\d{2}-\d{2}--\d{2}-\d{2}-\d{2})\}\}'

# Replace the old "Last updated" line with the new one
filename_content = re.sub(pattern, r'textbf{' + current_time + '}}', content)

with open('main.tex', 'w') as file:
    file.write(filename_content)


# Add README.md and main.tex to the staging area
subprocess.run(['git', 'add', 'README.md'])
subprocess.run(['git', 'add', 'main.tex'])