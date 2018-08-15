from views import GetQuestion
class GetUrls():
    @staticmethod
    def fetch_urls(question):
        question_view = GetQuestion.as_view('questions')        
        question.add_url_rule('/api/v1/questions/<int:questionId>', view_func=question_view, methods=['Get',])
         