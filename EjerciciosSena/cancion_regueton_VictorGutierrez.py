import random

# Listas por columnas de las palabras.
col1 = ["Mami", "Gata", "Perra", "Zorra", "Chica"]
col2 = ["Yo quiero", "Vamos a", "Yo voy a", "Yo quiero", "Yo vengo a"]
col3 = ["Castigarte", "Cogerte", "Encenderte", "Darte", "Azotarte"]
col4 = ["Duro", "Rápido", "Lento", "Suave", "Fuerte"]
col5 = ["Hasta que salga el sol", "Toda la noche", "Hasta el amanecer", "Hasta mañana", "Todo el día"]
col6 = ["Sin miedo", "Sin anestesia", "Contra el piso", "Contra la pared", "Sin compromiso"]

# Función para construir una estrofa al azar
def generar_frase():
    return f"{random.choice(col1)} {random.choice(col2)} {random.choice(col3)} {random.choice(col4)} {random.choice(col5)} {random.choice(col6)}."

# Función para construir un coro siguiendo las reglas
def generar_coro():
    palabra = random.choice(col3)
    return f"{palabra}, {palabra}, {palabra}, {random.choice(col5)}, {random.choice(col4)}."

# Generar la canción
print("\nComo Componer una Canción de Reggaetón\n")
for _ in range(4):  # Generar 4 frases aleatorias
    print(generar_frase())

print("\nCoro ")
print(generar_coro())

