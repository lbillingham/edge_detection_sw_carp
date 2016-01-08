import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
#%matplotlib inline

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

im = plt.imread(file_path)#'image.jpg')
plt.imshow(im)
