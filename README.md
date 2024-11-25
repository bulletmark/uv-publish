## UV-PUBLISH - run `uv publish` using credentials from your `~/.pypirc`
[![PyPi](https://img.shields.io/pypi/v/uv-publish)][uv-publish-py]

[`uv-publish`][uv-publish] is a simple command line wrapper to run [`uv
publish`][uv_publish] using your configured Python [PyPi][pypi]
credentials from your [`~/.pypirc`][pypirc] file. Simply run
`uv-publish` instead of `uv publish` with any of the options and
arguments that `uv publish` normally accepts. `uv-publish` will read
your `~/.pypirc` and pass those credentials to `uv publish` as arguments
`--username`, `--password`, or `--token`, and `--publish-url`. Those
arguments are passed automatically at the start of the `uv publish`
command line so they can be overridden manually by later arguments if
required. 

Note that similar tools to push your Python packages to [PyPi][pypi]
such as [`twine`][twine], [`hatch`][hatch], and [`flit`][flit] recognise
the common [`~/.pypirc`][pypirc] file so this wrapper is created to
enable [`uv publish`][uv_publish] to do the same.

By default `uv-publish` will use the first repository in your
`~/.pypirc` file (defaulting to `pypi` if the file does not exist). You
can specify the repository to use from your `~./pypirc` file with the
`--repository` (or `--repo`) option. This is the only option that
`uv-publish` accepts itself, all other options and arguments are passed
directly to `uv publish`. Note that `--repository` is the same switch
that `twine` and `flit` accept, and `--repo` is the same switch that
`hatch` accepts, so both are supported by `uv-publish`.

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

To upgrade:

```sh
$ uvx uv-publish@latest --help
```

To remove:

```sh
$ uv cache clean uv-publish
```

Of course `uv-publish` is available from [PyPi][uv-publish-py] so you
can choose to install it using [`pipx`][pipx] or [`pipxu`][pipxu] or
[`uv tool`][uvtool] if you prefer a traditional approach.

## Usage

Type `uv-publish -h` to view the usage summary:

```
usage: uv-publish [-h] [--repository {pypi,testpypi}]

Command line wrapper to run `uv publish` using default credentials from your
`~/.pypirc`. All extra arguments supplied on the command line are passed to
`uv publish`.

options:
  -h, --help            show this help message and exit
  --repository {pypi,testpypi}, --repo {pypi,testpypi}
                        Name of the repository to upload to (must match a
                        repository in your .pypirc file). Default is "pypi".
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
[uv-publish-py]: https://pypi.org/project/uv-publish/
[pipx]: https://github.com/pypa/pipx
[pipxu]: https://github.com/bulletmark/pipxu
[uvtool]: https://docs.astral.sh/uv/guides/tools/#installing-tools

<!-- vim: se ai syn=markdown: -->
