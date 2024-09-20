def calculate_pressure_total(M1, M2, m1, m2, V, T):
    # Convertir la temperatura de Celsius a Kelvin
    T_kelvin = T + 273.15

    # Constante de los gases
    R = 0.082

    # Calcular la presión total usando la fórmula proporcionada
    P_total = ((m1 / M1) + (m2 / M2)) * R * T_kelvin / V

    return P_total


# Solicitar al usuario que ingrese los valores necesarios
try:
    M1 = float(input("Ingresa la masa molar del primer gas (g/mol): "))
    M2 = float(input("Ingresa la masa molar del segundo gas (g/mol): "))
    m1 = float(input("Ingresa la masa del primer gas (g): "))
    m2 = float(input("Ingresa la masa del segundo gas (g): "))
    V = float(input("Ingresa el volumen del recipiente (dm³): "))
    T = float(input("Ingresa la temperatura (°C): "))

    pressure_total = calculate_pressure_total(M1, M2, m1, m2, V, T)
    print(f"La presión total ejercida por las moléculas es: {pressure_total:.2f} atm")
except ValueError:
    print("Por favor, ingresa valores numéricos válidos.")
