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

if args.action and args.time:
    action_file_path = args.action
    time_file_path = args.time
else:
    console.print(error.file())
    exit(1)

if args.d:
    table.columns = int(args.d)

if not args.interactive:
    table.create_table()
    actions = file.read_action_file(action_file_path)
    times = file.read_time_file(time_file_path)
    table.create_time_table(actions, times)

console.print(table.table)

console.save(args.save)
