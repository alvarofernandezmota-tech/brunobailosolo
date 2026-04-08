import random
import time

# ============================================
# 🍽️  EL RESTAURANTE DE PYTHON
# Aprende programando — para Begoña
# Cada plato = un concepto de Python
# ============================================

def mostrar_menu():
    print("""
╔══════════════════════════════════════════╗
║        🍽️  RESTAURANTE DE PYTHON         ║
║     Cada plato = un concepto nuevo   ║
╠══════════════════════════════════════════╣
║  1. 🥗  Plato 1 — VARIABLES              ║
║         Juego: ¿Qué tipo soy yo?        ║
║                                          ║
║  2. 🍲  Plato 2 — LISTAS                 ║
║         Juego: Mi lista de deseos        ║
║                                          ║
║  3. 🍕  Plato 3 — BUCLES                 ║
║         Juego: La cuenta atrás           ║
║                                          ║
║  4. 🥩  Plato 4 — CONDICIONES            ║
║         Juego: ¿Entras al club?          ║
║                                          ║
║  5. 🍰  Plato 5 — FUNCIONES              ║
║         Juego: La máquina de saludos    ║
║                                          ║
║  6. 🎂  Plato 6 — PROYECTO FINAL         ║
║         Juego: Adivina el número        ║
║                                          ║
║  0. 🚪  Salir del restaurante            ║
╚══════════════════════════════════════════╝
    """)


# ─── PLATO 1: VARIABLES ─────────────────────────────────
def plato1_variables():
    print("\n🥗 PLATO 1 — VARIABLES")
    print("─" * 42)
    print("Una variable es una caja donde guardas información.")
    print("Tiene un nombre y un contenido.\n")

    nombre = input("¿Cuál es tu nombre? ")
    edad   = int(input("¿Cuántos años tienes? "))
    ciudad = input("¿En qué ciudad vives? ")

    print("\n✅ Python acaba de crear 3 variables:")
    print(f"   nombre = '{nombre}'  → tipo texto  (str)")
    print(f"   edad   = {edad}          → tipo número (int)")
    print(f"   ciudad = '{ciudad}' → tipo texto  (str)")

    anio = 2026 - edad
    print(f"\n🎮 RESULTADO:")
    print(f"   Hola {nombre}! Tienes {edad} años, vives en {ciudad}")
    print(f"   y naciste aproximadamente en {anio}.")

    if edad >= 18:
        print(f"   Eres mayor de edad ✅")
    else:
        print(f"   Te faltan {18 - edad} años para ser mayor de edad.")

    print("\n💡 LO QUE APRENDISTE:")
    print("   variable = valor       ← así se crea una variable")
    print("   str  = texto           ← entre comillas")
    print("   int  = número entero   ← sin comillas")
    print("   f'Hola {nombre}'       ← f-string: mezcla texto y variables")

    input("\n[Pulsa Enter para volver al menú]")


# ─── PLATO 2: LISTAS ────────────────────────────────────
defplato2_listas():
    print("\n🍲 PLATO 2 — LISTAS")
    print("─" * 42)
    print("Una lista guarda VARIOS datos en una sola variable.")
    print("Como una bolsa de la compra con varias cosas dentro.\n")

    lista = []
    print("🎮 JUEGO: Tu lista de deseos")
    print("Escribe 4 cosas que te gustaría tener o hacer:\n")

    for i in range(1, 5):
        deseo = input(f"  Deseo {i}: ")
        lista.append(deseo)
        print(f"  ✅ Añadido a la lista. Ahora tiene {len(lista)} elemento(s).")

    print("\n📦 Tu lista completa:")
    print(f"   {lista}")

    print("\n📊 Ordenada alfabéticamente:")
    for i, item in enumerate(sorted(lista), 1):
        print(f"   {i}. {item}")

    print(f"\n💡 LO QUE APRENDISTE:")
    print("   lista = []              ← lista vacía")
    print("   lista.append(cosa)      ← añadir elemento")
    print("   len(lista)              ← cuántos elementos tiene")
    print("   lista[0]                ← primer elemento (empieza en 0)")
    print("   lista[-1]               ← último elemento")
    print("   sorted(lista)           ← ordenar")

    input("\n[Pulsa Enter para volver al menú]")


# ─── PLATO 3: BUCLES ────────────────────────────────────
defplato3_bucles():
    print("\n🍕 PLATO 3 — BUCLES")
    print("─" * 42)
    print("Un bucle repite una acción automáticamente.")
    print("Sin bucles tendrías que escribir lo mismo 100 veces.\n")

    print("🎮 JUEGO 1: Cuenta atrás del cohete (bucle FOR)")
    try:
        inicio = int(input("  ¿Desde qué número? "))
    except:
        inicio = 5

    print(f"\n  🚀 Despegando en...")
    for i in range(inicio, 0, -1):
        print(f"     {i}...", end=" ", flush=True)
        time.sleep(0.4)
    print("\n  🚀 ¡DESPEGUE!")

    print(f"\n  💡 for i in range({inicio}, 0, -1): ← repitiose {inicio} veces")

    print("\n🎮 JUEGO 2: Contador tú mandas (bucle WHILE)")
    print("  El bucle while repite MIENTRAS se cumpla una condición.")
    contador = 0
    while True:
        seguir = input(f"  Contador: {contador} — ¿Seguir sumando? (s/n): ")
        if seguir.lower() != "s":
            break
        contador += 1
    print(f"  Paraste en {contador}. Tú controlabas el bucle con 'break'.")

    print("\n💡 LO QUE APRENDISTE:")
    print("   for i in range(n):      ← repite n veces")
    print("   while condicion:        ← repite mientras sea verdad")
    print("   break                   ← sale del bucle")

    input("\n[Pulsa Enter para volver al menú]")


# ─── PLATO 4: CONDICIONES ───────────────────────────────
defplato4_condiciones():
    print("\n🥩 PLATO 4 — CONDICIONES (if / elif / else)")
    print("─" * 42)
    print("Python puede tomar decisiones.")
    print("SI pasa esto → haz esto. SI NO → haz lo otro.\n")

    print("🎮 JUEGO: ¿Entras al club?")
    nombre = input("  Tu nombre: ")
    edad   = int(input("  Tu edad:   "))
    vip    = input("  ¿Tienes tarjeta VIP? (s/n): ").lower()

    print(f"\n  🎯 Analizando a {nombre}...")

    if vip == "s" and edad >= 18:
        zona = "Zona VIP ✨ — ¡Acceso total!"
    elif edad >= 18:
        zona = "Zona General ✅ — Puedes entrar."
    elif edad >= 16:
        zona = "Zona Joven 🟡 — Sin acceso al bar."
    else:
        zona = "❌ No puedes entrar todavía."

    print(f"  → {zona}")

    print("\n💡 LO QUE APRENDISTE:")
    print("   if condicion:           ← primera opción")
    print("   elif otra_condicion:    ← segunda opción (sino...)")
    print("   else:                   ← si ninguna anterior se cumple")
    print("   and / or               ← combinar condiciones")

    input("\n[Pulsa Enter para volver al menú]")


# ─── PLATO 5: FUNCIONES ─────────────────────────────────
defplato5_funciones():
    print("\n🍰 PLATO 5 — FUNCIONES (def)")
    print("─" * 42)
    print("Una función es código que escribes una vez")
    print("y puedes usar cuantas veces quieras.\n")

    def saludar(nombre, idioma="español"):
        saludos = {
            "español": f"¡Hola, {nombre}! 👋",
            "inglés":  f"Hello, {nombre}! 👋",
            "francés": f"Bonjour, {nombre}! 👋",
            "italiano": f"Ciao, {nombre}! 👋",
        }
        return saludos.get(idioma, f"¡Hola en cualquier idioma, {nombre}! 🌍")

    print("🎮 JUEGO: La máquina de saludos")
    print("Introduce 3 nombres y un idioma.")
    print("La misma función saluda a todos de golpe:\n")

    nombres = []
    for i in range(1, 4):
        n = input(f"  Nombre {i}: ")
        nombres.append(n)

    print("  Idiomas disponibles: español / inglés / francés / italiano")
    idioma = input("  ¿En qué idioma saludamos? ")

    print("\n  ✅ Resultados:")
    for nombre in nombres:
        print(f"     {saludar(nombre, idioma)}")

    print(f"\n  La función se ejecutó {len(nombres)} veces, escrita solo 1 vez.")

    print("\n💡 LO QUE APRENDISTE:")
    print("   def nombre_funcion(parametro):  ← definir")
    print("   return resultado                ← devolver valor")
    print("   nombre_funcion('dato')          ← llamar/usar")

    input("\n[Pulsa Enter para volver al menú]")


# ─── PLATO 6: PROYECTO FINAL ────────────────────────────
defplato6_proyecto_final():
    print("\n🎂 PLATO 6 — PROYECTO FINAL")
    print("─" * 42)
    print("Aquí usas TODO lo aprendido:")
    print("variables + listas + bucles + condiciones + funciones\n")

    # FUNCIÓN
    def evaluar(intentos_usados, max_i):
        if intentos_usados == 1:
            return "¡Mente de ordenador! 🧠"
        elif intentos_usados <= max_i // 2:
            return "¡Muy bien! 🌟"
        elif intentos_usados <= max_i:
            return "¡Lo conseguiste! 👍"
        else:
            return "La próxima vez 💪"

    # VARIABLES
    secreto      = random.randint(1, 20)
    max_intentos = 6
    intentos     = 0
    historial    = []  # LISTA

    print("🎮 ADIVINA EL NÚMERO")
    print(f"Tengo un número del 1 al 20. Tienes {max_intentos} intentos.\n")

    # BUCLE WHILE
    while intentos < max_intentos:
        try:
            intento = int(input(f"  Intento {intentos+1}/{max_intentos} → "))
        except:
            print("  Escribe un número válido.")
            continue

        historial.append(intento)
        intentos += 1

        # CONDICIONES IF/ELIF/ELSE
        if intento == secreto:
            print(f"\n  🎉 ¡CORRECTO! Era el {secreto}.")
            break
        elif intento < secreto:
            print(f"  ⬆️  Más alto. Quedan {max_intentos - intentos} intentos.")
        else:
            print(f"  ⬇️  Más bajo. Quedan {max_intentos - intentos} intentos.")
    else:
        print(f"\n  ❌ Sin intentos. El número era {secreto}.")

    print(f"\n  📋 Historial de intentos: {historial}")
    print(f"  📊 Valoración: {evaluar(intentos, max_intentos)}")

    print("\n💡 EN ESTE JUEGO USASTE:")
    print("   ✅ Variables  (secreto, intentos, max_intentos)")
    print("   ✅ Lista      (historial de intentos)")
    print("   ✅ Bucle while (repite hasta acertar o agotar)")
    print("   ✅ Condiciones (más alto / más bajo / correcto)")
    print("   ✅ Función    (evaluar resultado final)")
    print("   ✅ random     (número aleatorio)")

    input("\n[Pulsa Enter para volver al menú]")


# ─── PROGRAMA PRINCIPAL ──────────────────────────────────
def main():
    print("\n¡Bienvenida al Restaurante de Python! 🍽️")
    nombre = input("¿Cómo te llamas? ")
    print(f"\nEncantado, {nombre}. Aquí aprenderás Python jugando.")
    print("Puedes hacer los platos en cualquier orden.\n")

    platos = {
        "1": plato1_variables,
        "2": plato2_listas,
        "3": plato3_bucles,
        "4": plato4_condiciones,
        "5": plato5_funciones,
        "6": plato6_proyecto_final,
    }

    completados = []

    while True:
        mostrar_menu()
        if completados:
            print(f"  ✅ Completados: {completados}\n")
        eleccion = input("  ¿Qué plato eliges? ")

        if eleccion == "0":
            print(f"\n👋 ¡Hasta pronto, {nombre}! Sigue programando 🐍")
            if len(completados) == 6:
                print("  🏆 ¡Completaste el menú entero! Eres una programadora.")
            break
        elif eleccion in platos:
            platos[eleccion]()
            if eleccion not in completados:
                completados.append(f"Plato {eleccion}")
        else:
            print("  Elige una opción del 0 al 6.")

main()
