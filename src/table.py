from random import choice

from rich.table import Table


class TimeTable:
    def __init__(self) -> None:
        self.table = Table(title="Time Table")
        self.columns = 7

    def create_table(self) -> None:
        """
        Create table from rich.
        Usage: create_table()
        Return: None
        """

        week = [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
        ]

        self.table.add_column("Time", justify="center")

        for column in range(self.columns):
            self.table.add_column(week[column], justify="center")

    def select_actions(self, actions) -> tuple:
        """
        Select actions randomly.
        Usage: select_actions(actions: list)
        Return: tuple
        """

        selected_actions = [choice(actions) for _ in range(self.columns)]
        return tuple(selected_actions)

    def create_time_table(self, actions: list, times: list) -> None:
        """
        Create time table.
        Usage: create_time_file(actions: list, times: list)
        Return: None
        """

        for time in times:
            selected_actions = self.select_actions(actions)
            self.table.add_row(time, *(selected_actions))
