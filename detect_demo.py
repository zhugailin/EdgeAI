import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from edgetpumodel import EdgeTPUModel

if __name__ == "__main__":
    #加载模型
    model_path= 'yolov5s-int8-224.tflite' 
    conf_thresh = 0.5
    iou_thresh = 0.45
    label_name = 'data/coco.yaml'
    image_path = 'data/images/bus.jpg'
    model = EdgeTPUModel(model_path, label_name, conf_thresh, iou_thresh)
    logger.info("-----------------Testing on image-------------------------")
    det, output = model.predict(image_path)
    print("output:",output)

