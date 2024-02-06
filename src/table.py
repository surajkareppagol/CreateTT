from random import choice

from rich.table import Column, Table

from console import Console


class TimeTable:
    def __init__(self) -> None:
        """
        Init TimeTable()
        Usage: table = TimeTable()
        Return: None
        """

        self.table = Table(title="Time Table")
        self.columns = 7
        self.week = [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
        ]

    def create_table(self) -> None:
        """
        Create table from rich.
        Usage: create_table()
        Return: None
        """

        self.table.add_column("Time", justify="center")

        for column in range(self.columns):
            self.table.add_column(self.week[column], justify="center")

    def select_actions(self, actions) -> tuple:
        """
        Select actions randomly.
        Usage: select_actions(actions)
        Return: tuple
        """

        selected_actions = [choice(actions) for _ in range(self.columns)]
        return tuple(selected_actions)

    def create_time_table(self, actions: list, times: list) -> None:
        """
        Create time table.
        Usage: create_time_file(actions, times)
        Return: None
        """

        for time in times:
            selected_actions = self.select_actions(actions)
            self.table.add_row(time, *(selected_actions))

    def create_time_table_interactive(self, actions: list, times: list) -> None:
        """
        Create time table with user input.
        Usage: create_time_file_interactive()
        Return: None
        """

        console = Console()

        actions_table = Table(Column(header="Index"), Column(header="Action"))
        selected_actions = []

        for index, action in enumerate(actions, start=1):
            actions_table.add_row(str(index), action)

        time_index = 0

        while True:
            for index in range(self.columns):
                console.print(self.table)
                console.print(actions_table)

                console.print(
                    f"[bold yellow]Selected Actions[/bold yellow]: {', '.join(selected_actions)}\n"
                )

                action_index = console.input(
                    f"[bold white]Enter the [yellow]index[/yellow] of the action for [yellow]{self.week[index]}[/yellow] at [yellow]{times[time_index]}[/yellow][/bold white]: "
                )

                selected_actions.append(actions[int(action_index) - 1])
                console.clear()

            self.table.add_row(times[time_index], *(selected_actions))
            selected_actions.clear()

            time_index += 1

            if time_index >= len(times):
                console.clear()
                break
