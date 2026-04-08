# ============================================================
# 🐍 EJERCICIO 06 — PROYECTO INTEGRADOR
#    Mini gestor de tareas por consola
# ============================================================
# En este ejercicio usas TODO lo aprendido:
#
#   ✅ Variables     → guardar datos
#   ✅ Listas        → guardar varias tareas
#   ✅ Condiciones   → decidir qué hacer según la opción
#   ✅ Bucles        → repetir el menú hasta salir
#   ✅ Funciones     → organizar el código en bloques
# ============================================================

# ── PARTE RESUELTA ──────────────────────────────────────────

tareas = []   # lista donde guardamos las tareas

def mostrar_tareas():
    """Muestra todas las tareas con su número."""
    if len(tareas) == 0:
        print("  No hay tareas todavía.")
    else:
        for i, tarea in enumerate(tareas, 1):
            print(f"  {i}. {tarea}")

def añadir_tarea(nueva):
    """Añade una tarea nueva a la lista."""
    tareas.append(nueva)
    print(f"  ✅ Tarea añadida: '{nueva}'")

def completar_tarea(numero):
    """Elimina la tarea en la posición indicada."""
    if 1 <= numero <= len(tareas):
        eliminada = tareas.pop(numero - 1)
        print(f"  ✔️  Completada y eliminada: '{eliminada}'")
    else:
        print("  ⚠️  Número de tarea no válido.")

# Bucle principal
while True:
    print("\n─── GESTOR DE TAREAS ──────────────")
    print("  1. Ver tareas")
    print("  2. Añadir tarea")
    print("  3. Completar tarea")
    print("  4. Salir")
    print("────────────────────────────────────")

    opcion = input("  Elige una opción (1-4): ")

    if opcion == "1":
        mostrar_tareas()
    elif opcion == "2":
        nueva = input("  ¿Qué tarea quieres añadir? ")
        añadir_tarea(nueva)
    elif opcion == "3":
        mostrar_tareas()
        try:
            num = int(input("  ¿Qué número de tarea completaste? "))
            completar_tarea(num)
        except ValueError:
            print("  Escribe un número válido.")
    elif opcion == "4":
        print("  👋 ¡Hasta luego!")
        break
    else:
        print("  Opción no válida. Elige entre 1 y 4.")


# ── TU TURNO ────────────────────────────────────────────────
# Añade esta función al programa de arriba:
# "buscar_tarea(palabra)" → muestra las tareas que contengan esa palabra
#
# Pista:
#   if "texto" in variable:   ← comprueba si un texto está dentro de otro

def buscar_tarea(palabra):
    resultados = []
    for tarea in tareas:
        if ___ in ___:           # ← completa con: palabra in tarea
            resultados.append(tarea)
    if resultados:
        print(f"  Tareas con '{palabra}':", resultados)
    else:
        print(f"  No hay tareas con '{palabra}'.")
