from __future__ import annotations
from moviepy.video import VideoClip
from moviepy.video.VideoClip import ImageClip
from moviepy.editor import VideoFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip

from logo import add_logo

def output_video(video_clip: VideoClip, output_filename: str):
    video_clip.write_videofile(output_filename, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")


video_editor = VideoEditor()

video_editor.add_logo().add_lower_thirds().finalize()

video_editor.add_lower_thirds(name='Klaudine Caday', bureau='Florida')

video_editor.finalize('output.mp4')


video_clip = VideoFileClip('resources/IMG_9941.MOV').subclip(0, 1)

video_clip = add_logo(video_clip)

output_video(video_clip, 'output.mp4')

