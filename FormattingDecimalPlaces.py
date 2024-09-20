def round_to_two_decimal_places(number):
    # Redondear el número a dos decimales
    return round(number, 2)


# Solicitar al usuario que ingrese un número
try:
    number = float(input("Ingresa un número: "))

    rounded_number = round_to_two_decimal_places(number)
    print(f"El número redondeado a dos decimales es: {rounded_number:.2f}")
except ValueError:
    print("Por favor, ingresa un número válido.")
    print("Que onda prueba practica 1.4")
