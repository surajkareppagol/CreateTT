from random import choice
from sys import exit
from time import sleep

import getch
from rich import box
from rich.table import Column, Table

from console import Terminal


class TimeTable:
    def __init__(self) -> None:
        """
        Init TimeTable()
        Usage: table = TimeTable()
        Return: None
        """

        self.table = Table(box=box.DOUBLE_EDGE, highlight=True)
        self.columns = 7
        self.week = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]

        self.console = Terminal()

    def set_columns(self, columns: int) -> None:
        if columns > 7:
            self.columns = 7
        elif columns < 1:
            self.columns = 1
        else:
            self.columns = columns

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

        self.console.clear()

        self.console.print_panel(
            "[bold yellow]CreateTT[/bold yellow] - Time Table Builder"
        )

        for time in times:
            selected_actions = self.select_actions(actions)
            self.table.add_row(time, *(selected_actions))

    def create_time_table_interactive(self, actions: list, times: list) -> None:
        """
        Create time table with user input.
        Usage: create_time_file_interactive(actions, times)
        Return: None
        """

        self.console.clear()

        actions_table = Table(Column(header="Index"), Column(header="Action"))
        selected_actions = []

        for index, action in enumerate(actions, start=1):
            actions_table.add_row(str(index), action)

        row_index = 0

        while True:
            column_index = 0
            while column_index < self.columns:
                self.console.print_panel(
                    "[bold yellow]CreateTT[/bold yellow] - Time Table Builder"
                )
                self.console.print(self.table)
                self.console.print(actions_table)

                self.console.print(
                    f"[bold yellow]Selected Actions[/bold yellow]: {', '.join(selected_actions)}\n"
                )

                self.console.print(
                    f"[bold white]Enter the [yellow]index[/yellow] (or [yellow]b[/yellow]) of the action for [yellow]{self.week[column_index]}[/yellow] at [yellow]{times[row_index]}[/yellow][/bold white]: ",
                    end="",
                )

                try:
                    action_index = getch.getche()
                    sleep(0.1)

                    if action_index == "b" and len(selected_actions) > 0:
                        selected_actions.pop()
                        self.console.clear()
                        continue
                    elif int(action_index) > len(actions):
                        self.console.clear()
                        continue
                except ValueError:
                    self.console.clear()
                    continue

                selected_actions.append(actions[int(action_index) - 1])
                column_index += 1

                self.console.clear()

            self.table.add_row(times[row_index], *(selected_actions))
            selected_actions.clear()

            row_index += 1

            if row_index >= len(times):
                self.console.clear()
                break
