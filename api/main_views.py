"""Module defines views """
from flask import jsonify, request
from flask.views import MethodView
from question_answer_class import Question, Answer
class GetQuestionAnswer(MethodView):
    """
    Class to run the views using method view
    params: routes
    respone: json data
    """
    question1 = Question(1, 'Kyalyango John',
                         'How can i implement an API using Flask frame work')
    question2 = Question(2, 'Sssali David', 'who knows what an API is')
    question3 = Question(3, 'Kajura Benson', 'how can i implement Restful API')
    questions = [question1, question2, question3]
    answer1 = Answer(1, 14, "Try Andela")
    answer2 = Answer(2, 2, "Let me contat google")
    answers = [answer1, answer2]
    def get(self, question_id):
        """
        get method for get requests
        param: route /api/v1/questions and /api/v1/questions/<int:question_id>
        response: json data
        """
        if str(request.url_rule) == "/api/v1/questions":
            return jsonify({'Questions':[question.__dict__ for question in self.questions]})
        if str(request.url_rule) == "/api/v1/questions/<int:question_id>":
            question_response = [question.__dict__ for question in self.questions
                                 if question.__dict__['user_question_id'] == question_id]
            return jsonify({'requested question': question_response[0]})
        return "Not found"
    def post(self, question_id=None):
        """
        post method for post requests
        param: route /api/v1/questions and /questions/<int:question_id>/answers
        response: json data
        """
        if str(request.url_rule) == "/api/v1/questions":
            add_question = Question(request.json['user_question_id'], request.json['user_name'],
                                    request.json['user_question'])
            self.questions.append(add_question)
            return jsonify({'New question file': [x.__dict__ for x in self.questions]})
        if str(request.url_rule) == "/questions/<int:question_id>/answers":
            add_answer = Answer(request.json['answer_id'], question_id, request.json['answer'])
            self.answers.append(add_answer)
            return jsonify({'Answer to question': [x.__dict__ for x in self.answers]})
        return jsonify({'Message': False})
