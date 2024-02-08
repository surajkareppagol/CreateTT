import argparse


class ArgsParse:
    def __init__(self) -> None:
        """
        Init ArgsParse()
        Usage: args = ArgsParse()
        Return: None
        """

        self.parser = argparse.ArgumentParser(add_help=False)

    def parse(self):
        """
        Parse arguments.
        Usage: ArgsParse.parse()
        Return: NameSpace
        """

        self.parser.add_argument("-a", "--action")
        self.parser.add_argument("-t", "--time")
        self.parser.add_argument("-d")
        self.parser.add_argument("-s", "--save", default="svg")
        self.parser.add_argument("-i", "--interactive", action="store_true")
        self.parser.add_argument("-c", "--customize", action="store_true")
        self.parser.add_argument("-h", "--help", action="store_true")

        self.args = self.parser.parse_args()

        return self.args
