from rich.console import Console
from rich.panel import Panel
from rich.terminal_theme import MONOKAI


class Terminal(Console):
    def __init__(self) -> None:
        """
        Init Console()
        Usage: console = Console()
        Return: None
        """
        super().__init__(record=True)

        self.help = """
[bold green]CreateTT[/bold green]
[bold red]Usage[/bold red]: [white]python3 main.py [...args][/white]

[bold red]Args[/bold red]:
    [bold yellow]-h, --help[/bold yellow]            Show help
    [bold yellow]-a, --action[/bold yellow]          Action file
    [bold yellow]-t, --time[/bold yellow]            Time file
    [bold yellow]-d[/bold yellow]                    Number of days
    [bold yellow]-s, --save[/bold yellow]            Save, (html, svg, txt)
    [bold yellow]-i, --interactive[/bold yellow]     Interactive mode
    [bold yellow]-c, --customize[/bold yellow]       Customize mode
        """

    def save_as(self, format: str) -> None:
        """
        Save as SVG, HTML or TXT.
        Usage: console.save(format)
        Return: None
        """

        if format == "svg":
            super().save_svg("Time Table.svg", theme=MONOKAI)
        if format == "html":
            super().save_html("Time Table.html", theme=MONOKAI)
        if format == "txt":
            super().save_text("Time Table.txt")

        super().print(
            f"\n[bold green]Success[/bold green]: Saved as [bold yellow]{format}[/bold yellow] file."
        )

    def print_panel(self, string: str) -> None:
        """
        Print panel from console.
        Usage: console.print_panel(string)
        Return: None
        """

        super().print(Panel(string))
