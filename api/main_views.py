from question_answer_class import Answer
from flask import jsonify, request
from flask.views import MethodView
import json

class GetQuestionAnswer(MethodView): 
    answer1 = Answer(1, 14, "Try Andela")
    answer2 = Answer(2, 2, "Let me contat google")
    answers = [answer1, answer2]   
    def post(self, questionId):
        add_answer = Answer(request.json['answer_id'], questionId, request.json['answer'])
        self.answers.append(add_answer)
        return jsonify({'Answer to question': [x.__dict__ for x in self.answers]})
        
                       