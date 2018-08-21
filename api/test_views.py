"""Module for making tests on the app"""
import unittest
import json
from run import app
class TestViews(unittest.TestCase):
    """"
    Class for making tests
    params: unittest.testCase
    """
    def setUp(self):
        """
        Method for making the client object
        """
        self.client = app.test_client
    def test_fetch_all_questions(self):
        """Method for tesing the get function which returns all questions"""
        result = self.client().get('api/v1/questions')
        respond = json.loads(result.data.decode("utf8"))

        self.assertEqual(result.status_code, 200)
        self.assertTrue(result.json["Questions"])
        self.assertIn('Questions', respond)
        self.assertIsInstance(respond, dict)
    def test_get_a_question(self):
        """Method for tesing the get function which returns one question"""
        result = self.client().get('api/v1/questions/1')
        result2 = self.client().get('api/v1/questions/a')
        respond = json.loads(result.data.decode("utf8"))
        self.assertEqual(result.status_code, 200)
        self.assertTrue(result.json["requested question"])
        self.assertEqual(result2.status_code, 404)
        self.assertIn('requested question', respond)
        self.assertIsInstance(respond, dict)
    def test_add_a_questions(self):
        """Method for tesing the post function which posts a question"""
        result = self.client().post('api/v1/questions',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_question_id=17, user_name="ben",
                                                         user_question=
                                                         "am in Gayaza where can i find andela")))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('New question file', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 201)
        self.assertTrue(result.json["New question file"])
    def test_add_a_answer(self):
        """Method for tesing the post function which posts an answer"""
        result = self.client().post('/questions/2/answers',
                                    content_type="application/json", data=json.dumps(dict(
                                        answer_id=4, answer=
                                        "am in Gayaza where can i find andela")))
        result2 = self.client().post('/questions/p/answers',
                                     content_type="application/json",
                                     data=json.dumps(dict(
                                         answer_id=4, answer=
                                         "am in Gayaza where can i find andela")))
        respond = json.loads(result.data.decode("utf8"))
        self.assertEqual(result.status_code, 201)
        self.assertEqual(result2.status_code, 404)
        self.assertTrue(result.json["Answer to question"])
        self.assertIn('Answer to question', respond)
        self.assertIsInstance(respond, dict)
            