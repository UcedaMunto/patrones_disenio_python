from abc import ABC, abstractmethod
from Implementacion import Motorcycle, Car, Bike
from debug import live

class FactoryVehicle(ABC, live):
    @abstractmethod
    def create_vehicle(self):
        pass
    def order_vehicle(self):
        vehicle = self.create_vehicle()
        print(f"Vehículo {vehicle.__class__.__name__} creado.")
        vehicle.start()
        vehicle.drive()
        vehicle.stop()
        return vehicle
    

class FactoryBike(FactoryVehicle, live):
    def create_vehicle(self):
        return Bike()

class FactoryCar(FactoryVehicle, live):
    def create_vehicle(self):
        return Car()

class FactoryMotorcycle(FactoryVehicle, live):
    def create_vehicle(self):
        return Motorcycle()
    
    

# Usando la fábrica de bicicletas como ejemplo
vehicle_factory = FactoryBike()
vehicle = vehicle_factory.order_vehicle()
print(f"=================== Usas un {vehicle.__class__.__name__}")

vehicle_factory2 = FactoryCar()
vehicle = vehicle_factory2.order_vehicle()
print(f"=================== Usas un {vehicle.__class__.__name__}")

