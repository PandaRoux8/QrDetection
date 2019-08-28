from tkinter import Tk, Label, Button, Entry, Text
from number_detection import start


class QrDetectionView:

    def __init__(self, master):
        self.master = master
        master.title("QR Detection")

        self.label = Label(master, text="Entrez index de la camera 0 à 5 surement")
        self.label.pack()

        self.camera_index = Entry(master)
        self.camera_index.pack()

        self.validate = Button(master, text="Valider", command=self.validate)
        self.validate.pack()

        self.log_camera = Text(master, state='disabled')
        self.log_camera.pack()

        self.last_nb = Label(master)
        self.last_nb.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def validate(self):
        start(int(self.camera_index.get()), self, self.master)


if __name__ == '__main__':
    root = Tk()
    my_gui = QrDetectionView(root)
    root.mainloop()