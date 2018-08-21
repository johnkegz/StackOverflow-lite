"""Module defines views """
from flask import jsonify, request
from flask.views import MethodView
from .question_answer_class import Question, Answer
class GetQuestion(MethodView):
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
    def get_all_questions(self):
        """
        method for getting all questions        
        response: json data
        """
        return jsonify({'Questions':[question.__dict__ for question in self.questions]}), 200
    def get_one_question(self, question_id):
        """
        method for getting one specific questions 
        params: question_id     
        response: json data
        """
        question_response = [question.__dict__ for question in self.questions
                                  if question.__dict__['user_question_id'] == question_id]
        return jsonify({'requested question': question_response[0]}), 200
    def post_a_quetion(self):
        """
        method for posting a questions 
        params: dictionary(json data)     
        response: json data
        """
        add_question = Question(request.json['user_question_id'], request.json['user_name'],
                                    request.json['user_question'])
        self.questions.append(add_question)
        return jsonify({'New question file': [x.__dict__ for x in self.questions]}), 201
    def post_an_answer(self, question_id):
        """
        method for posting an answer 
        params: dictionary(json data) and question_id    
        response: json data
        """
        add_answer = Answer(request.json['answer_id'], question_id, request.json['answer'])
        self.answers.append(add_answer)
        return jsonify({'Answer to question': [x.__dict__ for x in self.answers]}), 201       
    def get(self, question_id):
        """
        get method for get requests
        param: route /api/v1/questions and /api/v1/questions/<int:question_id>
        response: get_all_questions() and self.get_one_question(question_id)
        """
        if question_id is None:
            return self.get_all_questions()
        return self.get_one_question(question_id)         
        
    def post(self, question_id=None):
        """
        post method for post requests
        param: route /api/v1/questions and /questions/<int:question_id>/answers
        response: json data
        """
        if question_id is None:
           return self.post_a_quetion()
        return self.post_an_answer(question_id)
