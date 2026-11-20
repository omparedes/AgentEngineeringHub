# Escenarios reproducibles

Todos los proyectos y necesidades de estos ejemplos son sintéticos. Los comandos se ejecutan desde el checkout del Hub.

## Codex · una RPC usada por un cliente anterior

**Solicitud.** «Añadimos una pantalla Angular 22. Cambia una RPC que aún usa una aplicación móvil. Tenemos migraciones en Git y Pages ya está elegido. Prepara el cambio con material local».

```console
python scripts/hub.py recommend angular-supabase-cloudflare --agent codex --context cambio-existente --context cambio-sql
python scripts/hub.py show cambio-controlado
```

La propuesta incluye `angular-skills`, `project-bootstrap`, `supabase-skills`, `change-impact-analysis` y su workflow `cambio-controlado`. La configuración de Pages ya está decidida. Mantén inactiva la condición `hosting` hasta que haya una decisión nueva.

En el agente, pide: «Usa project-bootstrap del checkout del Hub. Distingue las pruebas que ya existen de las que propones». Una respuesta aceptable registra el contrato del móvil, propone probar parámetros y respuestas antiguas y nuevas, y describe la reversión si una migración deja datos incompatibles. Las migraciones versionadas bastan para preparar el análisis; no se necesita autenticar Supabase.

## Antigravity · regla de aprobación ambigua

**Solicitud.** «Un supervisor suele aprobar devoluciones grandes. Documenta lo que sabemos antes de diseñar el formulario».

```console
python scripts/hub.py recommend business-discovery --agent antigravity
python scripts/hub.py show domain-discovery
```

En un proyecto donde se haya incorporado esa skill, pide en Antigravity App o CLI: «/domain-discovery usa esta entrevista como única fuente y entrega una ficha reutilizable». El resultado esperado contiene el supervisor como actor, la práctica observada y preguntas sobre importe, moneda, obligatoriedad y excepciones. El umbral permanece abierto. La propuesta local recomienda `domain-discovery` y después `descubrimiento`.

## Web · seleccionar un navegador sólo para una tarea concreta

```console
python scripts/hub.py recommend generic-web --context prueba-navegacion --include playwright-mcp
```

La opción añade Playwright MCP a la **propuesta** e indica sus requisitos. Si el proyecto ya cuenta con una prueba de regresión adecuada, documenta esa alternativa y conserva la selección mínima.
