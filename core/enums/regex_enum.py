from enum import Enum


class RegexEnum(Enum):
    EMAIL = (
        r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
        [
            'email must contain "@" symbol',
            'email must have at least one character before "@"',
            'email must have a valid domain after "@" (e.g. example.com)',
            'email must have at least one dot (.) after the domain name',
            'email domain extension must be 2 to 6 characters long (e.g. .com, .co.uk)',
            'email can contain alphanumeric characters, periods (.), hyphens (-), and underscores (_)',
        ]
    )
    PASSWORD = (
        r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\d\s:])(\S){8,30}$',
        [
            'password must contain 1 number (0 - 9)',
            'password must contain min 1 uppercase letter',
            'password must contain min 1 lowercase letter',
            'password must contain min 1 alphanumeric character',
            'password min 8 max 30 characters without spaces',

        ]
    )

    def __init__(self, pattern: str, msg: str | list[str]) -> None:
        self.pattern = pattern
        self.msg = msg
