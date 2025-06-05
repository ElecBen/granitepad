def barra(parte, total, ancho=20):
    """Dibuja una barra de progreso de `ancho` caracteres."""
    if total <= 0:
        raise ValueError("total debe ser > 0")
    hechos = int(round(ancho * parte / total))
    hechos = max(0, min(ancho, hechos))
    return "[" + "#" * hechos + "-" * (ancho - hechos) + "]"
