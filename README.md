# Evaluador de Nivel de Compromiso de Sesiones de Clientes

 
**Fase:** 5 - Evaluación Final POA  

---

## Descripción

Programa en Python que analiza sesiones de clientes almacenadas en una matriz y clasifica el nivel de compromiso de cada sesión según su duración y cantidad de clics.

## Estructura del proyecto

```
📄 problema1_sesiones.py   # Código fuente principal
📄 README.md               # Este archivo
```

## Cómo ejecutar

```bash
python problema1_sesiones.py
```

## Lógica de clasificación

| Condición | Clasificación |
|-----------|--------------|
| Duración > 180s **Y** Clics > 8 | Alto |
| Duración < 60s **O** Clics < 3 | Bajo |
| Cualquier otro caso | Medio |

## Ejemplo de salida

```
==================================================
  INFORME DE NIVEL DE COMPROMISO POR SESIÓN
==================================================
ID Cliente   Duración (s)    Clics    Clasificación
--------------------------------------------------
C001         210             12       Alto
C002         45              2        Bajo
C003         130             5        Medio
==================================================
```
