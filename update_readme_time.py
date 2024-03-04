#!/usr/bin/env python3
import datetime
import subprocess
import re

# Get the current time
current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Retrieve the commit message and author
commit_message = subprocess.check_output(['git', 'log', '-1', '--pretty=%B']).decode('utf-8').strip()
commit_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('utf-8').strip()
author = subprocess.check_output(['git', 'log', '-1', '--pretty=%an']).decode('utf-8').strip()

# Read the existing content of README.md
with open('README.md', 'r') as file:
    content = file.read()

# Define a pattern to find the "Last updated" line
pattern = re.compile(r'Last updated: .*?\n', re.DOTALL)

# Replace the old "Last updated" line with the new one
timestamp_content = pattern.sub(f'Last updated: {current_time}\n', content)

# Define a pattern to find the "Commit hash" line
pattern = re.compile(r'Commit hash: .*?\n', re.DOTALL)

# Replace the old "Commit hash" line with the new one
hash_content = pattern.sub(f'Commit hash: {commit_hash}\n', timestamp_content)

# Define a pattern to find the "Author:" line
pattern = re.compile(r'Author: .*?\n', re.DOTALL)

# Replace the old "Author:" line with the new one
author_content = pattern.sub(f'Author: {author}\n', hash_content)

# Define a pattern to find the "Commit hash" line
pattern = re.compile(r'Commit message: .*?\n', re.DOTALL)

# Replace the old "Commit hash" line with the new one
msg_content = pattern.sub(f'Commit message: {commit_message}\n', author_content)

# Write the updated content back to README.md
with open('README.md', 'w') as file:
    file.write(msg_content)

# Add README.md to the staging area
subprocess.run(['git', 'add', 'README.md'])