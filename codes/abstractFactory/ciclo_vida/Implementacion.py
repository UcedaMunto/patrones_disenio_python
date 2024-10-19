from abc import ABC, abstractmethod
from debug import live

class IVehicle(ABC, live):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    @abstractmethod
    def drive(self):
        pass 

class Motorcycle(IVehicle, live):
    def drive(self):
        print("__________Conduciendo la motocicleta...")
    def start(self):
        print("__________Motocicleta encendida.")
    def stop(self):
        print("__________Motocicleta apagada.")

class Car(IVehicle, live):
    def drive(self):
        print("__________Conduciendo el coche...")
    def start(self):
        print("__________Coche encendido.")
    def stop(self):
        print("__________Coche apagado.")

class Bike(IVehicle, live):
    def drive(self):
        print("__________Conduciendo la bicicleta...")
    def start(self):
        print("__________Bicicleta encendida.")
    def stop(self):
        print("__________Bicicleta apagada.")
