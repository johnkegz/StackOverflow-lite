from question_answer_class import Question, Answer
from flask import jsonify, request
from flask.views import MethodView
import json

class GetQuestionAnswer(MethodView): 
    question1 = Question(1, 'Kyalyango John', 14, 'How can i implement an API using Flask frame work')   
    question2 = Question(2, 'Sssali David', 2, 'who knows what an API is')  
    question3 = Question(3, 'Kajura Benson', 6, 'how can i implement Restful API')   
    questions = [question1, question2, question3]

    answer1 = Answer(1, 14, "Try Andela")
    answer2 = Answer(2, 2, "Let me contat google")
    answers = [answer1, answer2]
    def get(self, questionId):
        if questionId == None:
            return jsonify({'Questions':[question.__dict__ for question in self.questions]})
        else:
            qn =[question.__dict__ for question in self.questions if question.__dict__['id'] == questionId]
            return jsonify({'requested question': qn[0]})   
    def post(self, questionId = None):
        if questionId == None:
            add_question = Question(request.json['id'], request.json['user_name'], request.json['question_id'], request.json['user_question'])
            self.questions.append(add_question)
            return jsonify({'New question file': [x.__dict__ for x in self.questions]})
        else:
            add_answer = Answer(request.json['answer_id'], questionId, request.json['answer'])
            self.answers.append(add_answer)
            return jsonify({'Answer to question': [x.__dict__ for x in self.answers]})
        
                       