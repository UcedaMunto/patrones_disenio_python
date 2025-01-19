from abc import ABC, abstractmethod

class IConffee(ABC):
    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_description(self):
        pass

class SimpleCoffee(IConffee):
    def get_cost(self):
        return 1.0
    
    def get_description(self):
        return "Café simple"
    
class CoffeDecorator(IConffee):
    def __init__(self, coffe):
        self._coffee = coffe
    def get_cost(self):
        return self._coffee.get_cost()
    def get__description(self):
        return self._coffee.get_description()
    
class MilkDecorator(CoffeDecorator):
    def __init__(self, coffe):
        super().__init__(coffe)
    def get_cost(self):
        return self._coffee.get_cost() + 0.5
    def get_description(self):
        return self._coffee.get_description() + "+ leche"
    
class WhippedCreamDecorator(CoffeDecorator):
    def __init__(self, coffe):
        super().__init__(coffe)
    def get_cost(self):
        return super().get_cost() + 0.7
    def get_description(self):
        return super().get_description() + ", con crema"
    
coffee = SimpleCoffee()
print( f"{ coffee.get_description() } : ${ coffee.get_cost()} ")

coffee = MilkDecorator( coffee )    
print( f"{ coffee.get_description() } : ${ coffee.get_cost()} ")

coffe = WhippedCreamDecorator(coffee)
print( f"{ coffee.get_description() } : ${ coffee.get_cost()} ")