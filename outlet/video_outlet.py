from abc import ABC, abstractmethod

class VideoOutlet(ABC):
    @abstractmethod
    def share_video_url(self, video_url: str):
        """Shares the video url on this outlet."""