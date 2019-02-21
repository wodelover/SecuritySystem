# -*- coding:utf-8 -*-
"""
此文件的功能是服务端代码，用于接收客户端传来的图像数据并进行保存
"""

from flask import Flask, request
import os

app = Flask(__name__)

# 定义保存图像文件的路径文件夹
image_filepath = "./upload/"
listenIp = "127.0.0.1"
listenPort = 9999

@app.route('/json', methods = ['POST'])
def my_json():
    upload_file = request.files['image']
    old_file_name = upload_file.filename
    if upload_file:
        file_path = os.path.join(image_filepath, old_file_name)
        upload_file.save(file_path)
        return 'save successful'


if __name__ == '__main__':
    app.run(listenIp, port = listenPort)
