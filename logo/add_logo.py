from __future__ import annotations
from moviepy.video import VideoClip
from moviepy.video.VideoClip import ImageClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.fx.all import resize

def _calculate_logo_width_height(main_video: VideoClip) -> tuple[int, int]:
    SCALE_FACTOR: int = 1 / 5
    return main_video.w * SCALE_FACTOR, main_video.h * SCALE_FACTOR

def add_logo(video_clip: VideoClip) -> VideoClip:
    logo_clip = ImageClip('resources/logo.png', duration=video_clip.duration)

    logo_width, logo_height = _calculate_logo_width_height(video_clip)
    logo_clip = logo_clip.fx(resize, width=logo_width, height=logo_height)

    return CompositeVideoClip([video_clip, logo_clip])