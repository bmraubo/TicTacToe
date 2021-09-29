class UserInterface:
    def welcome_message():
        print("Welcome to Tic Tac Toe")

    def game_instructions():
        instructions = "Each square on the board have a value from 1-9. Select which square you would like to play by inputting the correct value when promoted."
        print(instructions)

    def get_player_info():
        player_list = []
        while len(player_list) != 2:
            player_name = input(f"Enter Player {len(player_list)+1} Name: ")
            player_type = "human"
            player_list.append([player_name, player_type])
        return player_list


class TicTacToe:
    def __init__(self):
        self.board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        self.markers = {}
        self.players = []

    def create_players(self, players):
        for player in players:
            self.players.append(Player(player))

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

    def validate_player_move(self, player_move):
        try:
            player_move = int(player_move)
            if player_move < 1 or player_move > 9:
                print(f"{player_move} is not between 1 and 9")
                return False
            elif str(player_move) != (
                self.board[(player_move - 1) // 3][(player_move - 1) % 3]
            ):
                print(f"{player_move} has already been played")
                return False
            else:
                return True
        except ValueError:
            print(f"Value Error: {player_move} is not between 1-9")
            return False

    def play_game(self):
        for player in self.players:
            valid_move = False
            while valid_move == False:
                player_move = input(f"{player.name}, please enter move: ")
                valid_move = self.validate_player_move(player_move)
            self.make_move(player, int(player_move))
            self.draw_board()


class Player:
    def __init__(self, player_info):
        self.name = player_info[0]
        self.type = player_info[1]


if __name__ == "__main__":
    UserInterface.welcome_message()
    UserInterface.game_instructions()
    game = TicTacToe()
    player_list = UserInterface.get_player_info()
    game.create_players(player_list)
    game.assign_players()
    game.draw_board()
    game.play_game()
