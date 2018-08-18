"""Module for making tests on the app"""
import unittest
import json

from app import App
class TestViews(unittest.TestCase):
    """"
    Class for making tests
    params: unittest.testCase
    """
    def setUp(self):
        """
        Method for making the client object
        """
        self.client = App.test_client
    def test_fetch_all_questions(self):
        """Method for tesing the get function which returns all questions"""
        result = self.client().get('api/v1/questions')
        self.assertTrue(result.json["Questions"])
    def test_get_a_question(self):
        """Method for tesing the get function which returns one question"""
        result = self.client().get('api/v1/questions/1')
        self.assertTrue(result.json["requested question"])
    def test_add_a_questions(self):
        """Method for tesing the post function which posts a question"""
        result = self.client().post('api/v1/questions',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_question_id=17, user_name="ben",
                                                         user_question=
                                                         "am in Gayaza where can i find andela")))
        self.assertTrue(result.json["New question file"])
    def test_add_a_answer(self):
        """Method for tesing the post function which posts an answer"""
        result = self.client().post('/questions/2/answers',
                                    content_type="application/json",
                                    data=json.dumps(dict(
                                        answer_id=4, answer=
                                        "am in Gayaza where can i find andela")))
        self.assertTrue(result.json["Answer to question"])
        