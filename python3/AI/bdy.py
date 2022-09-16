#!/usr/bin/env python3

from aip import AipFace
import base64

APP_ID = "16646161"
APP_KEY = "X6G7DGNEErj35nkm0YvruODa"
SECRET_KEY = "3QYKfubQoqST7GCQEmKQP4kaM5WOfgOr"

client = AipFace(APP_ID, APP_KEY, SECRET_KEY)

file_name = './123.jpg'
with open(file_name, 'rb') as fb:
	data = base64.b64encode(fb.read())
	
img = data.decode()

res = client.detect(img, 'BASE64')

print(res)