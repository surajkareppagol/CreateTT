from sys import argv, exit

from args import ArgsParse
from console import Terminal
from error import Error
from file import File
from table import TimeTable

args = ArgsParse().parse()
error = Error()
table = TimeTable()
file = File()
console = Terminal()

if args.help or len(argv) == 1:
    console.print(console.help)
    exit(0)

if args.d:
    table.set_columns(int(args.d))

if args.action and args.time:
    table.create_table()

    try:
        actions = file.read_action_file(args.action)
        times = file.read_time_file(args.time)
        if args.interactive:
            table.create_time_table_interactive(actions, times)
        elif not args.interactive:
            table.create_time_table(actions, times)
    except KeyboardInterrupt:
        console.print(error.keyboard_interrupt_error)
        exit(1)
    except FileNotFoundError:
        console.print(error.file_not_found_error)
        exit(1)

else:
    console.print(error.file_error)
    exit(1)


console.print(table.table)

console.save_as(args.save)
