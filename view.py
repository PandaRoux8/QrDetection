"""
QR Detection
Name    :   Schluchter Jules
Mail    :   jules.schluchter@gmail.com
Date    :   04.09.2019
Desc    :   Create the views for the program
"""

from tkinter import Tk, Label, Button, Entry, Text
from number_detection import check_available_camera
from number_detection import NumberDetection


class QrCamSelection:

    def __init__(self, view):
        self.view = view
        view.title("QR Cam Selection")
        # Place the window in the center of the screen
        window_width = view.winfo_reqwidth()
        window_height = view.winfo_reqheight()
        width = int(view.winfo_screenwidth())
        # If double screen
        if width > 1980:
            width = width / 2
        position_right = int(width / 2 - window_width / 2)
        position_down = int(view.winfo_screenheight() / 2 - window_height / 2)
        view.geometry("+{}+{}".format(position_right, position_down))

        self.cam_selection_view()

    def cam_selection_view(self):
        self.label = Label(self.view, text="Sélectionner l'index de la camera dans la liste ci-dessous")
        self.label.pack()

        available_cam_index = check_available_camera()
        self.av_cam = Label(self.view)
        self.av_cam.pack()
        self.av_cam['text'] = available_cam_index

        self.camera_index = Entry(self.view)
        self.camera_index.pack()

        self.validate = Button(self.view, text="Valider", command=self.validate)
        self.validate.pack()

    def validate(self):
        camera_index = int(self.camera_index.get())
        self.view.destroy()
        QrDetection(camera_index)


class QrDetection:

    def __init__(self, camera_index):
        self.view = Tk()
        # Place the window in the center of the screen
        window_width = self.view.winfo_reqwidth()
        window_height = self.view.winfo_reqheight()
        width = int(self.view.winfo_screenwidth())
        if width > 1980:
            width = width / 2
        position_right = int(width / 2 - window_width / 2)
        position_down = int(self.view.winfo_screenheight() / 2 - window_height / 2)
        self.view.geometry("+{}+{}".format(position_right, position_down))

        # self.view.wm_attributes('-type', 'splash')
        self.qr_selection_view()
        NumberDetection(self, self.view, camera_index)

    def qr_selection_view(self):
        self.view.title("QR Detection")
        self.log_camera = Text(self.view, state='disabled')
        self.log_camera.configure(font=("Arial", 14))
        self.log_camera.pack()

        self.last_nb = Label(self.view)
        self.last_nb.pack()

    def quit(self):
        self.view.destroy()
