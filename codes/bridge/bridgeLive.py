import abc
from abc import ABC, abstractmethod
# https://refactoring.guru/es/design-patterns/bridge

class IFormat(ABC):
    print(f"Se define IFormat")
    @abstractmethod
    def play(self, file_path: str) -> None:
        pass

class MusicPlayer( ABC ):
    print(f"Se define MusicPlayer")
    def __init__(self, format:IFormat):
        self.format = format 

    @abstractmethod
    def play(self, file_path: str) -> None:
        pass

class DesktopPlayer(MusicPlayer):
    print(f"DesktopPlayer <- Musicplay (play)")
    def play(self, file_path:str) -> None:
        print("Using DesktopPlayer")
        self.format.play( file_path )

class MobilPlayer(MusicPlayer):
    print(f"MobilePlayer <- Musicplay (play)")
    def play(self, file_path:str) -> None:
        print("Using Mobileplayer")
        self.format.play( file_path )

class MP3(IFormat):
    print(F"MP3 <- IMPLEMENTA IFormat")
    def play(self, file_path: str) -> None:
        print(f"Playing MP3 FILE {file_path}")

class WAV(IFormat):
    print(F"MP3 <- IMPLEMENTA IFormat")
    def play(self, file_path: str) -> None:
        print(f"Playing WAV FILE {file_path}")

print("____________ inicia la ejecucion ____________")
mp3_format = MP3()
player = DesktopPlayer(mp3_format)
player.play("song mp3")

wav_format = WAV()
player2 = DesktopPlayer(wav_format)
player2.play("song wab")