"""Mide el coste de pintar muchas lineas de progreso.

Se ejecuta desde la raiz del repo para que `barras` este en la ruta:

    python -m bench.medir
"""
import time

from barras import linea


def main():
    total = 200000
    arranque = time.perf_counter()
    for i in range(total):
        linea("copiando", i, total)
    print("%d lineas en %.3f s" % (total, time.perf_counter() - arranque))
    print(linea("copiando", total, total))


if __name__ == "__main__":
    main()
