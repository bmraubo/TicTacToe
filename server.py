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
    response_data = ProcessMove.process_move(request_data)
    return response_data, 200


if __name__ == "__main__":
    main()
