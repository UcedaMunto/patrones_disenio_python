
from abc import ABC, abstractmethod

#------------------------------------------------------------------------
# -------- Productos - Objetos finales
#------------------------------------------------------------------------
class Vehiculo:
    def __init__(self):
        self.tipo = None
        self.partes = []

    def agregar_parte(self, parte):
        self.partes.append(parte)

    def mostrar_partes(self):
        return f"Vehículo: {self.tipo}, Partes: {', '.join(self.partes)}"


#------------------------------------------------------------------------
# -------- Contrato general - define los metodos comunes
#------------------------------------------------------------------------
class BuilderVehiculo:
    def __init__(self):
        self.vehiculo = Vehiculo()

    def reset(self):
        self.vehiculo = Vehiculo()

    def set_tipo(self):
        pass

    def agregar_ruedas(self):
        pass

    def agregar_motor(self):
        pass

    def agregar_puertas(self):
        pass

    def obtener_vehiculo(self):
        return self.vehiculo


#------------------------------------------------------------------------
# -------- Define la construccion especifica en base al contrato - 
# -------- retorna objetos finales
#------------------------------------------------------------------------
class BuilderCarro(BuilderVehiculo):
    def set_tipo(self):
        self.vehiculo.tipo = "Carro"

    def agregar_ruedas(self):
        self.vehiculo.agregar_parte("4 ruedas")

    def agregar_motor(self):
        self.vehiculo.agregar_parte("Motor de gasolina")

    def agregar_puertas(self):
        self.vehiculo.agregar_parte("4 puertas")


# Builder concreto: Motocicleta
class BuilderMotocicleta(BuilderVehiculo):
    def set_tipo(self):
        self.vehiculo.tipo = "Motocicleta"

    def agregar_ruedas(self):
        self.vehiculo.agregar_parte("2 ruedas")

    def agregar_motor(self):
        self.vehiculo.agregar_parte("Motor pequeño")

    def agregar_puertas(self):
        self.vehiculo.agregar_parte("Sin puertas")


# Director
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construir_vehiculo_completo(self):
        self.builder.reset()
        self.builder.set_tipo()
        self.builder.agregar_ruedas()
        self.builder.agregar_motor()
        self.builder.agregar_puertas()
        return self.builder.obtener_vehiculo()


# Uso del patrón Builder
if __name__ == "__main__":
    # Crear un builder para un carro
    builder_carro = BuilderCarro()
    director = Director(builder_carro)

    carro = director.construir_vehiculo_completo()
    print(carro.mostrar_partes())

    # Crear un builder para una motocicleta
    builder_moto = BuilderMotocicleta()
    director = Director(builder_moto)

    motocicleta = director.construir_vehiculo_completo()
    print(motocicleta.mostrar_partes())