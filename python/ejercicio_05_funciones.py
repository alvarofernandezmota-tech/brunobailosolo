# ============================================================
# 🐍 EJERCICIO 05 — FUNCIONES (def)
# ============================================================
# Una función es un bloque de código con nombre que:
#   - Se define una vez con def
#   - Se puede llamar cuantas veces quieras
#   - Puede recibir datos de entrada (parámetros)
#   - Puede devolver un resultado (return)
#
# Estructura:
#   def nombre_funcion(parametro1, parametro2):
#       # código
#       return resultado
# ============================================================

# ── PARTE RESUELTA ──────────────────────────────────────────

# Función sin parámetros
def saludar():
    print("¡Hola! Soy una función.")

saludar()   # llamar la función

# Función con parámetros
def saludar_a(nombre):
    print(f"¡Hola, {nombre}!")

saludar_a("Begoña")
saludar_a("Álvaro")

# Función con return
def cuadrado(numero):
    resultado = numero ** 2
    return resultado

print(cuadrado(4))    # → 16
print(cuadrado(7))    # → 49

# Función con valor por defecto en el parámetro
def presentar(nombre, ciudad="Madrid"):
    print(f"{nombre} vive en {ciudad}.")

presentar("Ana")               # usa Madrid por defecto
presentar("Luis", "Barcelona") # sobreescribe el defecto


# ── TU TURNO ────────────────────────────────────────────────
# 1. Crea una función "suma" que reciba dos números y devuelva su suma
# 2. Crea una función "es_par" que reciba un número y devuelva True/False
# 3. Llama a ambas funciones con distintos valores

def suma(a, b):
    return ___   # ← completa

def es_par(numero):
    return ___ == 0   # ← pista: usa el operador % (módulo / resto)

print(suma(3, 7))         # → 10
print(suma(10, 5))        # → 15
print(es_par(4))          # → True
print(es_par(7))          # → False
