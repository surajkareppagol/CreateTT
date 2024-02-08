class Error:
    def __init__(self) -> None:
        """
        Init Error()
        Usage: error = Error()
        Return: None
        """

        self.file_error = "[red bold]Error[/red bold]: Provide path value."

        self.keyboard_interrupt_error = (
            "\n\n[red bold]Error[/red bold]: Pressed [bold red]CTRL + C[/bold red]."
        )

        self.file_not_found_error = "[red bold]Error[/red bold]: File Not Found."
