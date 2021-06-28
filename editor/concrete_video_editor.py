from __future__ import annotations
from video_editor.video_editor import VideoEditor
from moviepy.video import VideoClip
from moviepy.video.VideoClip import ImageClip
from moviepy.editor import VideoFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.fx.all import resize


in_test = True


class ConcreteVideoEditor(VideoEditor):
    def __init__(self, filepath: str):
        self.video_clip = VideoFileClip(filepath)

        if in_test:
            self.video_clip = self.video_clip.subclip(0, 1)

    def add_logo(self, logo_filepath: str):

        def _calculate_logo_width_height(main_video: VideoClip) -> tuple[int, int]:
            SCALE_FACTOR: int = 1 / 5
            return main_video.w * SCALE_FACTOR, main_video.h * SCALE_FACTOR

        logo_clip = ImageClip(logo_filepath, duration=self.video_clip.duration)

        logo_width, logo_height = _calculate_logo_width_height(self.video_clip)
        logo_clip = logo_clip.fx(resize, width=logo_width, height=logo_height)

        self.video_clip = CompositeVideoClip([self.video_clip, logo_clip])

    def add_lower_thirds(self, name: str, bureau: str):
        pass

    def upload_to_youtube(self, video_name: str):
        pass

    def write_file(self, name: str):
        self.video_clip.write_videofile(name, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")
