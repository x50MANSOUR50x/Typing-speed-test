import tkinter as tk
from tkinter import *
import pandas as pd
from random import choice
import time
from tkinter import messagebox

start_time = None

def check_wbm():
    """Calculate and display words per minute."""

    global start_time

    counter = 0

    text = text_entry.get("1.0", "end-1c")

    if start_time is None:
        messagebox.showwarning("Warning", "Start typing first!")
        return

    if len(text) < len(sample_text):
        messagebox.showwarning("Warning", "The sentence isn't complete")
        return


    final_time = time.time() - start_time

    # print(final_time)

    word_count = len(text.split(" "))

    wpm = ((word_count / final_time) * 60)
    # print(text)
    for index in range(len(sample_text)):
        if not(sample_text[index] == text[index]):
            counter += 1
    # print(counter)

    accuracy = round(100 - (counter/len(sample_text)) * 100, 2)

    result_text = f"{wpm:.0f} wpm"

    if wpm < 40:
        result_text += "\nKeep practicing to improve your speed!"
    elif wpm >= 100:
        result_text += "\nExcellent typing speed!"
    else:
        result_text += "\nGood job! Keep going!"

    result_text += f"\nYou missed { counter } letters, and your accuracy is { accuracy }%"

    tk.messagebox.showinfo("Typing Speed Result", result_text)

def start_typing(event=None):
    """Record the start time when user begins typing."""

    global start_time
    start_time = time.time()




text_data = pd.read_csv("sample_texts.csv")
text_data_list = list(text_data['sample_text'])

sample_text = choice(text_data_list)

window = tk.Tk()
window.title("Typing speed test")
window.minsize(width=800, height=300)

text_label = tk.Label(text=f"{ sample_text }", font=("Arial", 24, "bold"))
text_label.pack()

text_entry = Text(window, height=5, width=50, font=("Arial", 14))
text_entry.bind("<FocusIn>", start_typing)
text_entry.place(x=130, y=100)

submit_button = tk.Button(text="Submit", width=10, height=3, command=check_wbm)
submit_button.place(x=368, y=230)

window.mainloop()


# print(start_time)