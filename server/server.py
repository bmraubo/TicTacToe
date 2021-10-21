from flask import Flask, request
import os

from server.serverlogic import ServerLogic

app = Flask(__name__)


def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port)


class ProcessMove:
    # Full process
    def process_move(data):
        data_check = ProcessMove.check_request(data)
        if data_check[0] == False:
            # Handle Errors
            pass
        # Validate Move
        move_validation = ServerLogic.validate_move(data["board"], data["move"])
        if move_validation == False:
            # Handle errors
            pass
        # Make Move
        new_board_state = ServerLogic.change_board_value(
            data["board"], data["move"], data["player"]
        )
        # Run end game checks
        game_status = ServerLogic.end_game_check(
            data["board"], data["moves_made"], data["player"], data["board_size"]
        )
        # Prepare Response Data
        response_data = ProcessMove.prepare_response_data(new_board_state, game_status)
        return response_data

    # Check POST request data
    def check_request(data):
        required_data = ["player", "board", "board_size", "move", "moves_made"]
        for key in required_data:
            if key not in data:
                return (False, f"No {key} information")
        return (True, "OK")

    # Prepare Response Data
    def prepare_response_data(board_state, game_status):
        return {"board": board_state, "game_status": game_status[1]}


@app.route("/", methods=["POST"])
def process_request():
    request_data = request.get_json()
    response_data = {"request": "processed"}
    return response_data, 200


if __name__ == "__main__":
    main()
