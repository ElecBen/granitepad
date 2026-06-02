# Notas de diseno

`barra()` recorta el numero de bloques al ancho en lugar de
protestar cuando `parte` se pasa de `total`. Un contador que se pasa es un
error de quien cuenta, y comerse la barra entera del terminal seria peor.

El porcentaje se formatea con %.*f para poder elegir los decimales
sin construir la cadena de formato a mano. Con cero decimales queda un entero
sin punto, que es lo que se quiere en una linea estrecha.

`restante()` devuelve None mientras no haya nada hecho, en vez de
cero o de infinito. Quien pinta la linea decide si escribe "--:--"; el modulo
no se inventa una estimacion que no tiene.
