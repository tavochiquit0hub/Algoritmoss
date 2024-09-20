def nba_extrap(ppg, mpg):
    # Si mpg es 0, devolvemos 0
    if mpg == 0:
        return 0

    # Calcular los puntos extrapolados para 48 minutos
    ppg_48 = (ppg / mpg) * 48

    # Redondear a la décima más cercana
    return round(ppg_48, 1)


# Solicitar al usuario que ingrese los datos
try:
    ppg = float(input("Ingresa el promedio de puntos por juego (ppg): "))
    mpg = float(input("Ingresa el promedio de minutos jugados por juego (mpg): "))

    extrapolated_ppg = nba_extrap(ppg, mpg)
    print(f"El promedio de puntos por juego extrapolado para 48 minutos es: {extrapolated_ppg}")
except ValueError:
    print("Por favor, ingresa números válidos.")
