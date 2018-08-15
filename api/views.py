from question_class import Question
from flask import jsonify, request
from flask.views import MethodView

class GetQuestion(MethodView):
    question1 = Question(1, 'Kyalyango John', 14, 'How can i implement an API using Flask frame work')   
    question2 = Question(2, 'Sssali David', 2, 'who knows what an API is')  
    question3 = Question(3, 'Kajura Benson', 6, 'how can i implement Restful API')   
    questions = [question1, question2, question3]
   
    def get(self, questionId):       
        qn =[question.__dict__ for question in self.questions if question.__dict__['id'] == questionId]
        return jsonify({'requested question': qn[0]})
        
                       