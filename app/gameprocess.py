from app.logic import Logic


class GameProcess:

    # Check Board Value
    def check_board_value(board, current_board_value):
        # checks value in board data
        return board[str(current_board_value)]

    # Change Board Value
    def change_board_value(board, current_board_value, new_board_value):
        # replaces value in board data with new value
        board[str(current_board_value)] = str(new_board_value)
        return board

    # Package Move Information
    def package_move_information(board, player, player_move):
        move_information = {
            "player": {
                "name": player.name,
                "marker": player.marker,
            },
            "board": {
                "state": board.board,
                "size": board.size,
            },
            "move": {"move": player_move, "move_number": board.moves_made},
        }
        return move_information

    # Process Move Information
    def process_move(move_information):
        # Validate Move
        valid_move = Logic.validate_move(
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
        updated_board = GameProcess.change_board_value(
            move_information["board"]["state"],
            move_information["move"]["move"],
            move_information["player"]["marker"],
        )
        # Run Endgame Checks
        game_status = Logic.end_game(updated_board, move_information)
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
