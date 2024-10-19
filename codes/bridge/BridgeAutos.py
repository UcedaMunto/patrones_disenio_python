
from abc import ABC, abstractmethod

class IEngine(ABC):
    print("Interfaz Engine")
    @abstractmethod
    def stop(self):
        pass
    @abstractmethod
    def start(self):
        pass

class Vehicle(ABC):
    print("Abstraccion Vehiculo")
    def __init__(self, engine: IEngine) -> None:
        self._engine = engine
    @abstractmethod
    def drive( self ):
        pass

class Bus( Vehicle ):
    print("definiendo bus <- Vehiculo ")
    def drive(self):
        print("Manejando el bus")
        self._engine.start()

class Car( Vehicle ):
    print("definiendo carro <- Vehiculo ")
    def drive(self):
        print("Manejando el carro")
        self._engine.start()

class ElectricEngine(IEngine):
    print("definiendo motor electrico <- Iengine (implementando)")
    def start(self):
        print(F"start {self.__class__.__name__}")
    def stop(self):
        print(F"stop {self.__class__.__name__}")

class PetrolEngine(IEngine):
    print("definiendo motor de gasolina <- Iengine (implementando)")
    def start(self):
        print(F"start {self.__class__.__name__}")

    def stop(self):
        print(F"stop {self.__class__.__name__}")

print("_____________ INICIANDO EJECUCION _____________ ")

car_whith_petrol_engine = Car( PetrolEngine() )
car_whith_petrol_engine.drive()

bus_whith_electric_engine = Bus( ElectricEngine() )
bus_whith_electric_engine.drive()