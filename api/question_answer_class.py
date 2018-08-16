class Question():
    def __init__ (self, id, user_name, question_id, user_question):
        self.id = id
        self.user_name = user_name
        self.question_id = question_id
        self.user_question = user_question

class Answer():
    def __init__(self, answer_id, question_id, answer):
        self.answer_id = answer_id
        self.question_id = question_id
        self.answer = answer
