from abc import ABC, abstractmethod

# Cada método es abstracto y debe ser implementado por las clases concretas.
class IRobotBuilder(ABC):
    @abstractmethod
    def build_head(self, head): pass
    @abstractmethod
    def build_body(self, body): pass
    @abstractmethod
    def build_legs(self, legs): pass
    @abstractmethod
    def build_arms(self, arms): pass
    @abstractmethod
    def get_robot(self): pass

# Implementación concreta del builder que construye un robot.
class RobotBuilder(IRobotBuilder):
    def __init__(self):
        self.robot = Robot()
    def build_head(self, head):
        self.robot.head = head
    def build_body(self, body):
        self.robot.body = body
    def build_arms(self, arms):
        self.robot.arms = arms
    def build_legs(self, legs):
        self.robot.legs = legs
    def get_robot(self):
        return self.robot

# Director que orquesta el proceso de construcción del robot.
# Recibe un builder y define el proceso paso a paso.
class RobotDirector:
    def __init__(self, robot_builder) -> None:
        self.robot_builder = robot_builder
    def construct_robot(self):
        self.robot_builder.build_head("chasis")  # Construye la cabeza con valor "chasis".
        self.robot_builder.build_body("metal")   # Construye el cuerpo con valor "metal".
        self.robot_builder.build_legs("ruedas")  # Construye las piernas con valor "ruedas".
        self.robot_builder.build_arms("arma")    # Construye los brazos con valor "arma".


# Clase Robot: representa el producto final construido.
class Robot:
    # Método para mostrar la información del robot (sus partes).
    def display_robot_info(self):
        print("robot info")
        print(f"... {self.head}")   # Muestra la cabeza del robot.
        print(f"... {self.body}")   # Muestra el cuerpo del robot.
        print(f"... {self.arms}")   # Muestra los brazos del robot.
        print(f"... {self.legs}")   # Muestra las piernas del robot.

# Cliente: este código utiliza el director y el builder para construir el robot.

robot_builder = RobotBuilder()
robot_director = RobotDirector(robot_builder)

# El director construye el robot especificando los componentes.
robot_director.construct_robot()
robot = robot_builder.get_robot()
robot.display_robot_info()
