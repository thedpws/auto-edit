from abc import ABC, abstractmethod


class VideoEditor(ABC):

    @abstractmethod
    def add_logo(self, logo_filepath: str):
        """Adds the specified logo to the top left."""

    @abstractmethod
    def add_lower_thirds(self, name: str, bureau: str):
        """Adds lower thirds on beginning and end of the feature."""

    @abstractmethod
    def write_file(self, name: str):
        """Writes the video to the specified filename."""
