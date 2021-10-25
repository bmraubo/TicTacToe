from app.gamelogic import GameLogic


class GameProcess:
    def package_move(board, board_size, player, player_move, moves_made):
        move_information = {
            "player": {
                "name": player.name,
                "marker": player.marker,
            },
            "board": {
                "state": board,
                "size": board_size,
            },
            "move": {"move": player_move, "move_number": moves_made},
        }
        return move_information

    def process_move(move_information):
        # Validate Move
        valid_move = GameLogic.validate_move(
            move_information["board"]["state"],
            move_information["move"]["move"],
        )
        if valid_move[0] == False:
            # Return Error Information
            return {
                "move_success": False,
                "move_info": {"Error": "Invalid Move", "Reason": valid_move[1]},
            }
        # Make Move
        updated_board = GameLogic.change_board_value(
            move_information["board"]["state"],
            move_information["move"]["move"],
            move_information["player"]["marker"],
        )
        # Run Endgame Checks
        game_status = GameLogic.end_game(updated_board, move_information)
        # Return Response
        return {
            "move_success": True,
            "move_info": {
                "game_over": game_status[0],
                "game_status": game_status[1],
                "board": updated_board,
                "move_number": move_information["move"]["move_number"] + 1,
            },
        }
