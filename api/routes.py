from main_views import GetQuestionAnswer
class GetRoutes():
    @staticmethod
    def fetch_routes(questionanswer):
        question_answer = GetQuestionAnswer.as_view('questionsanswers')        
        questionanswer.add_url_rule('/questions/<int:questionId>/answers', view_func=question_answer, methods=['POST',])
         