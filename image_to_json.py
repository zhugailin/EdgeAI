# 导入相关的库
from sys import argv
from base64 import b64encode
from json import dumps

ENCODING = 'utf-8'    # 指定编码形式
SCRIPT_NAME, IMAGE_NAME, JSON_NAME = argv    # 获得文件名参数

# 读取二进制图片，获得原始字节码，注意 'rb'
with open(IMAGE_NAME, 'rb') as jpg_file:
    byte_content = jpg_file.read()
# 把原始字节码编码成 base64 字节码
base64_bytes = b64encode(byte_content)
# 将 base64 字节码解码成 utf-8 格式的字符串
base64_string = base64_bytes.decode(ENCODING)
# 用字典的形式保存数据
raw_data = {}
raw_data["name"] = IMAGE_NAME
raw_data["image_base64_string"] = base64_string
# 将字典变成 json 格式，缩进为 2 个空格
json_data = dumps(raw_data, indent=2)
# 将 json 格式的数据保存到文件中
with open(JSON_NAME, 'w') as json_file:
    json_file.write(json_data)