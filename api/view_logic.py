"""Module for processing logic for endpoints"""
from flask import jsonify, request
from .question_answer_class import Question, Answer
class QuestionAnswer:
    """Class for processing logic for endpoints"""
    questions = []
    answers = []
    @staticmethod
    def get_all_questions():
        """
        method for getting all questions
        response: json data
        """
        if len(QuestionAnswer.questions) == 0:
            return jsonify({'Questions':'No questions available please post a question'}), 200
        return jsonify({'Questions':[question.__dict__
                                     for question in QuestionAnswer.questions]}), 200
    @staticmethod
    def get_one_question(question_id):
        """
        method for getting one specific questions
        params: question_id
        response: json data
        """
        if len(QuestionAnswer.questions) == 0:
            return jsonify({'Questions':'No questions available please post a question'}), 200
        avilable_question_id = [
            question.__dict__ for question in QuestionAnswer.questions
            if question.__dict__['user_question_id'] == question_id]
        if len(avilable_question_id) == 0:
            return jsonify({question_id:"Question id doesnot exist"}), 200
        return jsonify({'requested question': [
            question.__dict__
            for question in QuestionAnswer.questions
            if question.__dict__['user_question_id'] == question_id]}), 200
    @staticmethod
    def post_a_quetion():
        """
        method for posting a questions
        params: dictionary(json data)
        response: json data
        """
        keys = ("user_question_id", "user_name", "user_question")
        if not set(keys).issubset(set(request.json)):
            return jsonify({'New question file': 'Your request has Empty feilds'})
        avilable_question_id = [question.__dict__ for question in QuestionAnswer.questions
                                if question.__dict__['user_question_id']
                                == request.json['user_question_id']]
        if len(avilable_question_id) != 0:
            return jsonify({request.json['user_question_id']:"Question id already exist"}), 200
        add_question = Question(request.json['user_question_id'], request.json['user_name'],
                                request.json['user_question'])
        QuestionAnswer.questions.append(add_question)
        return jsonify({'New question file': [
            question.__dict__ for question in QuestionAnswer.questions]}), 201
    @staticmethod
    def post_an_answer(question_id):
        """
        method for posting an answer
        params: dictionary(json data) and question_id
        response: json data
        """
        keys = ("answer_id", "answer")
        if not set(keys).issubset(set(request.json)):
            return jsonify({'New answer file': 'Your request has Empty feilds'}), 400
        availble_question_id = [
            question.__dict__ for question in QuestionAnswer.questions
            if question.__dict__['user_question_id'] == question_id]
        if len(availble_question_id) == 0:
            return jsonify({question_id:"Question id doesnot exist"}), 404
        availble_answer_id = [
            answer.__dict__ for answer in QuestionAnswer.answers
            if answer.__dict__['answer_id'] == request.json['answer_id']]
        if len(availble_answer_id) != 0:
            return jsonify({request.json['answer_id']:"answer id exist"}), 409
        add_answer = Answer(request.json['answer_id'], question_id, request.json['answer'])
        QuestionAnswer.answers.append(add_answer)
        return jsonify({'Question':[
            question.__dict__ for question in QuestionAnswer.questions
            if question.__dict__['user_question_id'] == question_id]}, {'Answer to question': [
                question.__dict__ for question in QuestionAnswer.answers
                if question.__dict__['user_question_id'] == question_id]}), 201
