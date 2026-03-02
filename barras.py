"""Barras de progreso en texto para la terminal."""

from __future__ import annotations

__all__ = ["barra", "girador", "linea", "porcentaje", "restante"]


def barra(parte: float, total: float,
          ancho: int = 20) -> str:
    """Dibuja una barra de progreso de `ancho` caracteres."""
    if total <= 0:
        raise ValueError("total debe ser > 0")
    hechos = int(round(ancho * parte / total))
    hechos = max(0, min(ancho, hechos))
    return "[" + "#" * hechos + "-" * (ancho - hechos) + "]"


def porcentaje(parte: float, total: float,
               decimales: int = 0) -> str:
    """El avance en tanto por ciento, con los decimales pedidos."""
    return "%.*f%%" % (decimales, 100.0 * parte / total)


def linea(etiqueta: str, parte: float, total: float,
          ancho: int = 20) -> str:
    """Junta etiqueta, barra y porcentaje en una linea de terminal."""
    return "%s %s %4s" % (etiqueta, barra(parte, total, ancho),
                          porcentaje(parte, total))


def restante(hechos: float, total: float,
             transcurrido: float) -> float | None:
    """Estimacion de los segundos que quedan al ritmo de hasta ahora."""
    if hechos <= 0:
        return None
    return transcurrido * (total - hechos) / hechos


def girador(i: int, marcos: str = ".oO@") -> str:
    """El marco de la ruedecilla que toca en el paso i."""
    return marcos[i % len(marcos)]
