import unittest
from app.server_process import ServerProcess
from flask import Flask, request


class testFlaskServer(unittest.TestCase):
    def test_client():
        app = Flask(__name__)
        app.testing = True
        return app.test_client()

        @app.route("/test", methods=["GET"])
        def test_response():
            return "OK", 200

    def test_server_response(self):
        test_client = testFlaskServer.test_client()
        response = test_client.get("/test")
        self.assertEqual(response, "OK")
