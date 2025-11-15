from Vehiculo import vehiculo

class Automovil(vehiculo):
    def __init__ (self, marca: str , anio: int ,modelo: str, num_puertas: int):
            vehiculo.__init__(self, marca=marca, modelo=modelo, anio=anio)
            self._num_puertas = num_puertas
            self._maletero = True
            self._claxon = False

    @property
    def num_puertas(self):
        return self._num_puertas

    @num_puertas.setter
    def num_puertas(self, num_puertas):
        self._num_puertas = num_puertas

    def open_maletero(self):
        self.maletero = True
        print(f"El maletero abrio")
    def toc_clax(self):
        self.claxon = False
        print(f"El claxon se toco")
    def __str__(self):
        return f"Automovil: {self.__dict__.__str__()}"

automovil = Automovil(marca="carro", modelo="efc", anio= "2021", num_puertas="4")
print(automovil)
automovil.open_maletero()
automovil.toc_clax()