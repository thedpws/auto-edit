from .video_host import VideoHost

class YouTube(VideoHost):

    def upload_private(filepath: str, title=None, description=None, tags=None) -> str:
        print(f'TODO: upload ${filepath} to YouTube')
