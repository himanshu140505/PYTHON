import json
import requests

class QuizApp:
    def __init__(self, api_url):
        self.api_url = api_url
        self.questions = self.load_questions()
        self.score = 0

    def load_questions(self):
        response = requests.get(self.api_url)
        return response.json()

    def start_quiz(self):
        for question in self.questions:
            print(question['question'])
            for i, option in enumerate(question['options']):
                print(f"{i + 1}. {option}")
            answer = int(input("Your answer: "))
            if question['options'][answer - 1] == question['answer']:
                self.score += 1
        self.show_result()

    def show_result(self):
        print(f"Your score: {self.score}/{len(self.questions)}")
 
if __name__ == "__main__":
    api_url = 'https://example.com/api/questions'  # Replace with the actual API URL
    quiz_app = QuizApp(api_url)
    quiz_app.start_quiz()