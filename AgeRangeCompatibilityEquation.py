import math
def age_range(age):
    if age <= 14:
        min_age = math.floor(age - 0.10 * age)
        max_age = math.floor(age + 0.10 * age)
    else:
        min_age = math.floor(age / 2 + 7)
        max_age = math.floor((age - 7) * 2)

    return f"{min_age}-{max_age}"
#math.floor sirve para redondear un nuemro hacia abajo

# Solicitar al usuario que ingrese su edad
try:
    age = int(input("Ingresa tu edad: "))

    if 1 <= age <= 100:
        result = age_range(age)
        print(f"El rango de edad recomendado es: {result}")
    else:
        print("Por favor, ingresa una edad entre 1 y 100.")
except ValueError:
    print("Por favor, ingresa un número entero válido.")
