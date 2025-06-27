import random
import tkinter.messagebox
from tkinter import *
from timeit import default_timer as timer
from words import word_list

RANDOM_WORD = random.choice(word_list)
WORDS_TYPED=0
start_time =None

window = Tk()

window.title('Typing Speed Test')

title_label = Label(text='Typing Test')
title_label.place(relx=0.5, rely=0.1, anchor=CENTER)

word_label = Label(text=f"{RANDOM_WORD}")
word_label.place(relx=0.5, rely=0.5, anchor=CENTER)

def change_word():
    global RANDOM_WORD
    RANDOM_WORD = random.choice(word_list)
    text_entry.delete(0, END)
    word_label.config(text=f"{RANDOM_WORD}")

def callback(sv):
    global RANDOM_WORD,WORDS_TYPED,start_time
    current_letter=(len(sv.get())-1)
    if start_time is None:
        start_time = timer()
    elapsed_time = timer() - start_time
    if elapsed_time >= 30:
        tkinter.messagebox.showinfo("Results",
                                    f"The results are in, you type at {(WORDS_TYPED / 5) / 0.5} WPM.")

        window.quit()

    if sv.get() == RANDOM_WORD:
        WORDS_TYPED += len(RANDOM_WORD)
        change_word()

    elif sv.get():
        try:
            if sv.get()[current_letter] != RANDOM_WORD[current_letter]:
                word_label.config(text=f"{RANDOM_WORD}", bg="Red")
            else:
                word_label.config(text=f"{RANDOM_WORD}",bg='white')
        except IndexError:
            word_label.config(text=f"{RANDOM_WORD}", bg="Red")

sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv:callback(sv))
text_entry = Entry(window, textvariable=sv)
text_entry.place(relx=0.5, rely=0.7, anchor=CENTER)
text_entry.focus()

window.mainloop()
