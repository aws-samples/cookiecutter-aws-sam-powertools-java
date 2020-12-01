import re
import sys

TERMINATOR = "\x1b[0m"
INFO = "\x1b[1;33m [INFO]: "
SUCCESS = "\x1b[1;32m [SUCCESS]: "
HINT = "\x1b[3;33m"
FAIL = "\033[91m [ERROR]"

PROJECT_SLUG_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

project_slug = '{{ cookiecutter.project_slug }}'

if not re.match(PROJECT_SLUG_REGEX, project_slug):
    print(FAIL + '"%s" is not a valid project_slug because does not match the RegEx: ^[_a-zA-Z][_a-zA-Z0-9]+$ ' % project_slug + TERMINATOR)

    # exits with status 1 to indicate failure
    sys.exit(1)
