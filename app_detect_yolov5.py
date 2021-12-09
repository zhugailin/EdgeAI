import numpy as np
import base64
import os
import time
import cv2
import json

def base642img(img_base64):
    """
    输入base64格式数据，转为numpy的int数据。
    """
    img = base64.b64decode(str(img_base64))
    img = np.fromstring(img, np.uint8)
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    return img

def img2base64(img):
    """
    numpy的int数据转换为base64格式。
    """
    retval, buffer = cv2.imencode('.jpg', img)
    img_base64 = base64.b64encode(buffer)
    img_base64 = img_base64.decode()
    return img_base64
    


# if __name__ == '__main__':

    # img_file = "/data/home/zgl/coral/pycoral/examples/flask_edgetpu/data/images/bus.jpg"
    # img = cv2.imread(img_file, 0)
    # cv2.imwrite(img_file[:-4] + "_gray2d.jpg", img)
