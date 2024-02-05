from sys import argv
from sys import exit

from random import choice

from rich.console import Console
from rich.table import Table
from rich.terminal_theme import MONOKAI

console = Console(record=True)
table = Table(title="Time Table")

action_file_path = ""
time_file_path = ""

if len(argv) > 2:
    action_file_path = argv[1]
    time_file_path = argv[2]
else:
    console.print("[red bold]Provide path value.[/red bold]")
    exit(1)

columns = 7

if len(argv) > 3 and argv[3] == "-d" and argv[4]:
    columns = int(argv[4])


def create_table() -> None:
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

    table.add_column("Time", justify="center")

    for column in range(columns):
        table.add_column(week[column], justify="center")


def select_actions(actions) -> tuple:
    """
    Select actions randomly.
    Usage: select_actions(actions: list)
    Return: tuple
    """

    selected_actions = [choice(actions) for _ in range(columns)]
    return tuple(selected_actions)


def read_action_file(path: str) -> list:
    """
    Read action file.
    Usage: read_action_file(path: str)
    Return: list
    """

    with open(path) as file:
        data = file.readlines()
        # Step 2 : Create a python data structure from the data
        actions = [action.strip() for action in data]

    return actions


def read_time_file(path: str) -> list:
    """
    Read time file.
    Usage: read_time_file(path: str)
    Return: list
    """

    with open(path) as file:
        data = file.readlines()
        # Step 4 : Create a python data structure from the data
        times = [time.strip() for time in data]

    return times


def create_time_table(actions: list, times: list) -> list:
    """
    Create time table.
    Usage: create_time_file(actions: list, times: list)
    Return: list
    """

    for time in times:
        selected_actions = select_actions(actions)
        table.add_row(time, *(selected_actions))


create_table()

actions = read_action_file("./Actions.txt")
times = read_time_file("./Time.txt")

create_time_table(actions, times)

console.print(table)

console.save_html("Time Table.html", theme=MONOKAI)
console.save_svg("Time Table.svg", theme=MONOKAI)
