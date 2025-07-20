#!/usr/bin/env python3
import datetime
import subprocess
import re

def update_readme_timestamp(content, current_time):
    pattern = re.compile(r'Last updated: .*?\n', re.DOTALL)
    return pattern.sub(f'Last updated: {current_time}\n', content)

def update_pdf_links(content, current_time):
    patterns = [
        (r'\d{4}-\d{2}-\d{2}--\d{2}-\d{2}-\d{2}_Dissertation.pdf', f'{current_time}_Dissertation.pdf'),
        (r'\d{4}-\d{2}-\d{2}--\d{2}-\d{2}-\d{2}_Dissertation_keys.pdf', f'{current_time}_Dissertation_keys.pdf'),
        (r'\d{4}-\d{2}-\d{2}--\d{2}-\d{2}-\d{2}_Dissertation_diff.pdf', f'{current_time}_Dissertation_diff.pdf')
    ]
    for pattern, replacement in patterns:
        content = re.sub(pattern, replacement, content)
    return content

def update_main_tex_watermark(content, current_time):
    pattern = r'textbf\{(\d{4}-\d{2}-\d{2}--\d{2}-\d{2}-\d{2})\}\}'
    return re.sub(pattern, r'textbf{' + current_time + '}}', content)

def main():
    current_time = datetime.datetime.now().strftime('%Y-%m-%d--%H-%M-%S')

    with open('README.md', 'r') as file:
        readme_content = file.read()

    readme_content = update_readme_timestamp(readme_content, current_time)
    readme_content = update_pdf_links(readme_content, current_time)

    with open('README.md', 'w') as file:
        file.write(readme_content)

    with open('main.tex', 'r') as file:
        main_tex_content = file.read()

    main_tex_content = update_main_tex_watermark(main_tex_content, current_time)

    with open('main.tex', 'w') as file:
        file.write(main_tex_content)

    subprocess.run(['git', 'add', 'README.md'])
    subprocess.run(['git', 'add', 'main.tex'])

if __name__ == "__main__":
    main()