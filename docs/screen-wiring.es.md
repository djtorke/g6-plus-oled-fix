# Sustitución de la pantalla OLED

Estas fotografías son del módulo de reemplazo empleado en la reparación comunicada. La placa azul está marcada `0.42" OLED IIC VER1.1`; el flex lleva `V01870-MF1-B`. El controlador exacto no está confirmado. La pantalla original llevaba `G6_OLED_V2` y su flex estaba marcado `HP7240-01`.

![Vista frontal de la pantalla de reemplazo](images/replacement-front.jpg)

![Parte trasera de la placa de reemplazo y cables](images/replacement-back.jpg)

![Detalle del flex de la pantalla de reemplazo](images/replacement-flex.jpg)

## Señales y conexión

El módulo de la reparación utiliza cuatro conexiones. Conecta cada señal con su equivalente, identificando primero **ambos extremos**; el orden físico de los pads y el conector puede variar entre placas.

| Señal del gimbal | Señal equivalente del módulo | Función |
|---|---|---|
| GND | GND | Masa |
| Alimentación OLED | VCC/VDD de entrada del módulo | Alimentación; verificar tensión y compatibilidad del módulo |
| SCL | SCL / CLK | Reloj I²C |
| SDA | SDA / DATA | Datos I²C |

En este G6 Plus el usuario comprobó continuidad entre SCL y PB8 del GD32, y entre SDA y PB9. Es una referencia de señales, no un orden de cables del conector de la pantalla. Las fotos disponibles no dejan leer todas las etiquetas y no se ha documentado el orden exacto del conector original ni los colores: **no se puede indicar qué posiciones deben cruzarse**.

1. Retira batería y USB. Fotografía y etiqueta los cables y ambos conectores antes de desoldar; no te guíes solo por su color o posición.
2. Identifica GND, alimentación, SCL y SDA en ambos extremos mediante serigrafía, documentación del módulo y continuidad con todo desconectado. Confirma la tensión de alimentación y que sea compatible con el módulo: la tolerancia de la placa adaptadora no se deduce del controlador anunciado.
3. Si el orden de los contactos difiere, reubica o cruza **cada cable según su señal**. Suelda a los pads correspondientes del módulo sin trasladar automáticamente el orden del conector original. El número y función de los contactos del flex de 16 vías no son equivalentes a los cuatro pads externos.
4. Inspecciona las soldaduras; con todo desenergizado comprueba continuidad de cada hilo y ausencia de cortos entre pads vecinos y entre alimentación y masa. Aísla las conexiones y fija el conjunto sin presionar el cristal ni el flex antes de cerrar.

El [post de reparación de un G6](https://www.facebook.com/groups/SGHomeDIY/posts/9002169799856864/) se menciona como referencia de otra reparación, no como confirmación del pinout de este G6 Plus: no se ha podido acceder al contenido completo ni verificar sus conexiones.

Después de la sustitución, el parche experimental documentado en el [README](../README.es.md) resolvió el apagado parcial en un aparato. La conexión correcta de las señales y la compatibilidad de alimentación se deben verificar independientemente del firmware.
