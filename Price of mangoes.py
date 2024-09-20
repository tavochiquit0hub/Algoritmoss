def mango_cost(quantity, price_per_mango):
    # Calculamos cuántos mangos se pagan y cuántos se obtienen gratis
    # La oferta es "3 por 2", por lo que por cada 3 mangos, pagamos solo 2
    paid_mango_count = (quantity // 3) * 2 + (quantity % 3)
    total_cost = paid_mango_count * price_per_mango
    return total_cost


# Solicitar al usuario que ingrese la cantidad de mangos y el costo por mango
try:
    quantity = int(input("Ingresa la cantidad de mangos: "))
    price_per_mango = float(input("Ingresa el costo por mango: "))

    total_cost = mango_cost(quantity, price_per_mango)
    print(f"El costo total de los mangos es: ${total_cost:.2f}")
except ValueError:
    print("Por favor, ingresa números válidos.")
