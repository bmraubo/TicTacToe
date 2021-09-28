class Info:
    def welcome_message():
        print("Welcome to Tic Tac Toe")

    def game_instructions():
        instructions = "Each square on the board have a value from 1-9. Select which square you would like to play by inputting the correct value when promoted."
        print(instructions)


class Board:
    def __init__(self):
        self.board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.markers = {"X": None, "O": None}
        self.players = []

    def create_player(self, name):
        self.players.append(Player(name))

    def assign_players(self):
        # assigns players to X and O
        self.markers["X"] = self.players[0]
        self.markers["O"] = self.players[1]


class Player:
    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    Info.welcome_message()
    Info.game_instructions()
