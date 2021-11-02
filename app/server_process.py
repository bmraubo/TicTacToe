from requests.api import request
from app.board import Board
from app.player import Player
from app.logic import Logic
from app.util import Utilities


class ServerProcess:
    def server_process(request_data):
        received_board = Board.create_new_board_object(request_data["board"])
        received_player = Player.create_server_player_object(request_data)
        received_move = request_data["move"]
        # Move Validation
        move_validation = Logic.validate_move(received_board, received_move)
        if move_validation[0]:
            received_board.board_data = Utilities.change_board_value(
                received_board.board_data, received_move, received_player.marker
            )
            received_board.increase_moves_made_total()
            payload = Utilities.generate_payload(
                received_board, received_player, received_move
            )
            return {"move_success": move_validation[0], "game_data": payload}, 200
        else:
            return {
                "move_success": move_validation[0],
                "error": move_validation[1],
            }, 400

    def request_data_check(request_data):
        top_level_keys = ["board", "player", "move"]
        for key in top_level_keys:
            if key not in request_data:
                return False
        return True
