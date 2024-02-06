from rich.console import Console as RConsole
from rich.terminal_theme import MONOKAI


class Console:
    def __init__(self) -> None:
        """
        Init Console()
        Usage: console = Console()
        Return: None
        """

        self.console = RConsole(record=True)

    def print(self, string: str) -> None:
        """
        Print to the terminal.
        Usage: console.print(string)
        Return: None
        """

        self.console.print(string)

    def input(self, string: str) -> str:
        """
        Print to the terminal.
        Usage: console.print(str)
        Return: None
        """

        input_value = self.console.input(string)
        return input_value

    def clear(self) -> None:
        """
        Clear the terminal.
        Usage: console.clear()
        Return: None
        """

        self.console.clear()

    def save(self, format: str) -> None:
        """
        Save as SVG, HTML or TXT.
        Usage: console.save(format)
        Return: None
        """

        if format == "svg":
            self.console.save_svg("Time Table.svg", theme=MONOKAI)
        elif format == "html":
            self.console.save_html("Time Table.html", theme=MONOKAI)
        elif format == "txt":
            self.console.save_text("Time Table.txt")
