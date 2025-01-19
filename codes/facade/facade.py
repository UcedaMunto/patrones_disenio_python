

class DvdPlayer:
    def on(self):
        print("DVD Player on")
    def play_movie(self, movie):
        print(f"paying '{movie}'")
    def off(self):
        print("Dvd apagado")

class Projector:
    def on(self):
        print("projector on")
    def off(self):
        print("projector off")

class Speaker:
    def on(self):
        print("Speaker on")
    def off(self):
        print("Speaker off")

class TeatroCasa:
    def __init__(self, dvd, projector, spaker):
        self.Speaker = spaker
        self.DvdPlayer = dvd 
        self.Projector = projector
    def whatch(self, movie):
        self.Speaker.on()
        self.DvdPlayer.on()
        self.Projector.on()
        print("Treatro reproduciendo...")
        self.DvdPlayer.play_movie(movie)

    def end_movie(self):
        print("____________________________")
        print("apagando...")
        self.DvdPlayer.off()
        self.Projector.off()
        self.Speaker.off()

dvdplayer = DvdPlayer()
projector = Projector()
speaker = Speaker()

teatro = TeatroCasa( dvdplayer, projector, speaker)
teatro.whatch("PELUCILA")
teatro.end_movie()