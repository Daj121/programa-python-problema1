# Problema 1 - Evaluador de Nivel de Compromiso por Sesión

## Descripción
Herramienta interactiva que permite ingresar datos de sesiones de clientes y clasifica el nivel de compromiso de cada una según su duración y cantidad de clics.

## Estructura de Datos
Cada sesión se almacena en una matriz con el formato:

| Campo | Tipo | Descripción |
|---|---|---|
| ID Cliente | string | Identificador único del cliente |
| Duración | int | Duración de la sesión en segundos |
| Clics | int | Número de eventos de clic registrados |

## Lógica de Clasificación

| Nivel | Condición |
|---|---|
| **Alto** | Duración > 180s **Y** Clics > 8 |
| **Bajo** | Duración < 60s **O** Clics < 3 |
| **Medio** | Todos los demás casos |

## Módulos

### `clasificar_compromiso(duracion, clics)`
Recibe la duración y los clics de una sesión y retorna el nivel de compromiso: `"Alto"`, `"Medio"` o `"Bajo"`.

### `ingresar_sesiones()`
Solicita al usuario los datos de cada sesión de forma interactiva. Después de cada ingreso pregunta si desea agregar otra sesión.

### `main()`
Orquesta el flujo: llama al ingreso de datos y genera el informe final en consola.

## Cómo Ejecutar

```bash
python problema1_sesiones.py
```

## Ejemplo de Uso

```
=== INGRESO DE SESIONES ===

ID Cliente: C001
Duracion (segundos): 200
Eventos Clics: 10

Agregar otra sesion? (s/n): s

ID Cliente: C002
Duracion (segundos): 45
Eventos Clics: 2

Agregar otra sesion? (s/n): n

==================================================
  INFORME DE NIVEL DE COMPROMISO POR SESION
==================================================
ID Cliente   Duracion (s)    Clics    Clasificacion
--------------------------------------------------
C001         200             10       Alto
C002         45              2        Bajo
==================================================
Total sesiones: 2
```
