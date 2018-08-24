"""
   Module for processing logic for endpoints
"""

from .question_answer_class import Question, Answer
class QuestionAnswer:
    """
       Class for processing logic for endpoints
       """
    questions = []
    answers = []

    @staticmethod
    def get_all_questions():
        """
           method for getting all questions
           params: none
           response: dictionary
        """
        if not QuestionAnswer.questions:
            return True
        question_dict = [question.__dict__ for question in QuestionAnswer.questions]
        return question_dict

    @staticmethod
    def get_one_question(question_id):
        """
           method for getting one specific questions
           params: question_id
           response: dictionary
        """
        if not QuestionAnswer.questions:
            return {'Questions':'No questions available please post a question'}
        avilable_question_id = [
            question.__dict__ for question in QuestionAnswer.questions
            if question.__dict__['user_question_id'] == question_id]
        if not avilable_question_id:
            return {question_id:"Question id doesnot exist"}
        return {'requested question': [
            question.__dict__
            for question in QuestionAnswer.questions
            if question.__dict__['user_question_id'] == question_id]}

    @staticmethod
    def post_a_quetion(user_name, user_question):
        """
           method for posting a questions
           params: user_name and user_question
           response: dictionary
        """
        size = [question.__dict__ for question in QuestionAnswer.questions]
        counter = len(size) + 1
        add_question = Question(counter, user_name, user_question)
        QuestionAnswer.questions.append(add_question)
        return {'New question file': [
            question.__dict__ for question in QuestionAnswer.questions]}

    @staticmethod
    def post_an_answer(question_id, user_name, user_answer):
        """
           method for posting an answer
           params: user_name and question_id
           response: dictionary
        """
        availble_question_id = [
            question.__dict__ for question in QuestionAnswer.questions
            if question.__dict__['user_question_id'] == question_id]
        if not availble_question_id:
            question_dict = [question.__dict__ for question in QuestionAnswer.questions]
            empty_list = ["000000000000", "Question id you entered is out of range",
                          "Check down for the xexisting questions thanks ", "000000000000"]
            empty_list.append(question_dict)
            return empty_list
        size = [answer.__dict__ for answer in QuestionAnswer.answers]
        counter = len(size) + 1
        add_answer = Answer(counter, user_name, question_id, user_answer)
        QuestionAnswer.answers.append(add_answer)
        return {'Question':[
            question.__dict__ for question in QuestionAnswer.questions
            if question.__dict__['user_question_id'] == question_id]}, {'Answer to question': [
                question.__dict__ for question in QuestionAnswer.answers
                if question.__dict__['user_question_id'] == question_id]}
   