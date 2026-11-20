# Revisión de fuentes y decisiones

El reloj de cada ficha es `review.date` más `interval_days`. En la entrega inicial se sugieren 30 días para MCP y 90 para guías o skills. Abre una revisión antes si el proveedor anuncia deprecación, cambia la autenticación, amplía permisos o mueve el repositorio. La revisión produce una decisión por recurso.

| Estado del Issue | Evidencia para entrar | Siguiente decisión |
| --- | --- | --- |
| Nueva versión detectada | Tag, commit o aviso oficial distinto de la referencia anterior | Comparar cambios; una versión alojada puede diferir del código público. |
| Cambio relevante identificado | Diff o changelog concreta una diferencia de función, licencia, ruta o permiso | Enumerar clientes, fichas y perfiles que dependen del cambio. |
| Compatibilidad pendiente de comprobar | Existe una duda concreta de carga, transporte, API o alcance | Especificar entrada, entorno de ensayo y resultado esperado; mantener el estado real del runtime. |
| Cambio revisado | Evidencias contrastadas, incertidumbres y prueba o justificación de su ausencia | Presentar diff acotado y solicitar decisión humana. |
| Actualización aprobada | Revisor acepta el alcance y la evidencia del PR | Integrar el cambio revisado y enlazar el commit en el Issue. |
| Actualización descartada | Motivo registrado, por ejemplo un plugin duplicado o permisos desproporcionados | Conservar la ficha vigente y señalar qué nueva evidencia reabriría la revisión. |

Los estados anteriores describen un **cambio propuesto**. La ficha contiene el resultado de la última revisión de la **capacidad**. Un descarte no convierte el recurso actual en obsoleto.

## Procedimiento reproducible

1. Abre la [plantilla de revisión](../.github/ISSUE_TEMPLATE/revision.md). Anota ID, referencia vigente, nueva referencia y fuente de detección. Busca duplicados por función, proveedor y transporte.
2. Compara commits en el repositorio del proveedor, inspecciona changelog, README, manifiesto, licencia y ejemplos de alcance. Para un servicio alojado registra por separado la fecha de su documentación. Si un enlace se mueve, confirma la nueva propiedad.
3. Evalúa qué cambia para consumidores existentes. Ejemplo: para un nuevo grupo de operaciones en Supabase comprueba si modifica la configuración de sólo lectura o las expectativas del perfil. Si necesitas una prueba remota, propón una con datos sintéticos; deja el resultado pendiente hasta ejecutarla con autorización.
4. En el PR enlaza el Issue, agrega la referencia previa y nueva y actualiza sólo campos respaldados. Cambia `review.date` cuando se haya revisado la fuente. Conserva dudas y límites en `pending`. Sigue la [guía de pruebas](pruebas.md).
5. El revisor coteja fuentes, CI y decisión de alcance. El historial Git conserva el diff. En un checkout con historial, `git log --follow -- catalog/supabase-mcp.yaml` muestra cuándo y por qué cambió esa ficha.

## Futura detección programada

Un futuro lector periódico puede consultar únicamente metadatos públicos de una lista aprobada de repositorios. Debe registrar fecha, referencia previa y candidata, manejar límites de API, redirecciones y errores de red, y deduplicar por ID y referencia. Su salida será un informe revisable. Una referencia distinta nunca actualiza por sí sola compatibilidad, fecha de revisión o permisos. Esta versión mantiene el proceso manual.
