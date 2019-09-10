"""
QR Detection
Name    :   Schluchter Jules
Mail    :   jules.schluchter@gmail.com
Date    :   04.09.2019
"""
from tkinter import Tk
from view import QrCamSelection

if __name__ == '__main__':
    view = Tk()
    my_gui = QrCamSelection(view)
    view.mainloop()
