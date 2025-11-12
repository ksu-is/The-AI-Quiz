from tkinter import messagebox
import tkinter as tk
from tkinter import *
import string
import random

# Functions
def open_about_page():
    messagebox.showinfo("About", "A Python application to test users on verifying if they are Human or AI.")

def show_frame(frame):
    frame.tkraise()

def on_checkbox():
    if checked.get():
        print("Checkbox is checked!")
    else:
     print("Checkbox is unchecked!")
    
def show_text():
    print("You typed:", entry.get())

def check_answer():
    user_input_text = entry.get().strip() 
    if user_input_text == "XMYVN6W5":
        open_about_page()
    else:
        show_frame(AI_box)
    

# Homepage
root = tk.Tk()
root.title("The-AI-Quiz")
root.geometry("400x300")
root.configure(bg="#f0f0f0")


root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Frames
main_frame = tk.Frame(root, bg="#f0f0f0")
quiz1_frame = tk.Frame(root, bg="#e0f7fa")
quiz2_frame = tk.Frame(root, bg="#e0f7fa")
AI_box = tk.Frame(root, bg="#ff8e8e")
word_frame = tk.Frame(root, bg="#d9d9d9")

for frame in (main_frame, AI_box, quiz1_frame, quiz2_frame, word_frame):
    frame.grid(row=0, column=0, sticky='nsew')

show_frame(main_frame)

# Main Buttons
title_label = tk.Label(main_frame, text="The-AI-Quiz!", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
title_label.pack(pady=20)

desc_label = tk.Label(main_frame, text="Choose an option below to get started:", bg="#f0f0f0")
desc_label.pack(pady=10)

start_button = tk.Button(main_frame, text="Start", width=15, command=lambda: show_frame(quiz1_frame))
start_button.pack(pady=5)

about_button = tk.Button(main_frame, text="About", width=15, command=open_about_page)
about_button.pack(pady=5)

exit_button = tk.Button(main_frame, text="Exit", width=15, command=root.destroy)
exit_button.pack(pady=5)

# Quiz1 Buttons
quiz1_label = tk.Label(quiz1_frame, text="I'm not a robot:", font=("Helvetica", 14, "bold"), bg="#e0f7fa")
quiz1_label.pack(pady=20)

checked = tk.BooleanVar()
checkbox = tk.Checkbutton(quiz1_frame, text="Check me!", variable=checked, bg="#e0f7fa", command=lambda: show_frame(quiz2_frame))
checkbox.pack(pady=10)

back_button = tk.Button(quiz1_frame, text="Exit", width=10, command=lambda: show_frame(main_frame))
back_button.pack(pady=10)

# Quiz2 Buttons
quiz2_label = tk.Label(quiz2_frame, text="What did you do yesterday?", font=("Helvetica", 14, "bold"), bg="#e0f7fa")
quiz2_label.pack(pady=20)

idont_button = tk.Button(quiz2_frame, text="I don't know", width=15, command=lambda: show_frame(AI_box)) 
idont_button.pack(pady=5)

Walked_button = tk.Button(quiz2_frame, text="I walked", width=15, command=lambda: show_frame(word_frame))
Walked_button.pack(pady=5)

AI_top = tk.Label(AI_box, text="AI", font=("Helvetica", 20, "bold"), bg="#ff8e8e")
AI_top.pack(pady=10)

AI_text = tk.Label(AI_box, text="You are an AI, you must leave!", font=("Helvetica", 14, "bold"), bg="#ff8e8e")
AI_text.pack(pady=20)

AI_exit_button = tk.Button(AI_box, text="Exit", width=15, command=root.destroy)
AI_exit_button.pack(pady=10)

# Word Frame
word_label = tk.Label(word_frame, text="Write out the letters in the text box.", font=("Helvetica", 15, "bold"), bg="#d9d9d9")
word_label.pack(pady=10)

IM_photo = tk.PhotoImage(file=r"Documents\Github\The-AI-Quiz\XM.png")
IM_label = tk.Label(word_frame, image=IM_photo, bg="#d9d9d9")
IM_label.image = IM_photo
IM_label.pack() 

entry = tk.Entry(word_frame, width=30) 
entry.pack(padx=10, pady=5)
entry.insert(0, "")

text1_button = tk.Button(word_frame, text="Submit", command=check_answer)
text1_button.pack(padx=10, pady=5)

#show_frame(main_frame)

root.mainloop()



# Question 1
#answer = input("When was the first known use of the word 'quiz'? ")
#if answer == "1781":
    #print("Correct!")
#else:
    #print(f"The answer is '1781', not {answer!r}")

# Question 2
#answer = input("Which built-in function can get information from the user? ")
#if answer == "input":
    #print("Correct!")
#else:
   # print(f"The answer is 'input', not {answer!r}")

# Question 3
#QUESTIONS = {
   # "When was the first known use of the word 'quiz'": [
      #  "1781", "1771", "1871", "1881"
  #  ],
  #  "Which built-in function can get information from the user": [
  #      "input", "get", "print", "write"
  #  ],
   # "Which keyword do you use to loop over a given list of elements": [
    #    "for", "while", "each", "loop"
   # ],
   # "What's the purpose of the built-in zip() function": [
    #    "To iterate over two or more sequences at the same time",
     #   "To combine several strings into one",
     #   "To compress several files into one archive",
     #   "To get information from the user",
  #  ],
#}
#for question, alternatives in QUESTIONS.items():
   # correct_answer = alternatives[0]
  #  for alternative in sorted(alternatives):
    #    print(f"  - {alternative}")

   # answer = input(f"{question}? ")
   # if answer == correct_answer:
    #    print("Correct!")
    #else:
    #    print(f"The answer is {correct_answer!r}, not {answer!r}")

