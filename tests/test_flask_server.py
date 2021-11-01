import unittest
from app.server_process import ServerProcess
from flask import Flask, request


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
