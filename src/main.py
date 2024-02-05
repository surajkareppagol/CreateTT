from sys import argv
from sys import exit

import argparse

from random import choice

from rich.console import Console
from rich.table import Table
from rich.terminal_theme import MONOKAI

console = Console(record=True)
table = Table(title="Time Table")

action_file_path = ""
time_file_path = ""

if "-h" in argv or "--help" in argv:
    console.print(
        """
[bold green]CreateTT[/bold green]
[bold red]Usage[/bold red]: [white]python3 main.py [...args][/white]

[bold red]Args[/bold red]:
    [bold yellow]-h, --help[/bold yellow]     Show help
    [bold yellow]-a, --action[/bold yellow]   Action file
    [bold yellow]-t, --time[/bold yellow]     Time file
    [bold yellow]-d[/bold yellow]             Number of days
    [bold yellow]-s, --save[/bold yellow]     Save, (html, svg, txt)
        """
    )
    exit(0)


parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("-a", "--action")
parser.add_argument("-t", "--time")
parser.add_argument("-d")
parser.add_argument("-s", "--save")

args = parser.parse_args()

if args.action and args.time:
    action_file_path = args.action
    time_file_path = args.time
else:
    console.print("[red bold]Provide path value.[/red bold]")
    exit(1)

columns = 7

if args.d:
    columns = int(args.d)


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

actions = read_action_file(action_file_path)
times = read_time_file(time_file_path)

create_time_table(actions, times)

console.print(table)

if args.save:
    if args.save == "svg":
        console.save_svg("Time Table.svg", theme=MONOKAI)
    elif args.save == "html":
        console.save_html("Time Table.html", theme=MONOKAI)
    elif args.save == "txt":
        console.save_text("Time Table.txt")
