import os

import PIL.Image
import PIL.ImageOps
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile,askopenfilename






def select_and_convert():
    dest = "C:/Users/Asus/Desktop"

    def open_file():
        f_types = [('Jpg Files', '*.jpg'), ('PNG Files', '*.png')]
        filename = askopenfilename(multiple=True,filetypes=f_types)
        return filename

    images = open_file()

    def select_destination():
        dest_path = filedialog.askdirectory()
        return dest_path

    dest = select_destination()
    wm = PIL.Image.open(os.environ.get('WATERMARK_IMG'))
    wms = wm.size

    def watermark(ipath):
        # print(type(ipath))
        im = PIL.Image.open(ipath)
        im = PIL.ImageOps.exif_transpose(im)
        name = ipath.split('/')[-1]

        ims = im.size
        # ns = (wms[0] ** 2 // ims[0], wms[1] ** 2 // ims[1])

        pos = ((ims[0] - wms[0]) // 2, (ims[1] - wms[1]) // 2)
        im.paste(wm, box=pos, mask=wm)
        im.save(f'{dest}/{name}')

    for i in images:
        # print(type(i))
        watermark(i)


root = Tk()

root.title("Watermark Your Images")
root.geometry('800x600')

lbl = Label(root, text="Select you image")
lbl.grid()


def clicked():
    lbl.configure(text="I just got clicked")


btn = Button(root, text="Click me",
             fg="red", command=select_and_convert)

btn.grid(column=1, row=0)

root.mainloop()
