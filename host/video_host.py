from abc import ABC, abstractmethod

class VideoHost(ABC):

    @abstractmethod
    def upload_private(filepath: str, title=None, description=None, tags=None) -> str:
        """Uploads the specified file with the specified title, description and tags. Privacy is PRIVATE. Returns a url to the video."""