"""
   Module defines views
"""
from flask import jsonify, request
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
           response: json data get_all_questions() and self.get_one_question(question_id)
        """
        if question_id is None:
            if QuestionAnswer.get_all_questions() is True:
                return jsonify({'Questions':'No questions available please post a question'})
            return jsonify({'Questions': QuestionAnswer.get_all_questions()})
        return jsonify(QuestionAnswer.get_one_question(question_id))

    @staticmethod
    def post(question_id=None):
        """
           post method for post requests
           param: route /api/v1/questions and /questions/<int:question_id>/answers
           response: json data
        """
        if question_id is None:
            keys = ("user_name", "user_question")
            if not set(keys).issubset(set(request.json)):
                return jsonify({'New answer file': 'Your request has Empty feilds'}), 400
            return jsonify(QuestionAnswer.post_a_quetion(request.json['user_name'],
                                                         request.json['user_question']))
        keys = ("user_name", "answer")
        if not set(keys).issubset(set(request.json)):
            return jsonify({'New answer file': 'Your request has Empty feilds'}), 400
        return jsonify(QuestionAnswer.post_an_answer(question_id, request.json['user_name'],
                                                     request.json['answer']))
