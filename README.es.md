# Reparación experimental de pantalla OLED — FeiyuTech G6 Plus

Este proyecto prepara una modificación para el firmware **AJB/teclado Sony V1.10** del G6 Plus. La pantalla de reemplazo de un usuario se apagaba parcialmente tras unos segundos y mostraba un destello breve. Tras instalar esta variante, el usuario comunicó que funciona correctamente. Es un caso comprobado, no una garantía para todos los aparatos.

El flex de la pantalla de reemplazo lleva `V01870-MF1-B`. No se ha identificado su controlador: SSD1315 es una hipótesis. El flex de la pantalla original llevaba `HP7240-01`.

## Antes de empezar

- La modificación corresponde al firmware **teclado/AJB**, no al firmware GIMBAL. No se ha probado en otras versiones o variantes.
- Una actualización puede fallar y dejar el aparato inutilizable. Feiyu documenta la actualización mediante adaptador USB serie, pero no hemos demostrado la recuperación tras un fallo. Conserva el firmware oficial adecuado y el actualizador.
- Obtén por separado el archivo oficial WIRE **AJB Sony V1.10**. El generador solo acepta el SHA-256 exacto indicado debajo. No se ha confirmado que esté disponible actualmente en la [página oficial de descargas](https://www.feiyu-tech.com/g6-plus/down.html).

## Crear el archivo

Con Python 3 instalado, ejecuta:

```powershell
python patch_firmware.py "C:\ruta\G6P_AJB_Sony_WIRE_V1.10.bin" "C:\ruta\G6P_AJB_SONY_V110_OLED_EXPERIMENTAL.bin"
```

SHA-256 del original: `e4471c6d6cb3b50f2d39f178900d1ce4a52f6f71e53d90f5bc46123b3d090a3e`

SHA-256 del resultado: `eabe3b903c6fc2a21df7c45e053bf89792b0c51d27a8ef518643682c676c18b3`

El programa verifica el archivo original, la cabecera, el CRC y el resultado; tampoco sobrescribe archivos existentes. No se conecta al gimbal.

Para instalarlo, sigue el manual del fabricante para actualizar la placa **teclado/AJB** con el actualizador Windows y un adaptador USB serie. El manual indica 115200 baudios y batería instalada. En el caso comunicado no se leyó el firmware instalado antes ni después, por lo que su variante previa no quedó identificada de forma independiente. No se ha verificado que sea posible recuperar el aparato por USB tras un fallo.

## Qué cambia

El código analizado envía periódicamente `40 81 AD 30` a la pantalla. La modificación elimina una llamada y una emulación acotada observó `40 AD 30`. No cambia el multiplexado de 64 líneas. Todavía no sabemos exactamente cómo interpreta esas transacciones el controlador real ni por qué el cambio resolvió este caso. Consulta los [detalles técnicos](docs/technical.md).

Si lo pruebas, comparte modelo, versión, marcas de pantalla, síntoma y resultado, sin datos personales ni archivos de firmware propietario.
