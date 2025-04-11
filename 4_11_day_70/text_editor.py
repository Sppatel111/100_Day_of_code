# Text Editor - Notepad style application that can open, edit,
# and save text documents. Optional: Add syntax highlighting and other features.
import tkinter as tk
from tkinter import scrolledtext,filedialog,messagebox

window=tk.Tk()
window.title("Text Editor")
# window.config(padx=100,pady=100)
window.minsize(width=600,height=500)

def open_file():
    file_path=filedialog.askopenfilename(defaultextension='.txt',filetypes=[("Text Files", "*.txt"),
                                                           ("All Files", "*.*")])
    try:
        with open(file_path,'r') as file:
            text_area.delete(1.0,tk.END)
            text_area.insert(tk.END,file.read())
    except Exception as e:
        messagebox.showerror("Error",f"Failed to open file{e}")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[("Text Files", "*.txt"),
                                                                               ("All Files", "*.*")])
    try:
        with open(file_path,'w') as file:
            file.write(text_area.get(1.0,tk.END))
    except Exception as e:
        messagebox.showerror("Error",f"Failed to save changes.{e}")
def exit_editor():
    window.quit()

#scrollable text
text_area=scrolledtext.ScrolledText(window,wrap=tk.WORD)
text_area.pack(expand=True,fill='both')

# menu bar
menu_bar=tk.Menu(window)
window.config(menu=menu_bar)


#file menu
#tearoff=0
file_menu=tk.Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='File',menu=file_menu)
file_menu.add_command(label='Open',command=open_file)
file_menu.add_command(label="save",command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit',command=exit_editor)



window.mainloop()