""" Module for Question and answers"""
class Question:
    """
        Class defines the question atributes
        params: id, user_name, question_id, user_question
        """
    def __init__(self, user_question_id, user_name, user_question):
        self.user_question_id = user_question_id
        self.user_name = user_name
        self.user_question = user_question
    # @property
    # def questionss(self):
    #     """
    #     returns question id
    #     """
    #     return self.user_question_id
class Answer:
    """
        Class defines the answer atributes
        params: id, user_name, question_id, user_question
    """
    def __init__(self, answer_id, user_question_id, answer):
        self.answer_id = answer_id
        self.user_question_id = user_question_id
        self.answer = answer
    # @property
    # def answer_idd(self):
    #     """
    #     returns answer id
    #     """
    #     return self.answer_id
    # @property
    # def answerr(self):
    #     """
    #     returns answer id
    #     """
    #     return self.answer
