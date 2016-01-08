from tkinter import *
from tkinter import filedialog

def call_file():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title='Choose an image')

    return file_path
