from tkinter import messagebox
import tkinter as tk
from tkinter import *
import string

# Functions
def open_about_page():
    messagebox.showinfo("About", "A Python application to test users on verifying if they are Human or AI.")

def show_frame(frame):
    frame.tkraise()

def on_check():
    if checked.get():
        print("Checkbox is checked!")
    else:
        print("Checkbox is unchecked!")

# Homepage
root = tk.Tk()
root.title("The-AI-Quiz")
root.geometry("400x300")
root.configure(bg="#f0f0f0")


root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Frames
main_frame = tk.Frame(root, bg="#f0f0f0")
quiz_frame = tk.Frame(root, bg="#e0f7fa")

for frame in (main_frame, quiz_frame):
    frame.grid(row=0, column=0, sticky='nsew')

# Main Buttons
title_label = tk.Label(main_frame, text="The-AI-Quiz!", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
title_label.pack(pady=20)

desc_label = tk.Label(main_frame, text="Choose an option below to get started:", bg="#f0f0f0")
desc_label.pack(pady=10)

start_button = tk.Button(main_frame, text="Start", width=15, command=lambda: show_frame(quiz_frame))
start_button.pack(pady=5)

about_button = tk.Button(main_frame, text="About", width=15, command=open_about_page)
about_button.pack(pady=5)

exit_button = tk.Button(main_frame, text="Exit", width=15, command=root.destroy)
exit_button.pack(pady=5)

# Quiz Buttons
quiz_label = tk.Label(quiz_frame, text="Verify if you're Human or AI:", font=("Helvetica", 14, "bold"), bg="#e0f7fa")
quiz_label.pack(pady=20)

checked = tk.BooleanVar()
checkbox = tk.Checkbutton(quiz_frame, text="Check me!", variable=checked, command=on_check, bg="#e0f7fa")
checkbox.pack(pady=10)

back_button = tk.Button(quiz_frame, text="Exit", width=10, command=quiz_frame.destroy)
back_button.pack(pady=10)

show_frame(main_frame)

root.mainloop()



# Question 1
answer = input("When was the first known use of the word 'quiz'? ")
if answer == "1781":
    print("Correct!")
else:
    print(f"The answer is '1781', not {answer!r}")

# Question 2
answer = input("Which built-in function can get information from the user? ")
if answer == "input":
    print("Correct!")
else:
    print(f"The answer is 'input', not {answer!r}")

# Question 3
QUESTIONS = {
    "When was the first known use of the word 'quiz'": [
        "1781", "1771", "1871", "1881"
    ],
    "Which built-in function can get information from the user": [
        "input", "get", "print", "write"
    ],
    "Which keyword do you use to loop over a given list of elements": [
        "for", "while", "each", "loop"
    ],
    "What's the purpose of the built-in zip() function": [
        "To iterate over two or more sequences at the same time",
        "To combine several strings into one",
        "To compress several files into one archive",
        "To get information from the user",
    ],
}
for question, alternatives in QUESTIONS.items():
    correct_answer = alternatives[0]
    for alternative in sorted(alternatives):
        print(f"  - {alternative}")

    answer = input(f"{question}? ")
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

