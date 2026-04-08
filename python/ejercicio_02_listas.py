# ============================================================
# 🐍 EJERCICIO 02 — LISTAS
# ============================================================
# Una lista guarda VARIOS valores en una sola variable.
# Se escribe con corchetes [ ] y los elementos van separados
# por comas.
#
# Las listas:
#   - Mantienen el orden
#   - Pueden tener duplicados
#   - Empiezan a contar desde el índice 0
# ============================================================

# ── PARTE RESUELTA ──────────────────────────────────────────

frutas = ["manzana", "naranja", "plátano", "uva"]

print(frutas)           # lista completa
print(frutas[0])        # primer elemento  → manzana
print(frutas[-1])       # último elemento  → uva
print(len(frutas))      # cuántos hay      → 4

# Añadir un elemento al final
frutas.append("kiwi")
print(frutas)

# Eliminar un elemento
frutas.remove("naranja")
print(frutas)

# Ordenar
frutas.sort()
print(frutas)

# Recorrer la lista
for fruta in frutas:
    print("→", fruta)


# ── TU TURNO ────────────────────────────────────────────────
# 1. Crea una lista con 3 ciudades que te gustaría visitar
# 2. Añade una cuarta ciudad con append()
# 3. Imprime cuántas ciudades hay en total
# 4. Imprime la primera y la última

ciudades = [___, ___, ___]   # ← escribe 3 ciudades entre comillas

ciudades.append(___)         # ← añade una cuarta

print("Total de ciudades:", len(ciudades))
print("Primera:", ciudades[0])
print("Última:", ciudades[-1])
