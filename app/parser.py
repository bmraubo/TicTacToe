import argparse


class Parser:
    def run_parser(args):
        parser = argparse.ArgumentParser(
            prog="TicTacToe",
            description="Play a game of over-engineered TicTacToe locally or through a server",
        )
        parser.add_argument(
            "-server", help="start the game in server mode", action="store_true"
        )
        return parser.parse_args(args)
