#!/usr/bin/env python3

# import tkinter as Tk
import requests
from urllib import request
import sys



def dd(d):
  print(d)
  sys.exit()

def main(url):
  data = requests.get(url).content
  with open('mov/xyy.mp4', 'wb') as f:
    f.write(data)

if __name__ == "__main__":
  print(sys.version)
  #url = "https://vd2.bdstatic.com/mda-kdhjrgxav13uv0ah/sc/mda-kdhjrgxav13uv0ah.mp4?v_from_s=tc_haokan_4469&auth_key=1620377794-0-0-323d6c16a67c7d727467e7ba0499c18b&bcevod_channel=searchbox_feed&pd=1&pt=3&abtest=3000165_2"
  #main(url)
