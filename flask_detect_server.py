#启动带yolov5推理的flask http服务

import logging
from flask import Flask, request, jsonify
import json
from edgetpumodel import EdgeTPUModel
import argparse
from app_detect_yolov5 import base642img
import numpy as np
import cv2

import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False # 让jsonify返回的json串支持中文


@app.route("/")
def info():
    info_str = "Flask app exposing tensorflow lite model "
    return info_str

@app.route('/detect_state/', methods=['POST'])
def inspection_state():
    if request.method != 'POST':
        res = {'code': 1, 'msg': 'Only POST requests are supported!', 'data': []}
        return jsonify(res)
    else:
        res = {"code": 0}
    return jsonify(res)


@app.route("/detect_edgetpu/", methods=["POST"])
def predict():
    if request.method != 'POST':
        res = {'code': 1, 'msg': 'Only POST requests are supported!', 'data': []}
        return jsonify(res)
    else:
        data = json.loads(request.get_data(as_text=True)) #data为传送过来的Json格式文件
        # print("-------data------",data)
        img_tag = base642img(data) #对json进行解析，返回的是numpy数据
        # print ("------img_tag-------",img_tag)
        model = EdgeTPUModel(args.model, args.labels, args.conf_thresh, args.iou_thresh)  #载入模型

        det, output  = model._predict(img_tag)
        # print("-----------------------------------------------")
        # print("detect result:",output)
        # print("-----------------------------------------------")

    return jsonify(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask app exposing coral USB stick")
    parser.add_argument("--model",default='yolov5s-int8-224.tflite',help="model file",)
    parser.add_argument("--labels", default='data/coco.yaml', help="labels file of model")
    parser.add_argument("--port", default=5003, type=int, help="port number")
    parser.add_argument("--root", default='/v1/vision/coral_detect_yolov5/', help="")
    parser.add_argument("--conf_thresh", default= 0.45 , help="")
    parser.add_argument("--iou_thresh", default= 0.25 , help="")
    parser.add_argument("--url", default='192.168.57.159/', help="")
    args = parser.parse_args()
   
    app.run(host="0.0.0.0", debug=True, use_reloader=False, port=args.port)



