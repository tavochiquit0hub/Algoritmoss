def find_third_angle(angle1, angle2):
    # La suma de los ángulos interiores de un triángulo es 180 grados
    third_angle = 180 - (angle1 + angle2)
    return third_angle


# Solicitar al usuario que ingrese los dos ángulos
try:
    angle1 = int(input("Ingresa el valor del primer ángulo: "))
    angle2 = int(input("Ingresa el valor del segundo ángulo: "))

    third_angle = find_third_angle(angle1, angle2)
    print(f"El tercer ángulo es: {third_angle} grados")
except ValueError:
    print("Por favor, ingresa un valor numérico válido.")
