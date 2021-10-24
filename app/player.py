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
        # Defend against losing if necessary
        # Play first available move
        return self.__first_available_move()

    def __first_available_move(self):
        total_squares = list(range(1, self.board.highest_value + 1))
        for num in total_squares:
            if self.board.check_board_value(num) == str(num):
                return str(num)

    def check_for_winning_move(self):
        for key in self.board.arrangements:
            for element in self.board.arrangements[key]:
                count = 0
                for value in element:
                    if self.board.check_board_value(value) == self.marker:
                        count += 1
                if count == self.board.size - 1:
                    for value in element:
                        if self.board.check_board_value(value) != self.marker:
                            if self.board.validate_move(value):
                                return value
        return False
