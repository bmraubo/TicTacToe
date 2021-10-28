class Utilities:
    def check_board_value(board_data, current_board_value):
        # checks value in board data
        return board_data[str(current_board_value)]

    def change_board_value(board_data, current_board_value, new_board_value):
        # replaces value in board data with new value
        board_data[str(current_board_value)] = str(new_board_value)
        return board_data

    def generate_payload(GameBoard, Player, move):
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
