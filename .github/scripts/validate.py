#!/usr/bin/env python3
import json, sys, os

def main():
    try:
        with open('guides.json', 'r') as f:
            guides = json.load(f)
    except Exception as e:
        print(f'ERROR: Could not load guides.json: {e}')
        sys.exit(1)

    errors = []
    for i, g in enumerate(guides):
        slug = g.get('slug', '')
        html_file = f'{slug}.html'
        if not os.path.isfile(html_file):
            errors.append(f'guides.json[{i}] "{slug}": missing file "{html_file}"')

    if errors:
        for e in errors:
            print(f'  {e}')
        print(f'{len(errors)} error(s) found.')
        sys.exit(1)
    else:
        print(f'OK: {len(guides)} guides validated.')
        sys.exit(0)

if __name__ == '__main__':
    main()
