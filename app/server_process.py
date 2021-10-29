from app.board import Board
from app.player import Player


class ServerProcess:
    def server_process(request_data):
        received_board = Board.create_server_board_object(request_data)
        received_player = Player.create_server_player_object(request_data)
        received_move = request_data["move"]
        # Move Validation
        # if move_validation[0]:
        # Update Board Object
        # Package {move_success}, {Board, Player}
        # else:
        # Package response {{move_success}, {error reason}}
        pass
