---
description: Capturas y verificacion visual con Playwright, nunca con el navegador interno de Cursor
alwaysApply: true
---

# Navegador: Playwright

El navegador interno de Cursor recorta la pagina. Para abrir el ERP, sacar capturas, armar recorridos o comprobar una pantalla usa Playwright (`plugin-playwright-playwright`). No uses el navegador interno de Cursor para eso.

- No fijes un viewport mas chico que la ventana. Con zoom del navegador, la captura usa la ventana completa: menu, contenido y paneles laterales. Si un control queda fuera, no achiques la ventana.
- La imagen tiene que mostrar la pagina completa: menu, contenido y paneles laterales. Si un control queda fuera, toma la pagina completa.
- Los marcadores de un recorrido van en porcentaje del ancho y del alto de esa imagen, y tienen que caer sobre el control (boton, campo o combo).
- No guardes, contabilices ni pagues documentos solo para sacar la foto.
