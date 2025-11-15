from automovil import Automovil
from motocicleta import Motocicleta
from motor import Motor

if __name__ == "__main__":
    # Instanciar motores para vehículos
    motor_coche1 = Motor("Gasolina", 120)
    motor_coche2 = Motor("Diesel", 150)
    motor_bike1 = Motor("Gasolina", 80)
    motor_bike2 = Motor("Eléctrico", 60)

    # Instanciar automóviles
    coche1 = Automovil("Ram", "Corolla", 2022, 5)
    coche2 = Automovil("Ford", "Focus", 2021, 5)

    # Instanciar motocicletas
    bike1 = Motocicleta("Yamaha", "M7", 2024, 300)
    bike2 = Motocicleta("Kawasaki", "R/P", 2022, 100)

    # Probar funcionalidades de automóviles
    coche1.encendido()
    coche1.apagado()
    coche1.toc_clax()
    coche1.open_maletero()

    # Probar funcionalidades de motocicletas
    bike1.h_caballito()
    bike2.u_patada_arranque()

    # Probar funcionalidad del motor
    motor_coche1.encender_motor()

    # Visualizar información de todos los vehículos
    print("\n--- Información de Vehículos ---")
    print(coche1)
    print(coche2)
    print(bike1)
    print(bike2)

