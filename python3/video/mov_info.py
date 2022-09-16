from moviepy.editor import VideoFileClip
import os

mov_path = './../pachong/mov/xyy.mp4'
clip = VideoFileClip(mov_path)
mov_size = os.path.getsize(mov_path)
mov_size = mov_size/1024
print(1024**3)
