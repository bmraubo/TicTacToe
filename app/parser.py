import argparse


class Parser:
    def create_parser():
        parser = argparse.ArgumentParser(
            prog="TicTacToe",
            description="Play a game of over-engineered TicTacToe locally or through a server",
        )
        parser.add_argument(
            "-server", help="start the game in server mode", action="store_true"
        )
        return parser
