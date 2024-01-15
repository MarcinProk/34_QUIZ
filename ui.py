import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
Q_FONT = ("Arial", 20, 'italic')

class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):              
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title('Quiz')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = tk.Label(text=f"Score: {self.quiz.score}")
        self.score_label.grid(column=1, row=0)
        self.score_label.config(bg=THEME_COLOR, padx=20, pady=20, fg='white')
                              
        self.canvas = tk.Canvas(width=300, height=250, bg='white')
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)
        self.canvas_text = self.canvas.create_text(
            150, 
            125, 
            width= 290,
            text="Question", 
            font=Q_FONT, 
            fill=THEME_COLOR)

        right_img = tk.PhotoImage(file=R"images\true.png")
        self.right_button = tk.Button(image=right_img, command=self.clicked_true)
        self.right_button.grid(column=0, row=2, padx=20, pady=20)

        wrong_img = tk.PhotoImage(file=R"images\false.png")
        self.wrong_button = tk.Button(image=wrong_img, command=self.clicked_false)
        self.wrong_button.grid(column=1, row=2, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else: 
            self.canvas.itemconfig(self.canvas_text, text="You have reached the end of the quiz!")
            self.right_button.config(state='disable')
            self.wrong_button.config(state='disable')

    def clicked_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def clicked_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:           
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000,self.get_next_question)
