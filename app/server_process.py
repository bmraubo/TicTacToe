from app.board import Board
from app.player import Player
from app.logic import Logic
from app.util import Utilities


class ServerProcess:
    def server_process(request_data):
        received_board = Board.create_server_board_object(request_data)
        received_player = Player.create_server_player_object(request_data)
        received_move = request_data["move"]
        # Move Validation
        move_validation = Logic.validate_move(received_board, received_move)
        if move_validation[0]:
            received_board.board_data = Utilities.change_board_value(
                received_board.board_data, received_move, received_player.marker
            )
            payload = Utilities.generate_payload(
                received_board, received_player, received_move
            )
            return {"move_success": True, "game_data": payload}
        # else:
        # Package response {{move_success}, {error reason}}
        pass
