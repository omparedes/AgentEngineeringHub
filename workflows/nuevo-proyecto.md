# Nuevo proyecto con Domain-First Agile Engineering

**Entrada.** Petición, objetivo inicial, roles que pueden confirmar el proceso, restricciones y evidencia disponible.

1. Ejecuta `project-bootstrap` para identificar el perfil, la fase y qué incertidumbre conviene resolver primero. Si el sistema ya está en uso, abre [cambio controlado](cambio-controlado.md) para delimitar el impacto.
2. Aplica [descubrimiento](descubrimiento.md) y usa la [ficha de dominio](../templates/dominio.md). Consulta a quienes deciden y a quienes realizan el trabajo cotidiano. Obtén un caso normal y una excepción. Registra contradicciones y fuentes ausentes.
3. Consolida el material autorizado con [consolidación de ideas](../templates/consolidacion-ideas.md). Valida con el rol responsable las decisiones que condicionan el alcance. Mantén material privado en el espacio autorizado del proyecto.
4. Redacta el [backlog](../templates/backlog-producto.md) y, si hay módulos o integraciones, el [mapa](../templates/mapa-modulos.md). Elige un incremento que incluya un recorrido y datos verificables. Aplaza decisiones que no bloqueen ese incremento.
5. Si la interfaz contiene decisiones abiertas, sigue [prototipado y validación](prototipado-validacion.md). Cuando el flujo quede aprobado, maquétalo con estados y fixtures identificados. Mantén los contratos de los servicios que se incorporarán después.
6. Implementa un recorrido por incremento. Comprueba reglas, permisos y persistencia que correspondan, ensaya errores y actualiza el backlog con el resultado de la revisión.
7. Aplica [cambio controlado](cambio-controlado.md) para preparar Preview, migración, reversión y revisión de producción. Recoge métricas o feedback posterior para decidir el siguiente incremento.

**Salida observable.** El equipo puede vincular la primera entrega con el problema inicial, demostrar su comportamiento y describir el paso siguiente. En un proyecto pequeño puede reunir los registros en un solo documento. [Metodología y variantes](../docs/metodologia/domain-first-agile-engineering.md)
