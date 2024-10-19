from abc import ABC, abstractmethod

# Interfaz abstracta que define los pasos para construir un robot.
# Cada método es abstracto y debe ser implementado por las clases concretas.
class IRobotBuilder(ABC):

    # Método abstracto para construir la cabeza del robot.
    @abstractmethod
    def build_head(self, head): pass

    # Método abstracto para construir el cuerpo del robot.
    @abstractmethod
    def build_body(self, body): pass

    # Método abstracto para construir las piernas del robot.
    @abstractmethod
    def build_legs(self, legs): pass

    # Método abstracto para construir los brazos del robot.
    @abstractmethod
    def build_arms(self, arms): pass

    # Método abstracto para obtener el robot construido.
    @abstractmethod
    def get_robot(self): pass


# Implementación concreta del builder que construye un robot.
class RobotBuilder(IRobotBuilder):
    
    # Constructor: inicializa un nuevo objeto Robot vacío.
    def __init__(self):
        self.robot = Robot()

    # Implementa la construcción de la cabeza.
    def build_head(self, head):
        self.robot.head = head

    # Implementa la construcción del cuerpo.
    def build_body(self, body):
        self.robot.body = body

    # Implementa la construcción de los brazos.
    def build_arms(self, arms):
        self.robot.arms = arms

    # Implementa la construcción de las piernas.
    def build_legs(self, legs):
        self.robot.legs = legs

    # Devuelve el robot completo una vez construido.
    def get_robot(self):
        return self.robot


# Director que orquesta el proceso de construcción del robot.
# Recibe un builder y define el proceso paso a paso.
class RobotDirector:
    
    # Inicializa el director con un builder de robots.
    def __init__(self, robot_builder) -> None:
        self.robot_builder = robot_builder

    # Controla el proceso de construcción del robot, especificando las partes.
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

# Crea una instancia del builder concreto de robots.
robot_builder = RobotBuilder()

# Crea una instancia del director que usará el builder.
robot_director = RobotDirector(robot_builder)

# El director construye el robot especificando los componentes.
robot_director.construct_robot()

# El cliente obtiene el robot construido a través del builder.
robot = robot_builder.get_robot()

# El cliente muestra la información del robot construido.
robot.display_robot_info()
