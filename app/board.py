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

    # checks all arrangements to see if player with 'marker' has won the game
    def win_check(self, marker):
        # nested function to check if a win condition is met
        def tally(self, marker, arrangement):
            count = 0
            for element in arrangement:
                for num in element:
                    if Utilities.check_board_value(self.board_data, num) == marker:
                        count += 1
                if count == self.size:
                    return True
                count = 0

        for key in self.arrangements:
            if tally(self, marker, self.arrangements[key]):
                return True

        return False

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
            new_board = Board.__server_move_logic(server_response)
            return new_board

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
        new_board.winner = Board.end_game(new_board, Player)
        return new_board

    def __make_server_request(GameBoard, Player, move):
        pass

    def __read_server_response(server_response):
        pass

    def end_game(GameBoard, player):
        # Checks if the most recent player's move has won them the game
        if GameBoard.win_check(player.marker):
            winner = player
            return winner
        # If the most recent move has not won the game, the outcome might be a draw
        elif GameBoard.moves_made == GameBoard.highest_value:
            winner = "Draw!"
            return winner
        else:
            return None

    def declare_winner(winner):
        if winner == "Draw!":
            return f"It's a {winner}"
        elif winner == None:
            pass
        else:
            return f"{winner.name} has won the game\N{Party Popper}"

    def package_request(GameBoard, Player, move):
        package = {
            "board": {
                "board_data": GameBoard.board_data,
                "size": GameBoard.size,
                "highest_value": GameBoard.highest_value,
                "arrangements": GameBoard.arrangements,
                "winner": GameBoard.winner,
                "moves_made": GameBoard.moves_made,
            },
            "player": {
                "name": Player.name,
                "type": Player.type,
                "marker": Player.marker,
            },
            "move": move,
        }
        return package

    def create_server_board_object(request_data):
        return Board(
            board_data=request_data["board"]["board_data"],
            size=request_data["board"]["size"],
            highest_value=request_data["board"]["highest_value"],
            arrangements=request_data["board"]["arrangements"],
            moves_made=request_data["board"]["moves_made"],
        )
