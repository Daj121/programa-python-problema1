# ============================================================
# Problema 1 - Una matriz almacena datos de sesiones de clientes con el formato: [ID Cliente, Duración (segundos), Eventos Clics]. 
# ============================================================

# --- Función Clasificar Compromiso ---
def clasificar_compromiso(duracion, clics):
    """Determina el nivel de compromiso de una sesión."""
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"


# --- INGRESO DINÁMICO DE DATOS ---
def ingresar_sesiones():
    sesiones = []
    print("=== INGRESO DE SESIONES ===\n")

    while True:
        id_cliente = input("ID Cliente: ").strip()
        try:
            duracion = int(input("Duracion (segundos): "))
            clics    = int(input("Eventos Clics: "))
            sesiones.append([id_cliente, duracion, clics])
            print()
        except ValueError:
            print("Error: duracion y clics deben ser numeros enteros.\n")
            continue

        continuar = input("Agregar otra sesion? (s/n): ").strip().lower()
        print()
        if continuar != "s":
            break

    return sesiones


# --- PROGRAMA PRINCIPAL ---
def main():
    sesiones = ingresar_sesiones()

    if not sesiones:
        print("No se ingresaron sesiones.")
        return

    print("\n" + "=" * 50)
    print("  INFORME DE NIVEL DE COMPROMISO POR SESION")
    print("=" * 50)
    print(f"{'ID Cliente':<12} {'Duracion (s)':<15} {'Clics':<8} {'Clasificacion'}")
    print("-" * 50)

    for sesion in sesiones:
        id_cliente = sesion[0]
        duracion   = sesion[1]
        clics      = sesion[2]
        nivel      = clasificar_compromiso(duracion, clics)
        print(f"{id_cliente:<12} {duracion:<15} {clics:<8} {nivel}")

    print("=" * 50)
    print(f"Total sesiones: {len(sesiones)}")


main()
