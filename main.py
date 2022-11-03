import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageDraw, ImageFont

window = tk.Tk()

# initialization of window
window.geometry("800x600")
window.title("Carlos' Watermarking App")

# Creating GUI
font = ('times', 18, 'bold')
small_font = ('times', 12)
l1 = tk.Label(window, text='Upload File & Create Watermark Image', width=50, font=font)
l1.grid(row=1, column=1)
in1 = tk.Entry(window, width=50, font=font)
in1.insert(0, 'Enter Watermark Text')
in1.grid(row=2, column=1)
rl = tk.Label(window, text='R', width=16, font=small_font)
rl.grid(row=4, column=0)
gl = tk.Label(window, text='G', width=16, font=small_font)
gl.grid(row=4, column=1)
bl = tk.Label(window, text='B', width=16, font=small_font)
bl.grid(row=4, column=2)
r_in = tk.Entry(window, width=16, font=font)
r_in.insert(0, 'Enter Red Value')
r_in.grid(row=5, column=0)
g_in = tk.Entry(window, width=16, font=font)
g_in.insert(0, 'Enter Green Value')
g_in.grid(row=5, column=1)
b_in = tk.Entry(window, width=16, font=font)
b_in.insert(0, 'Enter Blue Value ')
b_in.grid(row=5, column=2)
b1 = tk.Button(window, text='Watermark with String', width=20, command=lambda: create_watermark_image())
b1.grid(row=6, column=1)
b2 = tk.Button(window, text='Watermark with Logo', width=20, command=lambda: create_watermark_image_with_logo())
b2.grid(row=7, column=1)


def create_watermark_image():
    img = filedialog.askopenfilename()
    im = Image.open(img)
    image_height = round(im.height * 0.8)
    image_width = round(im.width * 0.8)
    watermark_font = ImageFont.truetype("arial.ttf", size=90)
    watermark = ImageDraw.Draw(im)
    watermark.text((image_width * 0.9, image_height * 0.9), f"{in1.get()}", font=watermark_font, fill=(int(r_in.get()), int(g_in.get()), int(b_in.get())))
    im.show()


def create_watermark_image_with_logo():
    img = filedialog.askopenfilename()
    logo = filedialog.askopenfilename()
    background = Image.open(img)
    logo_im = Image.open(logo)
    image_height = round(background.height * 0.8)
    image_width = round(background.width * 0.8)
    background.paste(logo_im, (image_width, image_height))
    background.show()

window.mainloop()

