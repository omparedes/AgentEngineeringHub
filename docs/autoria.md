# Añadir una capacidad o un perfil

Empieza buscando por función y proveedor. Dos clientes para el mismo servidor suelen compartir ficha. Abre un ID distinto si cambian de manera significativa el propósito, los requisitos o las decisiones de selección. Elige `origin: community` cuando una integración sea mantenida fuera del proveedor aunque trabaje con su producto.

## Una skill propia

1. Elige un ID en minúsculas, con guiones simples, de hasta 64 caracteres. Crea `skills/ID/SKILL.md`; reserva `.agents/skills/` para procedimientos necesarios al mantener el Hub.
2. Usa frontmatter YAML con `name` igual al directorio y una `description` que indique resultado y disparador. Describe entradas, decisiones, límites, evidencia de salida y un caso de uso. Incluye referencias auxiliares sólo si se consultan bajo una condición concreta. [Especificación](https://agentskills.io/specification)
3. Parte de la [ficha de dominio](../catalog/domain-discovery.yaml). Cambia ID, alcance, prerrequisitos y `entry` para enlazar el archivo real. Fija revisión y licencia. Si la skill necesita este checkout al distribuirse, indica cómo localizarlo.
4. Ejecuta `validate` y las pruebas. Ensaya una petición representativa y una parecida que no deba activar la skill. Comprueba una decisión o artefacto observable y documenta el cliente empleado. Una prueba de metadatos por sí sola permite declarar `metadata-checked`.
5. Si la skill es externa, registra sus fuentes y el procedimiento de incorporación en una ficha. Examina los scripts y el alcance; evita incorporar el código upstream al Hub.

## Un servidor MCP

Usa la [ficha Angular CLI MCP](../catalog/angular-cli-mcp.yaml) para un proceso stdio y la [ficha Supabase MCP](../catalog/supabase-mcp.yaml) para un servicio remoto. Identifica endpoint o binario, propietario, transporte, operaciones posibles, autenticación, dependencias, privilegios y alternativa local. Indica si la licencia cubre código, guías o servicio.

Para una receta nueva agrega un archivo inerte en `mcp/` y enlázalo desde su [guía](../mcp/README.md). Representa parámetros de proyecto con marcadores. No asumas que un cliente acepta el formato de configuración de otro. Documenta conexión, resultado esperado y cómo retirar esa configuración. Actualiza `review.runtime` sólo si existe evidencia del ensayo; registra en qué cliente y superficie se hizo.

## Un perfil

1. Parte del [perfil de frontend](../profiles/angular-frontend.yaml). Usa `activate_when` para delimitar el tipo de proyecto y `stack` para tecnologías observadas. Las condiciones describen hechos de la tarea que un operador puede confirmar sin red.
2. Por cada `choice` escribe ID, nivel, razón y lista `when`. Una dependencia debe aparecer en el perfil y ser elegible siempre que lo sea su consumidor. Una capacidad marcada no aplicable puede documentar una exclusión útil.
3. Reutiliza IDs existentes. Reserva `conflicts_with` para incompatibilidades reales; dos navegadores que cubren una tarea pueden ser alternativas sin ser incompatibles.
4. Prueba el caso por defecto, una condición activada y la inclusión indebida de un ID. Para una tecnología nueva confirma que las fichas relevantes se puedan encontrar con `list --tech`.

## Formato de datos

Se admite un objeto YAML o JSON por archivo, con nombre igual al ID. Las fechas YAML deben ser cadenas ISO entre comillas. Se rechazan claves repetidas, alias YAML y campos desconocidos. Los esquemas de [capacidad](../schemas/capability.schema.json), [perfil](../schemas/profile.schema.json) y [frontmatter](../schemas/skill.schema.json) definen campos y enumeraciones. Usa referencias locales relativas a la raíz en `entry` y relativas al documento en enlaces Markdown. Conserva las URLs de fuentes en HTTPS.

Si cambia el contrato, añade pruebas para registros anteriores y documenta el orden de migración. Extender primero la lectura y migrar después permite que la CI de una rama base siga entendiendo las contribuciones.
