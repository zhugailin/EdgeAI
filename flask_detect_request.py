import json
import requests
import app_detect_yolov5
import cv2
from flask import request,make_response

def requst_yolov5_edgetpu():
    """
    
    """
    API = "http://192.168.57.159:5003/detect_edgetpu/"


    img_file = "/data/home/zgl/coral/pycoral/examples/flask_edgetpu/data/images/bus.jpg"
    img_base64 = app_detect_yolov5.img2base64(cv2.imread(img_file))

    send_data = json.dumps(img_base64)
    # out_data = app_detect_yolov5.base642img(img_base64) 
    # print (out_data)

    res = requests.post(url=API, data=send_data).json()
    # print("------------------------------")
    # print (res)
    for s in res:
        if s != "img_result":
            print(s,":",res[s])
    print("------------------------------")
if __name__ == '__main__':

    requst_yolov5_edgetpu()
