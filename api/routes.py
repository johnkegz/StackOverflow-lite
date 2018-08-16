from question_class import Question
from flask import jsonify, request
from flask.views import MethodView
import json

class GetQuestion(MethodView):
    question1 = Question(1, 'Kyalyango John', 14, 'How can i implement an API using Flask frame work')   
    question2 = Question(2, 'Sssali David', 2, 'who knows what an API is')  
    question3 = Question(3, 'Kajura Benson', 6, 'how can i implement Restful API')   
    questions = [question1, question2, question3]
   
    def post(self):

        add_question = Question(request.json['id'], request.json['user_name'], request.json['question_id'], request.json['user_question'])

        self.questions.append(add_question)
        return jsonify({'New question file': [x.__dict__ for x in self.questions]})
        
                       