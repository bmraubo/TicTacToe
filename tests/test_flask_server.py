import unittest
from app.server_process import ServerProcess
from flask import Flask, request
from app.board import Board
from app.player import HumanPlayer
from app.util import Utilities


class TestSimpleServer(unittest.TestCase):
    def create_test_server():
        app = Flask(__name__)
        app.testing = True

        @app.route("/test", methods=["POST"])
        def test_response():
            return "OK", 200

        return app

    def test_server_response(self):
        test_server = TestSimpleServer.create_test_server()
        with test_server.test_client() as client:
            response = client.post("/test")
            self.assertEqual(response.status_code, 200)


class TestGameServer(unittest.TestCase):
    def create_test_game_server():
        app = Flask(__name__)
        app.testing = True

        @app.route("/", methods=["POST"])
        def test_process():
            request_data = request.get_json()
            return ServerProcess.server_process(request_data)

        return app

    def server_process_test_set_up(test_move):
        test_board = Board()
        test_board.create_board(3)
        test_player = HumanPlayer(["Marx", "human", "X"])
        request_data = Utilities.generate_payload(test_board, test_player, test_move)
        return request_data

    def test_game_server_move(self):
        test_server = TestGameServer.create_test_game_server()
        with test_server.test_client() as client:
            test_move = "1"
            request_data = TestGameServer.server_process_test_set_up(test_move)
            response = client.post("/", json=request_data)
            response_board_data = response.json["game_data"]["board"]["board_data"]
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json["game_data"]["board"]["size"], 3)
            self.assertEqual(
                Utilities.check_board_value(response_board_data, "1"),
                "X",
            )
