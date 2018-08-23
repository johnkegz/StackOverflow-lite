"""Module defines views """
from flask.views import MethodView
from .view_logic import QuestionAnswer
class GetQuestion(MethodView):
    """
    Class to run the views using method view
    params: routes
    respone: json data
    """
    @staticmethod
    def get(question_id):
        """
        get method for get requests
        param: route /api/v1/questions and /api/v1/questions/<int:question_id>
        response: get_all_questions() and self.get_one_question(question_id)
        """
        if question_id is None:
            return QuestionAnswer.get_all_questions()
        return QuestionAnswer.get_one_question(question_id)
    @staticmethod
    def post(question_id=None):
        """
        post method for post requests
        param: route /api/v1/questions and /questions/<int:question_id>/answers
        response: json data
        """
        if question_id is None:
            return QuestionAnswer.post_a_quetion()
        return QuestionAnswer.post_an_answer(question_id)
