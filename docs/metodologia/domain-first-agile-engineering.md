# Domain-First Agile Engineering

Domain-First Agile Engineering es la metodología personal del Hub para desarrollar aplicaciones con ayuda de agentes. Parte de entender cómo funciona el dominio, convierte lo aprendido en decisiones trazables y entrega incrementos verificables. Cada proyecto ajusta la profundidad según riesgo, tamaño y restricciones. Las fases o sprints son opciones de planificación. En un proyecto individual puede bastar una lista priorizada y una revisión por incremento.

## Etapas y evidencia para avanzar

| Etapa | Trabajo del equipo y del agente | Evidencia para avanzar |
| --- | --- | --- |
| A. Descubrimiento | Aclara el problema, el proceso actual y quién pide, opera, autoriza y recibe el resultado. Escucha a directivos y personal operativo. Reconstruye un caso normal y excepciones. Busca problemas omitidos en la solicitud original. | Actores, necesidades por rol, reglas y excepciones con fuente. Diferencia hechos confirmados, hipótesis y preguntas pendientes. |
| B. Consolidación | Usa ChatGPT u otro agente para ordenar notas, conversaciones e ideas que puedas compartir. Separa el negocio actual, los problemas, las restricciones y el alcance propuesto. Registra decisiones y desacuerdos. | Resumen, evidencia, actores, reglas, decisiones y preguntas con responsable. La propuesta conserva las incógnitas y sus fuentes. |
| C. Planificación | Define objetivos, requisitos funcionales y no funcionales, épicas, historias, criterios de aceptación, módulos y dependencias. Prioriza un MVP que entregue valor y planifica sprints o fases según el tamaño. | Backlog trazable y primer incremento que pueda demostrarse. El roadmap deja margen para ajustar alcance y prioridades cuando llegue evidencia nueva. |
| D. Prototipado visual | Explora pantallas, componentes y navegación con Stitch, Figma, bocetos locales u otra herramienta que sirva al proyecto. En paralelo, acuerda contratos, entidades conceptuales y necesidades de seguridad. Da prioridad al modelo conceptual antes de materializar almacenamiento. | Versión de prototipo revisada por los roles pertinentes. Registra comportamiento, responsividad, accesibilidad, estados y decisiones pendientes. |
| E. Maquetación inicial | Implementa componentes, navegación y estados con información ficticia, fixtures o mocks claramente identificados. Mantén un punto de integración definido para conectar servicios reales después. | La interfaz reproduce el recorrido aprobado. Las pruebas distinguen el comportamiento simulado del comportamiento respaldado por un servicio real. |
| F. Implementación por módulos | Entrega incrementos verticales con reglas, contratos, permisos, datos y pruebas. Incorpora autenticación y autorización, usuarios, procesos, consultas, persistencia, reportes, auditoría, integraciones o administración según el dominio. | Cada incremento resuelve un flujo verificable y tiene validaciones de contrato, permisos y errores acordes al riesgo. |
| G. Calidad y revisión | Ajusta pruebas unitarias, integración, E2E, roles, accesibilidad, rendimiento, seguridad, revisión visual y validación con usuarios. Elige herramientas cuando aporten una comprobación concreta. | Resultados que un revisor puede reproducir, defectos o riesgos registrados y criterios de aceptación pendientes explícitos. |
| H. Despliegue y mejora | Revisa cambios y migra datos de forma compatible. Usa Preview antes de producción cuando corresponda. Registra versión, autorización, reversión, monitoreo y retroalimentación. Prioriza requisitos nuevos a partir de los resultados. | Evidencia de Preview y de recuperación, responsable de aprobar y condición observable de parada. Después del despliegue, métricas o feedback enlazados al siguiente incremento. |

Las etapas permiten iterar. Una regla nueva puede devolver una historia a descubrimiento. Un problema de teclado puede devolver una pantalla a validación antes de consolidar la interfaz.

## Trazabilidad y privacidad

Usa IDs locales para enlazar origen, regla, historia, criterio y prueba. Por ejemplo, `E-01 → RN-01 → HU-01 → CA-01 → PR-01`. Si dos fuentes discrepan, conserva ambas y registra quién puede confirmar la regla. Una sugerencia del agente queda como hipótesis hasta que exista evidencia. Anota responsable, fecha y motivo cuando una decisión cambie.

Mantén entrevistas, notas crudas, enlaces privados, datos personales y credenciales fuera del repositorio público. En una sesión de ChatGPT o en una herramienta de diseño, usa sólo material cuyo tratamiento esté autorizado. Las fichas públicas usan referencias saneadas y ejemplos ficticios. Aplica la [política de seguridad del Hub](../../SECURITY.md).

## Adaptar la profundidad

| Variante | Práctica mínima | Qué activa más trabajo |
| --- | --- | --- |
| Ligera | Problema y audiencia, lista ordenada, boceto si cambia la navegación, primer incremento y pruebas de los recorridos principales. | Incertidumbre sobre el flujo o la interfaz, más roles o datos sensibles. |
| Empresarial | Entrevistas por rol, requisitos y decisiones trazables, mapa de módulos, prototipo revisado por operaciones, pruebas por rol y plan de recuperación. | Dependencias críticas, migraciones, auditoría, regulación o integraciones. Evalúa ASVS cuando corresponda. |
| Mantenimiento | Delimita el cambio, reconstruye el comportamiento actual y aplica análisis de impacto. Usa prototipo sólo si ayuda a decidir la interfaz. | Contratos incompatibles, persistencia, autorizaciones o producción crítica exigen más evidencia y secuencia de reversión. |

## Recursos del Hub

- Usa `project-bootstrap` para elegir variante, fase, siguiente evidencia y capacidades del perfil.
- Usa `domain-discovery` con el [workflow de descubrimiento](../../workflows/descubrimiento.md) para reconstruir el proceso y contrastar fuentes.
- Sigue [nuevo proyecto](../../workflows/nuevo-proyecto.md) para planificar y entregar desde el dominio. Para decisiones de interfaz abre [prototipado y validación](../../workflows/prototipado-validacion.md).
- Usa `change-impact-analysis` con [cambio controlado](../../workflows/cambio-controlado.md) antes de modificar un sistema existente.
- Usa `hub-maintainer` cuando la experiencia de un proyecto justifique revisar una ficha, un perfil o un procedimiento del Hub. Comparte evidencia saneada.

Consulta los [cuatro ejemplos de aplicación](../../examples/domain-first.md) para ver qué evidencia requiere cada variante.
