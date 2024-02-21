import getch


def get_key(key):
    """
    Get key name.
    Usage: get_key(key)
    Return: str
    """

    if key == "\033":
        getch.getch()
        arrow = getch.getch()

        keys = ["up", "down", "right", "left"]

        if arrow in "ABCD":
            return keys[ord(arrow) - 65]


def read_file(path: str) -> list:
    """
    Read time file.
    Usage: read_time_file(path)
    Return: list
    """

    with open(path) as file:
        data = [line.strip() for line in file.readlines()]

    return data
