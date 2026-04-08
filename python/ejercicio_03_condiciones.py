# ============================================================
# 🐍 EJERCICIO 03 — CONDICIONES (if / elif / else)
# ============================================================
# Python puede tomar decisiones según si algo es verdad o no.
#
# Estructura:
#   if condicion:       → si se cumple esto...
#       hacer_algo()
#   elif otra:          → si no, pero se cumple esto otro...
#       hacer_otra()
#   else:               → si ninguna anterior se cumple...
#       hacer_default()
#
# Operadores de comparación:
#   ==  igual           !=  distinto
#   >   mayor que       <   menor que
#   >=  mayor o igual   <=  menor o igual
# ============================================================

# ── PARTE RESUELTA ──────────────────────────────────────────

temperatura = 22   # grados

if temperatura >= 30:
    print("Hace mucho calor. 🌞")
elif temperatura >= 20:
    print("Temperatura agradable. 🌤️")
elif temperatura >= 10:
    print("Fresquito, coge una chaqueta. 🧥")
else:
    print("Hace frío. Quédate en casa. ❄️")

# Combinar condiciones con and / or
llueve = False

if temperatura >= 20 and not llueve:
    print("Perfecto para salir.")
else:
    print("Mejor planea algo en casa.")


# ── TU TURNO ────────────────────────────────────────────────
# Escribe un programa que evalúe una nota (0-10) e imprima:
#   10          → "Matrícula de honor 🏆"
#   entre 7-9   → "Notable 🌟"
#   entre 5-6   → "Aprobado ✅"
#   menos de 5  → "Suspenso ❌"

nota = int(input("Introduce una nota del 0 al 10: "))

if nota == ___:
    print("Matrícula de honor 🏆")
elif nota >= ___:
    print("Notable 🌟")
elif nota >= ___:
    print("Aprobado ✅")
else:
    print("Suspenso ❌")
