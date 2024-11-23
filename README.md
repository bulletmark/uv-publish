## UV-PUBLISH - run `uv publish` using default credentials from `~/.pypirc`
[![PyPi](https://img.shields.io/pypi/v/uv-publish)](https://pypi.org/project/uv-publish/)

[`uv-publish`][uv-publish] is a simple command line wrapper to run [`uv
publish`][uv_publish] using your default configured Python [PyPi][pypi]
credentials from your [`~/.pypirc`][pypirc] file. Simply run
`uv-publish` instead of `uv publish` with any of the options and
arguments that `uv publish` normally accepts. `uv-publish` will read
your `~/.pypirc` and pass those credentials to `uv publish` as arguments
`--username`, `--password`, or `--token`, and `--publish-url`. Those
arguments are passed automatically at the start of the `uv publish`
command line so they can be overridden manually by later arguments if
required. 

By default, `uv-publish` uses the `pypi` server configuration from your `~/.pypirc`.
You can specify a different index server using the `--index`
parameter in either of these formats:
```bash
uv-publish --index=testpypi  # using equals sign
uv-publish --index testpypi  # using space
```
This allows you to easily switch between different package indexes
(e.g., PyPI and TestPyPI) configured in your `~/.pypirc` file.

Note that similar tools to push your Python packages to [PyPi][pypi]
such as [`twine`][twine], [`hatch`][hatch], and [`flit`][flit] recognise
the common [`~/.pypirc`][pypirc] file so this wrapper is created to
enable [`uv publish`][uv_publish] to do the same.

This utility has been developed and tested on Linux but should also work
on macOS and Windows although has not been tried on those platforms. The
latest documentation and code is available at
https://github.com/bulletmark/uv-publish.

## How to run

You are a [`uv`][uv] user so you should have `uv` installed. Just run
`uv-publish` as follows (`uv-publish` will get automatically installed
by [`uvx`][uvx] if you don't already have it):

```sh
$ uvx uv-publish [uv publish options]
```

E.g. if you use [`twine`][twine] to publish your package[s] and you
store your PyPi credentials in `~/.pypirc` then you can
swap to [`uv-publish`][uv-publish] by simply changing the command:

```sh
$ twine upload dist/*
```

to:

```sh
$ uvx uv-publish
```

For example, to publish to TestPyPI:
```sh
$ uvx uv-publish --index=testpypi
# or
$ uvx uv-publish --index testpypi
```

To publish to PyPI (default):
```sh
$ uvx uv-publish  # uses pypi by default
```

To upgrade:

```sh
$ uvx uv-publish@latest --help
```

To remove:

```sh
$ uv cache clean uv-publish
```

## License

Copyright (C) 2024 Mark Blakeney. This program is distributed under the
terms of the GNU General Public License. This program is free software:
you can redistribute it and/or modify it under the terms of the GNU
General Public License as published by the Free Software Foundation,
either version 3 of the License, or any later version. This program is
distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License at
<http://www.gnu.org/licenses/> for more details.

[uv-publish]: https://github.com/bulletmark/uv-publish
[uv]: https://docs.astral.sh/uv/
[uvx]: https://docs.astral.sh/uv/guides/tools/
[uv_publish]: https://docs.astral.sh/uv/guides/publish/
[twine]: https://twine.readthedocs.io/
[hatch]: https://hatch.pypa.io/
[flit]: https://flit.readthedocs.io/
[pypirc]: https://packaging.python.org/en/latest/specifications/pypirc/
[pypi]: https://pypi.org/

<!-- vim: se ai syn=markdown: -->
