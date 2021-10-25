from flask import Flask, request
import os
import werkzeug

from server.processmove import ProcessMove

app = Flask(__name__)


def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


@app.route("/", methods=["POST"])
def process_request():
    request_data = request.get_json()
    return ProcessMove.process_move(request_data)


if __name__ == "__main__":
    main()
