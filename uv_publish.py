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
    config = ConfigParser()
    config.read_string(DEFAULT_CONFIG)
    if PYPIRC.exists():
        config.read(PYPIRC)

    server = config['distutils']['index-servers'].strip().split()[0]
    settings = config[server]
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

    res = subprocess.run(['uv', 'publish'] + opts + sys.argv[1:])
    return res.returncode

if __name__ == '__main__':
    sys.exit(main())
