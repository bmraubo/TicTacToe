class Player:
    def __init__(self, player_info):
        self.name = player_info[0]
        self.type = player_info[1]
        self.marker = player_info[2]


class HumanPlayer(Player):
    def __init__(self, player_info):
        Player.__init__(self, player_info)

    def get_player_move(self, player_move=None):
        if player_move == None:
            player_move = input(f"{self.name}, please enter move: ")
            return player_move
        else:
            return player_move


class ComputerPlayer(Player):
    def __init__(self, player_info):
        Player.__init__(self, player_info)

    def get_player_move(self, board):
        total_squares = list(range(1, board.highest_value + 1))
        for num in total_squares:
            if board.check_board_value(num) == str(num):
                return str(num)
