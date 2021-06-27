from __future__ import annotations
from moviepy.video import VideoClip
from moviepy.video.VideoClip import ImageClip
from moviepy.editor import VideoFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.fx.all import resize


def calculate_logo_width_height(main_video: VideoClip) -> tuple[int, int]:
    SCALE_FACTOR: int = 1 / 5
    return main_video.w * SCALE_FACTOR, main_video.h * SCALE_FACTOR


video_clip = VideoFileClip('resources/IMG_9941.MOV').subclip(0, 1)

logo_clip = ImageClip('resources/logo.png', duration=video_clip.duration)

logo_width, logo_height = calculate_logo_width_height(video_clip)
logo_clip = logo_clip.fx(resize, width=logo_width, height=logo_height)

final_clip = CompositeVideoClip([video_clip, logo_clip])

final_clip.write_videofile("output.mp4", temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")