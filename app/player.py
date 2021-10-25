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
    def __init__(self, player_info, board):
        Player.__init__(self, player_info)
        self.board = board

    def get_player_move(self):
        # If possible, play winning move
        winning_move = self.check_for_winning_move()
        if winning_move != False:
            return winning_move
        else:
            # Defend against losing if necessary
            # Play first available move
            return self.__first_available_move()

    def __first_available_move(self):
        possible_moves = list(range(1, self.board.highest_value + 1))
        for move in possible_moves:
            if self.board.check_board_value(str(move)) == str(move):
                return str(move)

    def check_for_winning_move(self):
        possible_moves = list(range(1, self.board.highest_value + 1))
        for move in possible_moves:
            simulated_board = self.board
            if not simulated_board.validate_move(move):
                continue
            simulated_board.board[str(move)] = self.marker
            if simulated_board.win_check(self.marker):
                return str(move)
            simulated_board.board[str(move)] = str(move)

        return False
