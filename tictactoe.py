class Info:
    def welcome_message():
        print("Welcome to Tic Tac Toe")

    def game_instructions():
        instructions = "Each square on the board have a value from 1-9. Select which square you would like to play by inputting the correct value when promoted."
        print(instructions)


class TicTacToe:
    def __init__(self):
        self.board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        self.markers = {}
        self.players = []

    def create_player(self, name, type):
        self.players.append(Player(name, type))

    def assign_players(self):
        # assigns players to X and O
        self.markers[self.players[0]] = "X"
        self.markers[self.players[1]] = "O"

    def draw_board(self):
        # draws the current board state
        divider = "+---+---+---+"
        print(divider)
        print(f"| {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]} |")
        print(divider)
        print(f"| {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]} |")
        print(divider)
        print(f"| {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]} |")
        print(divider)

    def make_move(self, player, move):
        self.board[(move - 1) // 3][(move - 1) % 3] = self.markers[player]


class Player:
    def __init__(self, name, type):
        self.name = name
        self.type = type


if __name__ == "__main__":
    Info.welcome_message()
    Info.game_instructions()
