from main_views import GetQuestionAnswer
class GetRoutes():
    @staticmethod
    def fetch_routes(questionanswer):
        question_view = GetQuestionAnswer.as_view('questions')
        questionanswer.add_url_rule('/api/v1/questions', view_func=question_view, defaults={'questionId': None}, methods=['Get',])        
        questionanswer.add_url_rule('/api/v1/questions/<int:questionId>', view_func=question_view, methods=['Get',])
        question_answer = GetQuestionAnswer.as_view('questionsanswers')
        questionanswer.add_url_rule('/api/v1/questions', view_func=question_answer, methods=['POST',])        
        questionanswer.add_url_rule('/questions/<int:questionId>/answers', view_func=question_answer, methods=['POST',])
         