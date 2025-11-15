from Vehiculo import vehiculo
class Motocicleta(vehiculo):
    def __init__ (self, marca: str , anio: str ,modelo: str, cilindraje: int):
            vehiculo.__init__(self, marca=marca, anio=anio,  modelo=modelo)
            self._cilindraje = cilindraje
            self._caballo = True
            self._arranque = False

    @property
    def cilindraje(self):
        return self.cilindraje

    @cilindraje.setter
    def cilindraje(self, new_cilindraje:int):
        self._cilindraje = new_cilindraje

    def h_caballito(self):
        self.caballo= True
        print(f"Se hizo caballito")

    def u_patada_arranque(self):
        self.arranque = False
        print(f"Se ha usado la patada de arranque para encender")
    def __str__(self):
        info_padre=super ().__str__()
        return f"{info_padre}\ncilindraje:{self._cilindraje}cc"

motocycle = Motocicleta(marca="kawasaki", modelo="ht4", anio= "2024", cilindraje="84")
print(motocycle)
motocycle.h_caballito()
motocycle.u_patada_arranque()