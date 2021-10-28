from app.board import Board


class Player:
    def __init__(self, player_info):
        self.name = player_info[0]
        self.type = player_info[1]
        self.marker = player_info[2]

    def create_server_player_object(request_data):
        player_info = [
            request_data["player"]["name"],
            request_data["player"]["type"],
            request_data["player"]["marker"],
        ]
        return HumanPlayer(player_info)


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
        total_squares = list(range(1, self.board.highest_value + 1))
        for num in total_squares:
            if Board.check_board_value(self.board.board_data, num) == str(num):
                return str(num)
