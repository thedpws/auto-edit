from moviepy.video import VideoClip
from moviepy.video.VideoClip import ImageClip
from moviepy.editor import VideoFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.fx.all import resize


video_clip = VideoFileClip('resources/IMG_9941.MOV').subclip(0, 1)

logo_clip = ImageClip('resources/logo.png', duration=video_clip.duration)
logo_clip = logo_clip.fx(resize, width=100, height=100)

final_clip = CompositeVideoClip([video_clip, logo_clip])

final_clip.write_videofile("output.mp4", temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")