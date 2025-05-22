import tkinter as tk
import random

def generate_questions():
    questions = []
    for _ in range(5):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        operation = random.choice(['+', '*'])
        if operation == '+':
            correct_answer = a + b
            questions.append((a, b, correct_answer, operation))
        else:
            correct_answer = a * b
            questions.append((a, b, correct_answer, operation))
    return questions

def check_answers():
    correct_count = 0
    for i in range(5):
        user_answer = entry_vars[i].get()
        if user_answer.isdigit() and int(user_answer) == questions[i][2]:
            correct_count += 1
            answer_entries[i].config(bg='lightgreen')
        else:
            answer_entries[i].config(bg='lightcoral')

    result_label.config(text=f"Количество правильных ответов: {correct_count}")

root = tk.Tk()
root.title("Тест по сложению и умножению")

questions = generate_questions()
entry_vars = []
answer_entries = []

for i, (a, b, _, operation) in enumerate(questions):
    question_label = tk.Label(root, text=f"{a} {operation} {b} = ")
    question_label.grid(row=i, column=0)

    entry_var = tk.StringVar()
    entry_vars.append(entry_var)

    answer_entry = tk.Entry(root, textvariable=entry_var)
    answer_entry.grid(row=i, column=1)
    answer_entries.append(answer_entry)

check_button = tk.Button(root, text="Проверка", command=check_answers)
check_button.grid(row=5, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=6, columnspan=2)

root.mainloop()