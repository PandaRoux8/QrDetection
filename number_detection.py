from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import cv2
import os
import datetime
from PIL import Image
# from view import root


def check_camera(video, view, root):
    datas = []
    while True:
        check, frame = video.read()
        img = Image.fromarray(frame)
        decoded_image = decode(img)
        data = decoded_image.get('data')

        if data:
            now = datetime.datetime.now()
            str_now = now.strftime("%m/%d/%Y, %H:%M:%S")
            print("%s %s" % (data, str_now))

        if data and data not in datas:
            datas.append(data)
            data_str = "%s%s" % (data.decode(), '\n')
            view.log_camera.configure(state='normal')
            view.log_camera.insert('end', data_str)
            view.log_camera.configure(state='disabled')
            root.update()
            # view.update_gui()
            # camera_label['text'] = data
            file = open("qr_data.txt", "a+")
            now = datetime.datetime.now()
            file.write("N° : %s; Date : %s \n" % (data.decode(), now))
            file.close()

        # Affiche la vue de la camera
        cv2.imshow("Capture", frame)
        if cv2.waitKey(1) == 27:
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
# if __name__ == '__main__':
    #  Index de la camera a utilisé -> 1 parce que 2 camera sur PC portable
    # TODO : Automate this try 1 to 10
    video = cv2.VideoCapture(index_camera)
    check_camera(video, view, root)
    video.release()
