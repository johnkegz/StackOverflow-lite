import unittest
from app import app
class TestViews(unittest.TestCase):
    def setUp(self):
        self.question = app
        self.client = self.question.test_client
    def test_fetch_all_questions(self):
        result = self.client().get('api/v1/questions')
        self.assertTrue(result.json["Questions"])