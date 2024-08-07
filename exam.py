import tkinter as tk
from tkinter import messagebox
import pandas as pd
import random

class QuizApp:
    def __init__(self, root, csv_file):
        self.root = root
        self.root.title("Quiz App")

        self.data = pd.read_csv(csv_file, sep=';')
        self.questions = self.data.to_dict(orient='records')
        random.shuffle(self.questions)

        self.current_question_index = 0
        self.correct_answers = 0
        self.user_answers = []

        self.question_label = tk.Label(root, text="", wraplength=400, justify="left")
        self.question_label.pack(pady=10)

        self.options = tk.StringVar(value="")
        self.option_buttons = []

        for i in range(5):
            rb = tk.Radiobutton(root, text="", variable=self.options, value=i, anchor='w', justify='left', wraplength=400)
            rb.pack(fill='x')
            self.option_buttons.append(rb)

        self.reveal_button = tk.Button(root, text="Reveal Answer", command=self.reveal_answer)
        self.reveal_button.pack(pady=5)

        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack(side='right', padx=5, pady=5)

        self.back_button = tk.Button(root, text="Back", command=self.previous_question)
        self.back_button.pack(side='left', padx=5, pady=5)

        self.finish_button = tk.Button(root, text="Finish", command=self.finish_quiz)
        self.finish_button.pack(pady=5)

        self.show_question()

    def show_question(self):
        question_data = self.questions[self.current_question_index]
        self.question_label.config(text=question_data['Question'])
        options = [question_data[f'Option {chr(65+i)}'] for i in range(5) if question_data[f'Option {chr(65+i)}']]
        
        for i, opt in enumerate(options):
            self.option_buttons[i].config(text=opt)
            self.option_buttons[i].pack()
        
        for i in range(len(options), 5):
            self.option_buttons[i].pack_forget()

        self.options.set("")

    def reveal_answer(self):
        question_data = self.questions[self.current_question_index]
        correct_answer = question_data['Correct Answer']
        correct_index = ord(correct_answer) - 65
        messagebox.showinfo("Correct Answer", f"The correct answer is: {question_data[f'Option {correct_answer}']}")
        self.user_answers.append((self.current_question_index, self.options.get() == correct_index))

    def next_question(self):
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
            self.show_question()

    def previous_question(self):
        if self.current_question_index > 0:
            self.current_question_index -= 1
            self.show_question()

    def finish_quiz(self):
        answered_questions = len(self.user_answers)
        correct_answers = sum(1 for _, correct in self.user_answers if correct)
        incorrect_answers = answered_questions - correct_answers
        messagebox.showinfo("Quiz Summary", f"Questions Answered: {answered_questions}\nCorrect Answers: {correct_answers}\nIncorrect Answers: {incorrect_answers}")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root, "1.csv")
    root.mainloop()
