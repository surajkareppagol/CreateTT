from random import choice
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

    def create_actions_table(self, actions):
        """
        Create actions table.
        Usage: create_actions_table(actions)
        Return: Table()
        """

        actions_table = Table(box=box.SQUARE)
        actions.append("Empty")

        for i in range(1, len(actions) + 1):
            actions_table.add_column(str(i))

        actions_table.add_row(*(tuple(actions)))
        return actions_table

    def create_time_table_interactive(self, actions: list, times: list) -> None:
        """
        Create time table with user input.
        Usage: create_time_file_interactive(actions, times)
        Return: None
        """

        self.console.clear()

        selected_actions = []

        actions_table = self.create_actions_table(actions[:])

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

                        column_index -= 1
                        continue
                    elif int(action_index) > len(actions) + 1:
                        self.console.clear()
                        continue
                except ValueError:
                    self.console.clear()
                    continue

                selected_actions.append(
                    actions[int(action_index) - 1]
                    if int(action_index) <= len(actions)
                    else "Empty"
                )
                column_index += 1

                self.console.clear()

            self.table.add_row(times[row_index], *(selected_actions))
            selected_actions.clear()

            row_index += 1

            if row_index >= len(times):
                self.console.clear()
                break

    def build_custom_table(self, table_data) -> None:
        """
        Build custom table.
        Usage: build_custom_table(table_data)
        Return: None
        """

        self.table = Table(box=box.DOUBLE_EDGE, highlight=True)
        self.create_table()

        for key, value in table_data.items():
            self.table.add_row(key, *(tuple(value)))

    def format_action_string(self, string, color) -> str:
        """
        Build custom table.
        Usage: format_action_string(string, color)
        Return: str
        """

        return f"[bold {color}]{string}[/bold {color}]"

    def customize_table(self, actions, times) -> None:
        """
        Build and customize table.
        Usage: customize_table(actions, times)
        Return: None
        """

        current_selected_time = 0
        current_selected_action = 0

        table_data = {}

        actions_table = self.create_actions_table(actions[:])

        for time in times:
            table_data[time] = [choice(actions) for _ in range(self.columns)]

        table_data_copy = table_data.copy()

        while True:
            self.console.clear()
            self.console.print_panel(
                "[bold yellow]CreateTT[/bold yellow] - Time Table Builder"
            )

            self.console.print(
                "\nUse ([bold yellow]w, a, s, d, q[/bold yellow]) to select cell, and select [bold yellow]index[/bold yellow] to change cell value.\n"
            )

            for key, value in table_data_copy.items():
                table_data[key] = value[:]

            selected_string = table_data_copy[times[current_selected_time]][
                current_selected_action
            ]

            formatted_string = self.format_action_string(selected_string, "red")

            table_data[times[current_selected_time]][
                current_selected_action
            ] = formatted_string

            self.build_custom_table(table_data)
            self.console.print(self.table)
            self.console.print(actions_table)

            try:
                index = getch.getch()

                if index.isdigit() and int(index) <= len(actions) + 1:
                    table_data_copy[times[current_selected_time]][
                        current_selected_action
                    ] = (
                        actions[int(index) - 1]
                        if int(index) <= len(actions)
                        else "Empty"
                    )

                if index == "d" and current_selected_action < self.columns - 1:
                    current_selected_action += 1

                if index == "a" and current_selected_action > 0:
                    current_selected_action -= 1

                if index == "w" and current_selected_time > 0:
                    current_selected_time -= 1

                if index == "s" and current_selected_time < len(times) - 1:
                    current_selected_time += 1
            except ValueError:
                self.console.clear()
                continue

            if index == "q":
                self.console.clear()
                break
