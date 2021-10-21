from flask import Flask, request
import os

app = Flask(__name__)


def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port)


class ProcessMove:
    def check_request(data):
        required_data = ["player", "board", "board_size", "move"]
        for key in required_data:
            if key not in data:
                return (False, f"No {key} information")
        return (True, "OK")


@app.route("/", methods=["POST"])
def process_move():
    request_data = request.get_json()
    response_data = {"move": "processed"}
    return response_data, 200


if __name__ == "__main__":
    main()
