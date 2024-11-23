#!/usr/bin/python3
'''
Command line wrapper to run `uv publish` with given arguments using
default credentials from your `~/.pypirc`.
'''
from __future__ import annotations

import argparse
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

    servers = config['distutils']['index-servers'].strip().split()
    opt = argparse.ArgumentParser(description=__doc__)
    opt.add_argument('--repository', '--repo', choices=servers,
                     default=servers[0],
                     help='Name of the repository to upload to (must match a '
                     f'repository in your {PYPIRC.name} file). '
                     'Default is "%(default)s".')

    args, rest = opt.parse_known_args()

    settings = config[args.repository]
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

    res = subprocess.run(['uv', 'publish'] + opts + rest)
    return res.returncode

if __name__ == '__main__':
    sys.exit(main())
