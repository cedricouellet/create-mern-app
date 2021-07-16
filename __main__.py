#!/usr/bin/env python3

# TODO ADD NPM DEPENDENCIES AND LICENSE.TXT

import sys
import os
from typing import NoReturn


USAGE = 'usage: create-mern-api [-h] PATH'

HELP = f"""{USAGE}

MERN API Template Builder

positional arguments:
  PATH               the path in which to create the project
"""


def main(args: list[str]) -> None:
    if not args:
        exit_invalid_usage()

    if "-h" in args or '--help' in args:
        print(HELP)
        sys.exit(0)

    path = args[0]
    if path == '' or path.startswith('-'):
        exit_invalid_usage()

    try:
        if path != '.':
            os.mkdir(path)
            os.chdir(path)

        os.system('git init')
        os.system('npm init -y')

        with open('.gitignore', 'w') as f:
            f.write('/node_modules\nnode_modules/\n.env\n/.vscode\n/.idea\n')

        open('README.md', 'w').close()
        open('LICENSE.txt', 'w').close()
        open('.env', 'w').close()
        open('example.env', 'w').close()
        open('app.js', 'w').close()

        os.mkdir('controllers')
        os.mkdir('config')
        os.mkdir('models')
        os.mkdir('utils')
        os.mkdir('middlewares')
        os.mkdir('routes')

    except BaseException as ex:
        print('[create-mern-api] ', ex.__class__.__name__,
              ': ', ex, file=sys.stderr, sep='')


def exit_invalid_usage() -> NoReturn:
    print(USAGE)
    print('create-mern-api: error: The following arguments are required: PATH')
    sys.exit(1)


if __name__ == '__main__':
    main(sys.argv[1:])
