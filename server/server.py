from flask import Flask, request
import os

app = Flask(__name__)


def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port)


class ProcessMove:
    def check_request(data):
        if "player" not in data:
            return False
        elif "board" not in data:
            return False
        elif "board_size" not in data:
            return False
        elif "move" not in data:
            return False
        else:
            return True


@app.route("/", methods=["POST"])
def process_move():
    request_data = request.get_json()
    response_data = {"move": "processed"}
    return response_data, 200


if __name__ == "__main__":
    main()
