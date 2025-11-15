class Motor:
    def __init__(self, tipo: str, potencia: int):
        self._tipo = tipo
        self._potencia = potencia
        self._motor_encendido = False

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, new_tipo):
        self._tipo = new_tipo

    @property
    def potencia(self):
        return self._potencia

    @potencia.setter
    def potencia(self, new_potencia):
        self._potencia = new_potencia

    def encender_motor(self):
        self._motor_encendido = True
        print(f"Motor encendido")

    def apagar_motor(self):
        self._motor_encendido = False
        print(f"Motor apagado")

    def __str__(self):
        return f"Motor: {self.__dict__.__str__()}"


motorc = Motor("combustion", 830)
print(motorc)
motorc.encender_motor()
motorc.apagar_motor()