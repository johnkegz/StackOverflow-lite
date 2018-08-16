import unittest
import json
from json import JSONEncoder

from app import app
class TestViews(unittest.TestCase):
    def setUp(self):
        self.question = app
        self.client = self.question.test_client        
    def test_add_a_answer(self):
        result = self.client().post('/questions/2/answers' , content_type="application/json", data=json.dumps(dict(answer_id=4, answer="am in Gayaza where can i find andela")))
        self.assertTrue(result.json["Answer to question"])
        