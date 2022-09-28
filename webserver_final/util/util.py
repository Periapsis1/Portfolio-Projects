import re

def camel_to_snake(s):
    """
    Convert a camel case string to snake case.
    """
    return '_'.join(
        [x.lower() for x in re.findall('[A-Z][^A-Z]*', s)]
    )

def snake_to_camel(s):
    """
    Convert a snake case string to camel case.
    """
    return ''.join(x.capitalize() for x in s.split('_'))