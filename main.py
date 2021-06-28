from __future__ import annotations
from moviepy.video import VideoClip
from video_editor import ConcreteVideoEditor, VideoEditor


def main():
    video_editor: VideoEditor = ConcreteVideoEditor('resources/IMG_9941.MOV')

    video_editor.add_logo('resources/logo.png')

    video_editor.add_lower_thirds(name='Aaaaa Bbbbb', bureau='Florida')

    video_editor.add_closer()

    video_editor.write_file('output.mp4')


if __name__=='__main__':
    main()
