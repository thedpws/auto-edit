from __future__ import annotations
from moviepy.video import VideoClip
from editor import ConcreteVideoEditor, VideoEditor
from host import YouTube, VideoHost
from outlet import VideoOutlet, AzTelegram


def main():
    video_editor: VideoEditor = ConcreteVideoEditor('resources/IMG_9941.MOV')

    video_editor.add_logo('resources/logo.png')

    video_editor.add_lower_thirds(name='Aaaaa Bbbbb', bureau='Florida')

    video_editor.add_closer('resources/ffc2.mp4')

    video_editor.write_file('output.mp4')

    youtube: VideoHost = YouTube()

    video_url: str = youtube.upload_private('output.png')

    outlet: VideoOutlet = AzTelegram()

    outlet.share_video_url(video_url)


if __name__=='__main__':
    main()
