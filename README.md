# granitepad

![tests](https://github.com/ElecBen/granitepad/actions/workflows/tests.yml/badge.svg)

Dibuja barras de progreso y avisos de avance en texto.

## Uso

```python
from barras import linea

linea("bajando", 3, 10)  # "bajando [######--------------]  30%"
```

## Estructura

```
barras.py  modulo principal
tests/     tests con pytest
docs/      notas de diseno
```

## API

| funcion | que devuelve |
| --- | --- |
| `barra(parte, total, ancho)` | la barra de progreso entre corchetes |
| `porcentaje(parte, total, decimales)` | el avance en tanto por ciento, ya formateado |
| `linea(etiqueta, parte, total, ancho)` | la etiqueta, la barra y el porcentaje en una sola linea |
| `restante(hechos, total, transcurrido)` | los segundos que quedan al ritmo actual, o None |
| `girador(i, marcos)` | el marco de la ruedecilla que toca en cada paso |

## Medir

El banco de pruebas vive en `bench/` y se lanza como modulo, siempre desde la raiz del repo:

```
python -m bench.medir
```
