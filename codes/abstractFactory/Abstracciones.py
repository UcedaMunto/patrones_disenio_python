from abc import ABC, abstractmethod  # Importa la clase base abstracta y el decorador para métodos abstractos

# ------------------------------------------------------------------------------------------------
# --------------    Objectos abstractos
# ------------------------------------------------------------------------------------------------
class IButton(ABC):  # IButton hereda de ABC para ser una clase abstracta
    @abstractmethod  # Define un método abstracto que debe ser implementado por las subclases
    def render(self):
        pass  # Método abstracto que no tiene implementación en esta clase
class IDropDown(ABC):  # IDropDown es una clase abstracta
    @abstractmethod  # Método abstracto que debe ser implementado en subclases
    def render(self):
        pass  # Método sin implementación
class ITextBox(ABC):  # ITextBox es una clase abstracta
    @abstractmethod  # Método abstracto que será implementado por subclases
    def render(self):
        pass  # Método sin implementación

# ------------------------------------------------------------------------------------------------
# --------------    Factory - Creadora abstracta
# ------------------------------------------------------------------------------------------------

class IThemeFactory(ABC):  # IThemeFactory es una clase abstracta
    @abstractmethod  # Método abstracto para crear un botón
    def create_button(self):
        pass  # Método sin implementación
    @abstractmethod  # Método abstracto para crear un dropdown
    def create_dropdown(self):
        pass  # Método sin implementación
    @abstractmethod  # Método abstracto para crear una caja de texto
    def create_text_box(self):
        pass  # Método sin implementación

# ------------------------------------------------------------------------------------------------
# --------------    Objetos concretos - definiciones de sus metodos
# ------------------------------------------------------------------------------------------------
# Implementación concreta de un botón para Linux
class LinuxButton(IButton):  # Hereda de IButton e implementa el método render
    def render(self):
        print("render linux button")  # Imprime un mensaje indicando la representación del botón de Linux

# Implementación concreta de un dropdown para Linux
class LinuxDropDown(IDropDown):  # Hereda de IDropDown e implementa el método render
    def render(self):
        print("render linux dropdown")  # Imprime un mensaje indicando la representación del dropdown de Linux

# Implementación concreta de una caja de texto para Linux
class LinuxTextBox(ITextBox):  # Hereda de ITextBox e implementa el método render
    def render(self):
        print("render linux textbox")  # Imprime un mensaje indicando la representación de la caja de texto de Linux

# Implementación concreta de un botón para Mac
class MacButton(IButton):  # Hereda de IButton e implementa el método render
    def render(self):
        print("render Mac button")  # Imprime un mensaje indicando la representación del botón de Mac

# Implementación concreta de un dropdown para Mac
class MacDropDown(IDropDown):  # Hereda de IDropDown e implementa el método render
    def render(self):
        print("render Mac dropdown")  # Imprime un mensaje indicando la representación del dropdown de Mac

# Implementación concreta de una caja de texto para Mac
class MacTextBox(ITextBox):  # Hereda de ITextBox e implementa el método render
    def render(self):
        print("render Mac textbox")  # Imprime un mensaje indicando la representación de la caja de texto de Mac

# ------------------------------------------------------------------------------------------------
# --------------    Factory concretas - definiciones de sus metodos
# ------------------------------------------------------------------------------------------------
# Implementación concreta de una fábrica de temas para Linux
class LinuxFactory(IThemeFactory):  # Hereda de IThemeFactory e implementa los métodos para crear componentes
    def create_button(self):
        return LinuxButton()  # Retorna una instancia de LinuxButton
    def create_dropdown(self):
        return LinuxDropDown()  # Retorna una instancia de LinuxDropDown
    def create_text_box(self):
        return LinuxTextBox()  # Retorna una instancia de LinuxTextBox
    
# Implementación concreta de una fábrica de temas para Mac
class MacFactory(IThemeFactory):  # Hereda de IThemeFactory e implementa los métodos para crear componentes
    def create_button(self):
        return MacButton()  # Retorna una instancia de MacButton
    def create_dropdown(self):
        return MacDropDown()  # Retorna una instancia de MacDropDown
    def create_text_box(self):
        return MacTextBox()  # Retorna una instancia de MacTextBox
    


# Crear una fábrica de temas para Linux
linux_factory = LinuxFactory()  # Instancia de LinuxFactory
mac_factory = MacFactory()  # Instancia de MacFactory
linux_button = linux_factory.create_button()  # Crea una instancia de LinuxButton
mac_drodown = mac_factory.create_dropdown()  # Crea una instancia de MacDropDown
mac_button = mac_factory.create_button()  # Crea una instancia de MacButton
linux_button.render()  # Llama al método render del botón de Linux
mac_drodown.render()  # Llama al método render del dropdown de Mac
mac_button.render()  # Llama al método render del botón de Mac
