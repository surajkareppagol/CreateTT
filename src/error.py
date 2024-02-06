class Error:
    def __init__(self) -> None:
        """
        Init Error()
        Usage: error = Error()
        Return: None
        """
        pass

    def help(self) -> str:
        """
        Return help error string.
        Usage: error.help()
        Return: str
        """

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

    def file(self) -> str:
        """
        Return file error string.
        Usage: error.file()
        Return: str
        """
        return "[red bold]Error[/red bold]: Provide path value."
