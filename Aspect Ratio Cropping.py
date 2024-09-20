import math

def convert_to_16_9(x, y):
    # Calcula el nuevo valor de x para la relación de aspecto 16:9
    new_x = math.ceil((16 / 9) * y)
    return new_x, y

# Ejemplo de uso:
x, y = 1440, 1080  # Resolución arbitraria con relación de aspecto 4:3
new_resolution = convert_to_16_9(x, y)
print(f"Resolución original: ({x}, {y})")
print(f"Nueva resolución con relación 16:9: {new_resolution}")
