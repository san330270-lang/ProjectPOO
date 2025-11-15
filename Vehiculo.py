"""
Sistema de Gestión de Vehículos con POO
Implementa: Herencia, Composición, Encapsulamiento y Métodos de Comportamiento
Basado en diagrama UML proporcionado
"""
from operator import truediv


class vehiculo:
    """Clase Motor - Utilizada mediante composición en vehículos"""

    def __init__(self, marca, modelo, anio):
        self._marca = marca
        self._modelo = modelo
        self._anio = anio
        self._encender = False
        self._apagar = True
        self._maletero = False
        self._claxon = True


    """Metodos property y setter"""

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self,new_marca):
        self._marca = new_marca

    # Property para 'modelo'
    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, new_modelo):
        self._modelo = new_modelo

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self,n_anio):
        self._anio =  n_anio

    """Metodos de comportamiento"""

    def encendido(self):
        self.encender = True
        print(f"El vehiculo marca {self._marca} encendido")
    def apagado(self):
        self.apagado = False
        print(f"El vehiculo marca {self._marca} apagado")
    def __str__(self):
        return f"Vehiculo: {self.__dict__.__str__()}"
ferrari = vehiculo("Ford", "WWM", "2023")
ferrari.encendido()
ferrari.apagado()




