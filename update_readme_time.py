#!/usr/bin/env python3
import datetime
import subprocess

# Get the current time
current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Retrieve the commit message and author
commit_message = subprocess.check_output(['git', 'log', '-1', '--pretty=%B']).decode('utf-8').strip()
author = subprocess.check_output(['git', 'log', '-1', '--pretty=%an']).decode('utf-8').strip()

# Append the current time, commit message, and author to README.md
with open('README.md', 'a') as file:
    file.write(f'\n\nLast updated: {current_time}\nCommit message: {commit_message}\nAuthor: {author}\n')

# Add README.md to the staging area
subprocess.run(['git', 'add', 'README.md'])

