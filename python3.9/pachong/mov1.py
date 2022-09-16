#!/usr/bin/env python3

import sys, requests
from urllib import request





def main():
	url = 'https://api.okjx.cc:3389/jx.php?url=https://v.youku.com/v_show/id_XNTExODgyMTcyMA==.html?tpa=dW5pb25faWQ9MTAzNzUzXzEwMDAwMV8wMV8wMQ'
	
	mp4 = requests.get(url).content
	
	with open('秦时明月/23.mp4', 'wb') as f:
		f.write(mp4)


if __name__ == "__main__":
	main()