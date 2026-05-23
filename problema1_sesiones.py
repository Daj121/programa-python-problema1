# ============================================================
# Problema 1 - Una matriz almacena datos de sesiones de clientes con el formato: [ID Cliente, Duración (segundos), Eventos Clics]. 
# ============================================================

# --- DATOS INICIALES ---
# Matriz con formato: [ID Cliente, Duración, Eventos Clics]
sesiones = [
    ["C001", 210, 12],
    ["C002", 45,  2],
    ["C003", 130, 5],
    ["C004", 300, 9],
    ["C005", 55,  10],
    ["C006", 190, 7],
    ["C007", 30,  1],
]


# --- Función Clasificar Compromiso ---
def clasificar_compromiso(duracion, clics):
    """Determina el nivel de compromiso de una sesión."""
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"


# --- PROGRAMA PRINCIPAL ---
def main():
    print("=" * 50)
    print("  INFORME DE NIVEL DE COMPROMISO POR SESIÓN")
    print("=" * 50)
    print(f"{'ID Cliente':<12} {'Duración (s)':<15} {'Clics':<8} {'Clasificación'}")
    print("-" * 50)

    for sesion in sesiones:
        id_cliente = sesion[0]
        duracion   = sesion[1]
        clics      = sesion[2]
        nivel      = clasificar_compromiso(duracion, clics)
        print(f"{id_cliente:<12} {duracion:<15} {clics:<8} {nivel}")

    print("=" * 50)
    print("Fin del informe.")


main()
  
