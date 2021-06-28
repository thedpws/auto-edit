from __future__ import annotations
from video_editor.video_editor import VideoEditor
from moviepy.video import VideoClip
from moviepy.video.VideoClip import ImageClip
from moviepy.editor import VideoFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip

from logo import add_logo


class ConcreteVideoEditor(VideoEditor):
    def add_logo(self, logo_filepath: str):

    def add_lower_thirds(self, name: str, bureau: str):
        pass

    def write_file(self, name: str):
        video_clip.write_videofile(name, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")


video_clip = VideoFileClip('resources/IMG_9941.MOV').subclip(0, 1)

video_clip = add_logo(video_clip)

output_video(video_clip, 'output.mp4')

