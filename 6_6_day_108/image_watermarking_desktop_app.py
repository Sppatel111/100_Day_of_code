from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

from PIL import Image, ImageDraw, ImageFont

FONT_NAME = "Sans serif fonts"
PINK = "#F7CFD8"
CREAM = "#EDE8DC"

window = Tk()

window.title('Image watermarking')
window.config(padx=25, pady=25)

img_file = ''


def watermark(input, output, t_watermark, xy_pos):
    image = Image.open(input)
    edit_image = ImageDraw.Draw(image)


    font_watermark = ImageFont.truetype("arial.ttf", 200)
    edit_image.text(xy_pos, t_watermark, font=font_watermark, fill='#B5828C')
    image.show()
    image.save(output)


def select_file():
    global img_file
    img_file = askopenfilename()


def watermark_img():
    if img_file == '':
        messagebox.showerror("No image found", "Please select an image first.")
    else:
        output = f'watermarked.jpg'
        t_watermark = text_entry.get()
        watermark(img_file, output, t_watermark=t_watermark, xy_pos=(100, 100))
        messagebox.showinfo('complete', 'succesfully watermarked!')


title_label = Label(text='Img Watermark ', font=(FONT_NAME, 50, "bold"), fg=PINK, bg=CREAM)
title_label.grid(column=0, row=1, rowspan=4)

b1 = Button(window, text='1.select img', font=20, width=15, command=select_file)
b1.grid(column=1, row=1, columnspan=2, padx=25, pady=25)

b2 = Button(window, text='3. watermark img', font=20, width=15, command=watermark_img)
b2.grid(column=1, row=4, columnspan=2, padx=25, pady=25)

text_label = Label(text="2.watermark text ")
text_label.grid(column=1, row=2, padx=25, pady=25)
text_entry = Entry(width=26)
text_entry.grid(column=1, row=3)

window.mainloop()
