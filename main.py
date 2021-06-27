from __future__ import annotations
from moviepy.video import VideoClip
from moviepy.video.VideoClip import ImageClip
from moviepy.editor import VideoFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip

from logo import add_logo




video_clip = VideoFileClip('resources/IMG_9941.MOV').subclip(0, 1)

video_clip = add_logo(video_clip)


video_clip.write_videofile("output.mp4", temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")