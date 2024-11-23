#!/usr/bin/python3
'''
Command line wrapper to run `uv publish` using default credentials from
`~/.pypirc`.
'''
from __future__ import annotations

import subprocess
import sys
from configparser import ConfigParser
from pathlib import Path

PYPIRC = Path.home() / '.pypirc'

DEFAULT_CONFIG = '''
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
repository = https://upload.pypi.org/legacy/

[testpypi]
repository = https://test.pypi.org/legacy/
'''

def main() -> int:
    # Manual parsing of --index parameter
    args = sys.argv[1:]
    index = 'pypi'  # default value
    
    # Handle --index=value format
    remaining_args = []
    for arg in args:
        if arg.startswith('--index='):
            index = arg.split('=', 1)[1]
        elif arg == '--index' and remaining_args and not remaining_args[-1].startswith('-'):
            index = remaining_args.pop()
        else:
            remaining_args.append(arg)

    config = ConfigParser()
    config.read_string(DEFAULT_CONFIG)
    if PYPIRC.exists():
        config.read(PYPIRC)

    if index not in config:
        print(f"Error: Index '{index}' not found in configuration.")
        print("Available indexes:", ", ".join(name for name in config.sections() if name != 'distutils'))
        return 1

    settings = config[index]
    opts = []
    if user := settings.get('username'):
        password = settings.get('password')

        if '__token__' in user:
            if password:
                opts.append(f'--token={password}')
        else:
            opts.append(f'--username={user}')
            if password:
                opts.append(f'--password={password}')

        url = settings.get('repository')
        if url and opts:
            opts.append(f'--publish-url={url}')

    res = subprocess.run(['uv', 'publish'] + opts + remaining_args)
    return res.returncode

if __name__ == '__main__':
    sys.exit(main())
