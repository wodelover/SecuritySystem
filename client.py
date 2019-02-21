# -*- coding:UTF-8 -*-
"""
此文件的作用是定时拍照并实时上传图片进行显示
文件的执行步骤:
	1、拍照保存;
	2、文件发送;
	3、人体检测-->拍照时间调整;
	4、气体检测-->拍照时间调整;

需要执行此命令：
	 sudo apt-get install python-rpi.gpio
"""
import requests
import time
import os
# 服务器地址
server_url = 'http://127.0.0.1:9999/json'
# 图像路径
image_path = 'test.jpg'
# 间隔时间,毫秒为单位
duration_time = 1000
# 定义拍照脚本文件
capture_file = 'capture_image.sh'

# 1、拍照保存
def captureImage():
	if os.path.exists(capture_file):
		os.popen(capture_file)
	else:
		print("capture image shell file does not exist.")

# 2、文件发送
def sendImage():
	img = {'image': (image_path, open(image_path, 'rb'), 'image/jpg')}
	r = requests.post(server_url, files = img)
	print("post result:", r)

# 3、人体检测
def peopleDetection():
	pass

# 4、气体检测
def gasDetection():
	pass


# 循环检测
while 1:
	# 1、拍照保存
	captureImage()
	
	# 2、文件发送
	sendImage()
	
	# 3、人体检测
	peopleDetection()
	
	# 4、气体检测
	gasDetection()
	
	# 5、延时
	time.sleep(duration_time/1000)
	print("+++")
