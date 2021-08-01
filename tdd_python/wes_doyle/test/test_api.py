import json
import unittest

from flask import request

from app import app

class TestApi(unittest.TestCase):

    def test_ner_endpoint_give_json_body_returns_200(self):
        with app.test_client() as client:
            response = client.post('/ner', json={"sentnce": "Steve Malkmus is in a good band."})
            assert response._status_code == 200
