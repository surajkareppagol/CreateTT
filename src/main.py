from sys import argv, exit

from rich.console import Console
from rich.terminal_theme import MONOKAI

from args import ArgsParse
from error import Error
from file import File
from table import TimeTable

console = Console(record=True)

action_file_path = ""
time_file_path = ""

args = ArgsParse().parse()
error = Error()
table = TimeTable()
file = File()

if args.help or len(argv) == 1:
    console.print(error.help())
    exit(0)

if args.action and args.time:
    action_file_path = args.action
    time_file_path = args.time
else:
    console.print(error.file())
    exit(1)

if args.d:
    table.columns = int(args.d)

table.create_table()

actions = file.read_action_file(action_file_path)
times = file.read_time_file(time_file_path)

table.create_time_table(actions, times)

console.print(table.table)

if args.save:
    if args.save == "svg":
        console.save_svg("Time Table.svg", theme=MONOKAI)
    elif args.save == "html":
        console.save_html("Time Table.html", theme=MONOKAI)
    elif args.save == "txt":
        console.save_text("Time Table.txt")
