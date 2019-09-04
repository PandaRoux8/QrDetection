"""
QR Detection
Name    :   Schluchter Jules
Class   :   INF/EE 3
Date    :   04.09.2019
Desc    :   Get the frame from the camera and detect QR code, display them in a text box.
"""
from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import cv2
import datetime
from PIL import Image


def start_camera_capture(video, view, root):
    datas = []
    while True:
        check, frame = video.read()
        img = Image.fromarray(frame)
        decoded_image = decode(img)
        data = decoded_image.get('data')

        if data:
            now = datetime.datetime.now()
            str_now = now.strftime("%d/%m/%Y, %H:%M:%S")
            print("%s %s" % (data, str_now))

        if data and data not in datas:
            datas.append(data)
            now = datetime.datetime.now()
            number = "N° : %-50s" % data.decode()
            date = "Date : %s \n" % now.strftime("%d/%m/%Y, %H:%M:%S")
            data_str = number + date
            view.log_camera.configure(state='normal')
            view.log_camera.insert('end', data_str)
            view.log_camera.configure(state='disabled')
            root.update()

        # Affiche la vue de la camera
        cv2.imshow("Capture", frame)
        if cv2.waitKey(1) == 27:
            view.quit()
            break  # esc to quit


def decode(img):
    # Trouve le QR code
    decoded_image = pyzbar.decode(img)

    res = {}
    for obj in decoded_image:
        res = {
            'type': obj.type,
            'data': obj.data,
        }

    return res


def start(index_camera, view, root):
    #  Index de la camera a utilisé -> 1 parce que 2 camera sur PC portable
    video = cv2.VideoCapture(index_camera)
    start_camera_capture(video, view, root)
    video.release()


def check_available_camera():
    available_cam = ""
    for i in range(20):
        cam = cv2.VideoCapture(i)
        if cam.isOpened():
            if i == 0:
                available_cam += "%s" % str(i)
            else:
                available_cam += ", %s" % str(i)

    return available_cam
