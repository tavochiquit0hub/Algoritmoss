import math


def calculate_litres(time_hours):
    # Nathan bebe 0.5 litros por hora de ciclismo
    litres = 0.5 * time_hours
    # Redondear hacia abajo al entero más cercano
    return math.floor(litres)


# Solicitar al usuario que ingrese el tiempo en horas
try:
    time_hours = float(input("Ingresa el tiempo de ciclismo en horas: "))

    litres_drunk = calculate_litres(time_hours)
    print(f"Nathan beberá {litres_drunk} litros de agua.")
except ValueError:
    print("Por favor, ingresa un número válido.")
