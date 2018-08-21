"""Class for defining url routes"""
from api.main_views import GetQuestion
class GetRoutes():
    """
    GetRoutes defines routes
    params:urls
    """
    @staticmethod
    def fetch_routes(questionanswer):
        """
        Add url rule defines the routes for http requests
        """
        question_view = GetQuestion.as_view('questions')
        questionanswer.add_url_rule('/api/v1/questions', view_func=question_view,
                                    defaults={'question_id': None}, methods=['Get',])
        questionanswer.add_url_rule('/api/v1/questions/<int:question_id>',
                                    view_func=question_view, methods=['Get',])
        question_answer = GetQuestion.as_view('questionsanswers')
        questionanswer.add_url_rule('/api/v1/questions',
                                    view_func=question_answer, methods=['POST',])
        questionanswer.add_url_rule('/questions/<int:question_id>/answers',
                                    view_func=question_answer, methods=['POST',])
         