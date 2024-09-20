def calculate_ages(humanYears):
    # Inicializamos las edades de gato y perro en 0
    cat_years = 0
    dog_years = 0

    # Cálculo de años de gato
    if humanYears >= 1:
        cat_years += 15
    if humanYears >= 2:
        cat_years += 9
    if humanYears > 2:
        cat_years += (humanYears - 2) * 4

    # Cálculo de años de perro
    if humanYears >= 1:
        dog_years += 15
    if humanYears >= 2:
        dog_years += 9
    if humanYears > 2:
        dog_years += (humanYears - 2) * 5

    # Devuelve una lista con los años humanos, años de gato y años de perro
    return [humanYears, cat_years, dog_years]



# Ejemplo de uso
humanYears = 5
result = calculate_ages(humanYears)
print(result)  # Output: [5, 28, 34]
print(type(result))