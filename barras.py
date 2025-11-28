"""Barras de progreso en texto para la terminal."""


def barra(parte, total, ancho=20):
    """Dibuja una barra de progreso de `ancho` caracteres."""
    if total <= 0:
        raise ValueError("total debe ser > 0")
    hechos = int(round(ancho * parte / total))
    hechos = max(0, min(ancho, hechos))
    return "[" + "#" * hechos + "-" * (ancho - hechos) + "]"


def porcentaje(parte, total, decimales=0):
    """El avance en tanto por ciento, con los decimales pedidos."""
    return "%.*f%%" % (decimales, 100.0 * parte / total)


def linea(etiqueta, parte, total, ancho=20):
    """Junta etiqueta, barra y porcentaje en una linea de terminal."""
    return "%s %s %4s" % (etiqueta, barra(parte, total, ancho),
                          porcentaje(parte, total))
