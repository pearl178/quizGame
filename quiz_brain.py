
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.current_question = None

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.current_question.text = html.unescape(self.current_question.text)
        user_answer = input(f"Q.{self.question_number}: {self.current_question.text} (True/False): ")
        self.check_answer(user_answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("Sorry you got it wrong.")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score: {self.score}/{self.question_number}")
        print("\n")
