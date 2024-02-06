from sys import argv, exit

from args import ArgsParse
from console import Console
from error import Error
from file import File
from table import TimeTable

action_file_path = ""
time_file_path = ""

args = ArgsParse().parse()
error = Error()
table = TimeTable()
file = File()
console = Console()

if args.help or len(argv) == 1:
    console.print(error.help())
    exit(0)

if args.d:
    table.columns = int(args.d)

if args.action and args.time:
    table.create_table()

    action_file_path = args.action
    time_file_path = args.time

    actions = file.read_action_file(action_file_path)
    times = file.read_time_file(time_file_path)

    if args.interactive:
        table.create_time_table_interactive(actions, times)
    elif not args.interactive:
        table.create_time_table(actions, times)

else:
    console.print(error.file())
    exit(1)


console.print(table.table)

console.save(args.save)

console.print(
    f"\n[bold green]Success[/bold green]: Saved as [bold yellow]{args.save}[/bold yellow] file."
)
