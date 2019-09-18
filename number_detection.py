"""
QR Detection
Name    :   Schluchter Jules
Mail    :   jules.schluchter@gmail.com
Date    :   04.09.2019
Desc    :   Get the frame from the camera and detect QR code, display them in a text box.
"""
from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import cv2
import datetime
from datetime import timedelta
import time
from PIL import Image

CHECK_TOUR_TIME = 3


class NumberDetection(object):

    def __init__(self, view, root, index_camera):
        self.view = view
        self.root = root
        # Index of the camera to use
        video = cv2.VideoCapture(index_camera)
        self.start_camera_capture(video)
        video.release()

    def start_camera_capture(self, video):
        datas = {}  # Dict to store the number detected with the time when it was detected
        while True:
            check, frame = video.read()
            # Change image data from array to PIL Image
            img = Image.fromarray(frame)
            decoded_image = self.decode(img)
            # Get the QR decoded by pyzbar
            data = decoded_image.get('data')
            # Logging debug to see every QR code detected in the image
            # if data:
            #     number = "N° : %s" % data.decode()
            #     now_date = datetime.datetime.now()
            #     date = "Date : %s" % now_date.strftime("%d/%m/%Y, %H:%M:%S")
            #     data_str = number + date
            #     print(data_str)

            now = datetime.datetime.now()
            if data and data not in datas.keys():
                start_time = time.time()
                self.view.log_camera.configure(state='normal')
                self.view.log_camera.insert('end', "N° %s a débuté la course.\n" % data)
                self.view.log_camera.configure(state='disabled')
                self.root.update()
                datas.update({data: {
                        'last_time': start_time,
                        'time': CHECK_TOUR_TIME+1,
                        'tour': 0,
                    }
                })
                print("1", datas)

            # Check every x seconds
            now_time = time.time()
            if data and data in datas.keys():
                print(int(now_time - datas[data]['last_time']) , int(now_time - datas[data]['last_time']) > CHECK_TOUR_TIME)

            if data and data in datas.keys() and int(now_time - datas[data]['last_time']) > CHECK_TOUR_TIME:
                last_time = datas[data]['last_time']

                datas.update({data: {
                        'last_time': now_time,
                        'time': now_time - last_time,
                        'tour': datas[data]['tour'] + 1,
                    }
                })
                # TODO : CHeck this
                # data_str = "N° %s Time : %s Tour : %s\n" % (data.decode(), datas[data]['time'], datas[data]['tour'])
                # self.view.log_camera.configure(state='normal')
                # self.view.log_camera.insert('end', data_str)
                # self.view.log_camera.configure(state='disabled')
                # self.root.update()
                # with open("qr_data.txt", "a+") as f:
                #     f.write(data_str)

            # Display camera frames
            cv2.imshow("Capture", frame)
            if cv2.waitKey(1) == 27:
                self.view.quit()
                break  # esc to quit

    @staticmethod
    def decode(img):
        # Detect a QR code on an image
        decoded_image = pyzbar.decode(img)

        res = {}
        for obj in decoded_image:
            res = {
                'type': obj.type,
                'data': obj.data,
            }

        return res


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
