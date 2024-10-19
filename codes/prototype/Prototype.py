from abc import ABC, abstractmethod
import copy

class IClonable(ABC):
    @abstractmethod
    def clone(self):
        pass

class Shape(IClonable, ABC):
    def __init__(self) -> None:
        self.id = None
        self.name = None
    @abstractmethod
    def draw(self):
        pass

    def clone(self):
        cp = copy.copy(self)
        cp.id = cp.id * -1
        return cp
    
class Circle(Shape):
    def __init__(self) -> None:
        super().__init__()
        self.name = "CIRLCE"
    def draw(self):
        print(f"Drwa {self.id }")

class Rectangle(Shape):
    def __init__(self) -> None:
        super().__init__()
        self.name = "RECTANGLE"
    def draw(self):
        print(f"Drwa {self.id }")
    
class Rectangle(Shape):
    def __init__(self) -> None:
        super().__init__()
        self.name = "SQUEARE"
    def draw(self):
        print(f"Drwa {self.id }")

circle = Circle()
circle.id = 1
rectangle = Rectangle()
rectangle.id = 2
clone_circle = circle.clone()
clone_rectangle = rectangle.clone()

circle.draw()
rectangle.draw()
clone_circle.draw()
clone_rectangle.draw()

