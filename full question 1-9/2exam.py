import tkinter as tk
from tkinter import messagebox, simpledialog
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
        self.user_answers = [None] * len(self.questions)

        # Label for current question number and total questions
        self.progress_label = tk.Label(root, text="")
        self.progress_label.pack(pady=5)

        self.question_label = tk.Label(root, text="", wraplength=400, justify="left")
        self.question_label.pack(pady=10)

        self.options_vars = []
        self.option_checkboxes = []

        for i in range(5):
            var = tk.BooleanVar(value=False)
            cb = tk.Checkbutton(root, text="", variable=var, anchor='w', justify='left', wraplength=400)
            cb.pack(fill='x')
            self.option_checkboxes.append(cb)
            self.options_vars.append(var)

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
        self.progress_label.config(text=f"Question {self.current_question_index + 1}/{len(self.questions)}")
        self.question_label.config(text=question_data['Question'])
        options = [question_data[f'Option {chr(65+i)}'] for i in range(5) if question_data[f'Option {chr(65+i)}']]

        for i, opt in enumerate(options):
            self.option_checkboxes[i].config(text=opt)
            self.options_vars[i].set(False)  # Uncheck all checkboxes when loading a new question
            self.option_checkboxes[i].pack()

        for i in range(len(options), 5):
            self.option_checkboxes[i].pack_forget()

    def reveal_answer(self):
        question_data = self.questions[self.current_question_index]
        correct_answer = question_data['Correct Answer']
        correct_index = ord(correct_answer) - 65
        messagebox.showinfo("Correct Answer", f"The correct answer is: {question_data[f'Option {correct_answer}']}")
        selected_options = [var.get() for var in self.options_vars]
        self.user_answers[self.current_question_index] = selected_options

    def next_question(self):
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
            self.show_question()

    def previous_question(self):
        if self.current_question_index > 0:
            self.current_question_index -= 1
            self.show_question()

    def finish_quiz(self):
        answered_questions = sum(1 for answer in self.user_answers if any(answer))
        correct_answers = sum(1 for i, answer in enumerate(self.user_answers) if answer and answer[ord(self.questions[i]['Correct Answer']) - 65])
        incorrect_answers = answered_questions - correct_answers
        messagebox.showinfo("Quiz Summary", f"Total Questions: {len(self.questions)}\nQuestions Answered: {answered_questions}\nCorrect Answers: {correct_answers}\nIncorrect Answers: {incorrect_answers}")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the root window while asking for file

    # Ask user for the CSV file name
    csv_file = simpledialog.askstring("Input", "Please enter the CSV file name (including .csv extension):")

    if csv_file:
        app = QuizApp(root, csv_file)
        root.deiconify()  # Show the main window once the file is provided
        root.mainloop()
    else:
        messagebox.showwarning("Warning", "No file name provided. Exiting.")
