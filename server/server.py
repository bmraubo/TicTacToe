from flask import Flask, request
import os

app = Flask(__name__)


def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port)


@app.route("/", methods=["POST"])
def process_move():
    response_data = {"move": "processed"}
    return response_data, 200


if __name__ == "__main__":
    main()
