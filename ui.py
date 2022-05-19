THEME_COLOR = "#375362"
RED = '#EF6D6D'
GREEN = '#B8F1B0'
Q_FONT = ('Arial', 20, 'italic')
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = Label(text=" ", bg=THEME_COLOR, fg='white')
        self.score.grid(column=1, row=1)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 125,
            fill=THEME_COLOR,
            font=Q_FONT,
            text="",
            width=280)
        self.canvas.grid(column=0, row=2, columnspan=2, pady=20)
        true_image = PhotoImage(file='images/true.png')
        false_image = PhotoImage(file='images/false.png')
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.check_answer_true)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.check_answer_false)
        self.true_button.grid(column=0, row=3)
        self.false_button.grid(column=1, row=3)

        self.show_question()

        self.window.mainloop()

    def show_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz\n"
                                                            f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def check_answer_true(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def check_answer_false(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg=GREEN)
        else:
            self.canvas.config(bg=RED)
        self.window.after(1000, self.show_question)


