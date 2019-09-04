"""
QR Detection
Name    :   Schluchter Jules
Class   :   INF/EE 3
Date    :   04.09.2019
"""
from tkinter import Tk
from view import QrCamSelection

if __name__ == '__main__':
    view = Tk()
    my_gui = QrCamSelection(view)
    view.mainloop()
