# ============================================================
# 🐍 EJERCICIO 04 — BUCLES (for / while)
# ============================================================
# Un bucle repite código automáticamente.
#
# Dos tipos:
#   for   → cuando sabes cuántas veces repetir
#   while → cuando repites HASTA que algo cambie
#
# Palabras clave dentro de bucles:
#   break    → sale del bucle inmediatamente
#   continue → salta a la siguiente vuelta
# ============================================================

# ── PARTE RESUELTA: bucle FOR ────────────────────────────────

# Repetir N veces con range()
for i in range(5):             # 0, 1, 2, 3, 4
    print(f"Vuelta {i}")

# Recorrer una lista
colores = ["rojo", "verde", "azul"]
for color in colores:
    print(f"El color es: {color}")

# range con inicio, fin y paso
for i in range(0, 11, 2):     # 0, 2, 4, 6, 8, 10
    print(i, end=" ")
print()   # salto de línea


# ── PARTE RESUELTA: bucle WHILE ──────────────────────────────

contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1   # contador = contador + 1

# Bucle infinito controlado con break
numero = 0
while True:
    numero += 1
    if numero == 3:
        break
print(f"Paré en: {numero}")


# ── TU TURNO ────────────────────────────────────────────────
# 1. Usa un bucle FOR para imprimir los números del 1 al 10
# 2. Usa un bucle FOR para imprimir solo los PARES del 2 al 20
# 3. Usa un bucle WHILE que acumule suma hasta llegar a 50

# Ejercicio 1
for i in range(___, ___):
    print(i)

# Ejercicio 2
for i in range(___, ___, ___):   # ← inicio, fin, paso
    print(i)

# Ejercicio 3
total = 0
while total < ___:
    total += 1
print("Total final:", total)
