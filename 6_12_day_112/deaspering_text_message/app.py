from tkinter import *

window=Tk()
window.title('Type flow app')
window.config(padx=25,pady=25)
count=0
def check_text():
    global count,current_text
    if len(text_entry.get())> 0 and text_entry.get()==current_text:
        message_label.config(text=f'Deleting in: {count}')
        if count ==0:
            text_entry.delete(0,END)
            message_label.config(text='stat again...')
            window.after(1000,check_text)

        else:
            window.after(1000,check_text)
            count-=1
    else:
        current_text=text_entry.get()
        print(current_text)
        count=5
        window.after(1000,check_text)


current_text=''

title_label=Label(text='Type flow app')
title_label.grid(column=0,row=0)
message_label=Label(text='start Typing')
message_label.grid(column=0,row=1)
text_entry=Entry()
text_entry.grid(column=0,row=2,pady=30)
text_entry.focus()

check_text()

window.mainloop()