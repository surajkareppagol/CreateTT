from rich.console import Console
from rich.terminal_theme import MONOKAI


class Terminal(Console):
    def __init__(self) -> None:
        """
        Init Console()
        Usage: console = Console()
        Return: None
        """
        super().__init__(record=True)

    def save_as(self, format: str) -> None:
        """
        Save as SVG, HTML or TXT.
        Usage: console.save(format)
        Return: None
        """

        if format == "svg":
            super().save_svg("Time Table.svg", theme=MONOKAI)
        elif format == "html":
            super().save_html("Time Table.html", theme=MONOKAI)
        elif format == "txt":
            super().save_text("Time Table.txt")
