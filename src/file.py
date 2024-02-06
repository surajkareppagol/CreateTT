class File:
    def __init__(self) -> None:
        pass

    def read_action_file(self, path: str) -> list:
        """
        Read action file.
        Usage: read_action_file(path: str)
        Return: list
        """

        with open(path) as file:
            data = file.readlines()
            actions = [action.strip() for action in data]

        return actions

    def read_time_file(self, path: str) -> list:
        """
        Read time file.
        Usage: read_time_file(path: str)
        Return: list
        """

        with open(path) as file:
            data = file.readlines()
            times = [time.strip() for time in data]

        return times
