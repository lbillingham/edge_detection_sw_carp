from tkinter import *
from tkinter import filedialog

def call_file():
    '''
    User chooses image from pop-up and filepath is returned
    
    Note, pop-up currently appears behind browser
    '''
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title='Choose an image')

    return file_path
