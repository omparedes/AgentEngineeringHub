# Prototipado y validación de una interfaz

**Entrada.** Objetivo del recorrido, rol principal, reglas respaldadas, escenarios de excepción, contexto de dispositivos y sistema de diseño si existe.

1. Describe entrada, decisiones, salida y estados del recorrido. Incluye contenido vacío, carga, error, éxito y permiso denegado cuando apliquen. Define qué pregunta debe resolver el prototipo.
2. Elige la herramienta por esa pregunta. Usa un boceto local cuando alcance. Considera [Google Stitch](../catalog/google-stitch.yaml) para explorar alternativas con material saneado. Usa Figma cuando allí se mantiene el diseño aprobado o el equipo ha elegido ese flujo. [Intercambio con Stitch y Figma](../docs/prototipado.md)
3. Prepara sólo los estados necesarios para revisar el recorrido. Registra la versión, tamaño o breakpoint, acciones por teclado, foco, etiquetas y comportamiento por rol. En paralelo, acuerda contratos de datos y seguridad al nivel conceptual.
4. Recorre el prototipo con quienes deciden y operan. Completa [validación de prototipo](../templates/validacion-prototipo.md). Clasifica los hallazgos que bloquean el flujo, asigna responsable y fija criterios de aceptación comprobables. Repite la revisión de lo que cambie.
5. Una vez aprobada la versión, entrega al implementador las decisiones, estados, recursos autorizados y contratos pendientes. Adapta cualquier exportación al stack y al sistema de diseño. Etiqueta fixtures y mocks y comprueba la accesibilidad y responsividad sobre el producto implementado.

**Salida observable.** Hay una versión aprobada y un recorrido demostrable por rol. Los contratos pendientes, cambios y pruebas que se harán durante la implementación tienen un responsable.
