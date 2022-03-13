import re

from json import dumps as _json_dumps

SNAKE_CASE_RE_1 = re.compile(r"(.)([A-Z][a-z]+)")
SNAKE_CASE_RE_2 = re.compile(r"([a-z0-9])([A-Z])")


def snake_case(string):
    """Convert a string from PascalCase or camelCase to snake_case."""
    string = SNAKE_CASE_RE_1.sub(r"\1_\2", string)
    string = SNAKE_CASE_RE_2.sub(r"\1_\2", string)

    return string.lower()


def camel_case(string):
    """Convert a string from snake_case to camelCase."""
    return string[0] + string.title().replace("_", "")[1:]


def pascal_case(string):
    """Convert a string from snake_case to PascalCase."""
    return string.title().replace("_", "")


def lower_case_no_underscore(string):
    """Convert a string from snake_case to lowercase with no underscore."""
    return string.replace("_", "").lower()


def json(obj):
    """Convert object to JSON."""
    return _json_dumps(obj, separators=(",", ":"), check_circular=False)
