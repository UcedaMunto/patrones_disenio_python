import abc
from abc import ABC, abstractmethod
# https://refactoring.guru/es/design-patterns/bridge

# ________________ INTERFAZ
class IFormat(ABC):
    @abstractmethod
    def play(self, file_path: str) -> None:
        pass
# ________________ CLASE ABSTRACTA
class MusicPlayer( ABC ):
    def __init__(self, format:IFormat): # IFormat se utiliza como un contrato que permite conectar las clases  
        self.format = format 
    @abstractmethod
    def play(self, file_path: str) -> None:
        pass
#__________________ORIGEN
class MP3(IFormat): 
    print(f"MP3 Implementa la interfaz IFormat")
    def play(self, file_path: str) -> None:
        print(f"PLaying WAV FILE {file_path}")
class WAV(IFormat):
    print(f"WAV Implementa la interfaz IFormat")
    def play(self, file_path: str) -> None:
        print(f"PLaying WAV FILE {file_path}")

#__________________DESTINO
class DesktopPlayer(MusicPlayer):
    def play(self, file_path:str) -> None:
        print("Using Mobile player")
        self.format.play( file_path )
class MobilPlayer(MusicPlayer):
    def play(self, file_path:str) -> None:
        print("Using Mobile player")
        self.format.play( file_path )


#__________________EJECUCION

mp3_format = MP3()
player = DesktopPlayer(mp3_format)
player.play("song mp3")

wav_format = WAV()
player2 = DesktopPlayer(wav_format)
player2.play("song wab")