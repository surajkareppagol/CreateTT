class Error:
    def __init__(self) -> None:
        pass

    def help(self):
        return """
[bold green]CreateTT[/bold green]
[bold red]Usage[/bold red]: [white]python3 main.py [...args][/white]

[bold red]Args[/bold red]:
    [bold yellow]-h, --help[/bold yellow]     Show help
    [bold yellow]-a, --action[/bold yellow]   Action file
    [bold yellow]-t, --time[/bold yellow]     Time file
    [bold yellow]-d[/bold yellow]             Number of days
    [bold yellow]-s, --save[/bold yellow]     Save, (html, svg, txt)
        """

    def file(self):
        return "[red bold]Error[/red bold]: Provide path value."
