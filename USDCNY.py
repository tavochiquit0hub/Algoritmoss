def convert_currency(usd):
    # Tasas de conversión aproximadas
    usd_to_cny = 7.15
    usd_to_mxn = 17.50
    usd_to_jpy = 146.00

    # Conversión
    cny = usd * usd_to_cny
    mxn = usd * usd_to_mxn
    jpy = usd * usd_to_jpy

    # Formateo del resultado
    result = (
        f"{usd} USD es equivalente a:\n"
        f"{cny:.2f} Chinese Yuan\n"
        f"{mxn:.2f} Pesos Mexicanos\n"
        f"{jpy:.2f} Yenes Japoneses"
    )

    return result


# Solicitar al usuario que ingrese la cantidad en USD
try:
    usd_amount = float(input("Ingresa la cantidad en USD que deseas convertir: "))
    conversion_result = convert_currency(usd_amount)
    print(conversion_result)
except ValueError:
    print("Por favor, ingresa un número válido.")
