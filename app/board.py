from app.logic import MoveLogic
from app.util import Utilities


class Board:
    def __init__(
        self,
        board_data={},
        size=None,
        highest_value=None,
        arrangements=None,
        winner=None,
        moves_made=0,
    ):
        self.board_data = board_data
        self.size = size
        self.highest_value = highest_value
        self.arrangements = arrangements
        self.winner = winner
        self.moves_made = moves_made

    def create_board(self, size):
        self.size = size
        self.highest_value = size * size
        self.board_data = self.__generate_board()
        self.arrangements = self.__generate_win_arrangements()

    # creates data structure for board of requested size
    def __generate_board(self):
        board_data = {}
        total_squares = list(range(1, self.highest_value + 1))
        for num in total_squares:
            Utilities.change_board_value(board_data, num, num)
        return board_data

    # generates possible win arrangements to be checked by win_check()
    def __generate_win_arrangements(self):
        # Creates a master list of all values as strings
        master_list = []
        for x in list(range(1, self.highest_value + 1)):
            master_list.append(str(x))

        arrangements = {"rows": [], "columns": [], "diagonals": []}

        # creates a matrices of board locations, arranged in order for checking
        arrangements["rows"] = [
            master_list[x : x + self.size]
            for x in range(0, len(master_list), self.size)
        ]
        arrangements["columns"] = [
            master_list[x :: self.size] for x in range(0, self.size)
        ]
        arrangements["diagonals"] = [
            master_list[0 :: self.size + 1],
            master_list[self.size - 1 : self.highest_value - 2 : self.size - 1],
        ]

        return arrangements

    def make_move(self, Player, move, server=False):
        if server == False:
            move_validation_result = MoveLogic.validate_move(self, move, self.size)
            if move_validation_result[0]:
                new_board = Board.__local_move_logic(self, Player, move)
                return (True, new_board)
            else:
                return move_validation_result
        if server == True:
            server_response = Board.__make_server_request(self, Player, move)
            if server_response[0]:
                new_board = Board.__read_server_response(server_response["game_data"])
                return (True, new_board)
            else:
                return server_response

    def __local_move_logic(GameBoard, Player, move):
        new_board_data = Utilities.change_board_value(
            GameBoard.board_data, move, Player.marker
        )
        new_board = Board(
            board_data=new_board_data,
            size=GameBoard.size,
            highest_value=GameBoard.highest_value,
            arrangements=GameBoard.arrangements,
            moves_made=GameBoard.moves_made + 1,
        )
        new_board.winner = MoveLogic.end_game(new_board, Player)
        return new_board

    def __make_server_request(GameBoard, Player, move):
        request_data = Utilities.generate_payload(GameBoard, Player, move)
        # Insert Post Request here
        return  # Response to POST Request

    def __read_server_response(server_response):
        new_board = Board.create_new_board_from_server_data(server_response)
        return new_board

    def create_new_board_from_server_data(response_data):
        return Board(
            board_data=response_data["board"]["board_data"],
            size=response_data["board"]["size"],
            highest_value=response_data["board"]["highest_value"],
            arrangements=response_data["board"]["arrangements"],
            moves_made=response_data["board"]["moves_made"],
        )

    def create_server_board_object(request_data):
        return Board(
            board_data=request_data["board"]["board_data"],
            size=request_data["board"]["size"],
            highest_value=request_data["board"]["highest_value"],
            arrangements=request_data["board"]["arrangements"],
            moves_made=request_data["board"]["moves_made"],
        )
