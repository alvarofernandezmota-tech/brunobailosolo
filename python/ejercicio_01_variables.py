# ============================================================
# 🐍 EJERCICIO 01 — VARIABLES Y TIPOS DE DATOS
# ============================================================
# Una variable es una caja con nombre que guarda información.
# Python tiene distintos tipos según lo que guardes.
#
# TIPOS BÁSICOS:
#   str   → texto, siempre entre comillas
#   int   → número entero
#   float → número con decimales
#   bool  → solo True o False
# ============================================================

# ── PARTE RESUELTA ──────────────────────────────────────────
# Así se crean variables en Python:

nombre   = "Begoña"        # str   → texto
edad     = 25              # int   → número entero
altura   = 1.65            # float → número decimal
es_mayor = True            # bool  → verdadero o falso

# Mostrar variables con print()
print("Nombre:", nombre)
print("Edad:", edad)
print("Altura:", altura)
print("¿Es mayor de edad?", es_mayor)

# f-string: forma elegante de mezclar texto y variables
print(f"Hola, {nombre}. Tienes {edad} años y mides {altura}m.")

# type() nos dice qué tipo es una variable
print(type(nombre))   # <class 'str'>
print(type(edad))     # <class 'int'>
print(type(altura))   # <class 'float'>


# ── TU TURNO ────────────────────────────────────────────────
# 1. Crea una variable con TU nombre
# 2. Crea una variable con TU edad
# 3. Imprime: "Me llamo X y tengo Y años."

mi_nombre = ___         # ← escribe tu nombre entre comillas
mi_edad   = ___         # ← escribe tu edad (sin comillas)

print(f"Me llamo {mi_nombre} y tengo {mi_edad} años.")
