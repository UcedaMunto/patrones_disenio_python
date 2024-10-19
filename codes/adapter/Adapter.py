from abc import ABC, abstractmethod

# Interfaz esperada para reproducir archivos de audio
class ReproductorAudio(ABC):
    @abstractmethod
    def reproducir(self, archivo):
        pass

# Servicio para reproducir archivos MP3
class ServicioMP3:
    def reproducir_mp3(self, archivo_mp3):
        print(f"Reproduciendo archivo MP3: {archivo_mp3}")

# Servicio para reproducir archivos WAV
class ServicioWAV:
    def reproducir_wav(self, archivo_wav):
        print(f"Reproduciendo archivo WAV: {archivo_wav}")

# Adaptador para el servicio MP3
class AdaptadorMP3(ReproductorAudio):
    def __init__(self, servicio_mp3):
        self.servicio_mp3 = servicio_mp3

    def reproducir(self, archivo):
        # Llamamos al método específico del servicio MP3
        self.servicio_mp3.reproducir_mp3(archivo)

# Adaptador para el servicio WAV
class AdaptadorWAV(ReproductorAudio):
    def __init__(self, servicio_wav):
        self.servicio_wav = servicio_wav

    def reproducir(self, archivo):
        # Llamamos al método específico del servicio WAV
        self.servicio_wav.reproducir_wav(archivo)

# Cliente que usa el adaptador para reproducir archivos de audio sin preocuparse del formato
class Reproductor:
    def __init__(self, reproductor_audio):
        self.reproductor_audio = reproductor_audio

    def reproducir_archivo(self, archivo):
        self.reproductor_audio.reproducir(archivo)

# Uso del sistema con ambos adaptadores
if __name__ == "__main__":
    # Servicio de MP3
    servicio_mp3 = ServicioMP3()
    adaptador_mp3 = AdaptadorMP3(servicio_mp3)

    # Servicio de WAV
    servicio_wav = ServicioWAV()
    adaptador_wav = AdaptadorWAV(servicio_wav)

    # Reproductor usando adaptador de MP3
    reproductor_mp3 = Reproductor(adaptador_mp3)
    reproductor_mp3.reproducir_archivo("cancion.mp3")

    # Reproductor usando adaptador de WAV
    reproductor_wav = Reproductor(adaptador_wav)
    reproductor_wav.reproducir_archivo("audio.wav")
