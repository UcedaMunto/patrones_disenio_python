import abc
from abc import ABC, abstractmethod
# https://refactoring.guru/es/design-patterns/bridge

class IFormat(ABC):
    @abstractmethod
    def play(self, file_path: str) -> None:
        pass

class MusicPlayer( ABC ):
    def __init__(self, format:IFormat):
        self.format = format 

    @abstractmethod
    def play(self, file_path: str) -> None:
        pass

class DesktopPlayer(MusicPlayer):
    def play(self, file_path:str) -> None:
        print("Using Mobile player")
        self.format.play( file_path )

class MobilPlayer(MusicPlayer):
    def play(self, file_path:str) -> None:
        print("Using Mobile player")
        self.format.play( file_path )

class MP3(IFormat):
    def play(self, file_path: str) -> None:
        print(f"PLaying WAV FILE {file_path}")


class WAV(IFormat):
    def play(self, file_path: str) -> None:
        print(f"PLaying WAV FILE {file_path}")

    
mp3_format = MP3()
player = DesktopPlayer(mp3_format)
player.play("song mp3")

wav_format = WAV()
player2 = DesktopPlayer(wav_format)
player2.play("song wab")