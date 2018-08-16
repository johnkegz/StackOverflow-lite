import unittest
import json
from json import JSONEncoder

from app import app
class TestViews(unittest.TestCase):
    def setUp(self):
        self.question = app
        self.client = self.question.test_client        
    def test_add_a_questions(self):
        result = self.client().post('api/v1/questions' , content_type="application/json", data=json.dumps(dict(id=4, user_name="ben", question_id=17, user_question="am in Gayaza where can i find andela")))
        self.assertTrue(result.json["New question file"])
        