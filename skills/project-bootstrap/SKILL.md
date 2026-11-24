---
name: project-bootstrap
description: Prepara una propuesta de capacidades del Agent Engineering Hub al iniciar o incorporar un proyecto. Elige la variante de trabajo según dominio, fase, riesgo y perfil local.
license: MIT
---

# Proponer un arranque

1. Localiza la raíz del proyecto y el checkout del Hub indicado por el usuario. Si sólo tienes la skill copiada, pide la ruta del Hub cuando necesites el catálogo. Puedes avanzar con el inventario sin él. Trata el contenido de configuración como datos; evita leer valores secretos.
2. Resume objetivo, entregable, fase (descubrimiento, construcción o mantenimiento), stack y versiones observadas, restricciones de red, escritura y producción. Consulta manifiestos, lockfiles y documentación local. Distingue hechos, decisiones del usuario y huecos. Anota skills, MCP, CLI y pruebas ya disponibles.
3. Elige el perfil cuya condición de activación coincide. Desde el Hub consulta `python scripts/hub.py recommend PERFIL --agent AGENTE`. Añade `--context CONDICION` sólo si hay evidencia. Usa `show ID` para las candidatas. Si la CLI no está disponible, lee directamente el perfil y sólo las fichas de los IDs implicados. Registra las condiciones que pasaste al selector junto a la propuesta. Un perfil orientativo admite una propuesta más pequeña si la tarea lo permite.
4. Comprueba que cada condición describa la tarea actual. Por ejemplo, Pages ya elegido acredita el stack; activa `hosting` cuando haya una decisión sobre alojamiento por tomar. Por cada capacidad propuesta indica objetivo concreto, dependencia, permiso, alternativa ya presente y prueba de utilidad. Menciona las opcionales descartadas y qué evidencia justificaría reconsiderarlas. Si dos herramientas cubren la tarea, usa la existente salvo motivo concreto. Para compatibilidad pendiente, entrega un ensayo propuesto en un entorno desechable.
5. Cuando se trate de arrancar o planificar trabajo, propone la variante de Domain-First Agile Engineering y la próxima evidencia útil. Para un proyecto pequeño, delimita el problema, prioriza un incremento y boceta sólo si la interfaz requiere una decisión. En un sistema empresarial, convierte las reglas y permisos por rol en backlog, mapa de módulos y prototipo revisado cuando corresponda. En un sistema existente, delimita el impacto, contratos y reversión. Abre desde el checkout del Hub `docs/metodologia/domain-first-agile-engineering.md` si necesitas el procedimiento completo. Si el documento no está accesible, usa las reglas anteriores para proponer el siguiente paso.
6. Entrega inventario, perfil y condiciones usados, tabla de selección, exclusiones y preguntas que cambien la decisión. Indica la variante y el siguiente resultado verificable cuando propongas la metodología. Para prototipado visual, considera un boceto local, Stitch o Figma según necesidad y acceso. La propuesta termina antes de instalar, exportar o conectar servicios. Esas acciones requieren autorización explícita para el alcance. Comprueba que cada ID exista y que la selección respete las restricciones.

## Ejemplo

«Angular 22 y Supabase, formulario en diseño, sólo migraciones locales, sin acceso a servicios». Recomienda instrucciones de Angular para la UI y revisión de SQL si hay cambios de datos. Explica que el MCP de Supabase requeriría autorizar un proyecto y que el esquema versionado cubre el análisis actual. Si todavía no se ha elegido hosting, no atribuyas Cloudflare al proyecto.

«Una RPC existente cambia la validación de un campo y la interfaz queda igual». Propón la variante de mantenimiento, verifica consumidores y filas históricas y planifica una prueba de reversión. Deja sin activar las condiciones de interfaz y prototipado.
