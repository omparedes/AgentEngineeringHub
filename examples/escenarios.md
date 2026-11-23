# Escenarios reproducibles

Todos los proyectos y necesidades de estos ejemplos son sintéticos. Los comandos se ejecutan desde el checkout del Hub.

## Codex · una RPC usada por un cliente anterior

**Solicitud.** «Añadimos una pantalla Angular 22. Cambia una RPC que aún usa una aplicación móvil. Tenemos migraciones en Git y Pages ya está elegido. Prepara el cambio con material local».

```console
python scripts/hub.py recommend angular-supabase-cloudflare --agent codex --context trabajo-frontend --context cambio-existente --context cambio-sql
python scripts/hub.py show cambio-controlado
```

La propuesta incluye `angular-skills`, `modern-web-guidance`, `project-bootstrap`, `supabase-skills`, `change-impact-analysis` y su workflow `cambio-controlado`. La configuración de Pages ya está decidida. Mantén inactiva la condición `hosting` hasta que haya una decisión nueva.

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

## Frontend React y Next.js

Usa un portafolio ficticio con React, Next.js, TypeScript y Tailwind CSS. El alcance de ejemplo comprende una galería de proyectos y un formulario de contacto ya existentes. Consulta el perfil desde el Hub:

```powershell
python scripts/hub.py recommend generic-web --agent codex --context trabajo-frontend --context cambio-existente
python scripts/hub.py show modern-web-guidance
```

La propuesta incluye Modern Web Guidance para la plataforma web y `cambio-controlado` con su análisis de impacto. Los perfiles también aceptan `--agent antigravity`.

| Parte de la interfaz | Consulta genérica y comprobación propuesta |
| --- | --- |
| Responsive y tarjetas interactivas | `responsive container queries`. Ensaya tarjetas en una columna estrecha y un área ancha. Comprueba que cada enlace y botón conserve su semántica y su foco. |
| Formulario | `accessible form validation`. Comprueba etiquetas, mensajes de error, autocompletado y teclado. Mantén la validación de servidor del consumidor. |
| Galería, animaciones y accesibilidad | `accessible image gallery` y `reduced motion animation`. Comprueba orden del foco, texto alternativo, Escape si hay diálogo y preferencias de movimiento. Considera CSS nativo o Motion for React según el requisito de interacción. |
| Rendimiento | `optimize responsive images`. Contrasta la guía con `next/image` y la configuración del consumidor. Mide LCP, INP y CLS en un entorno comparable antes y después. |

Adapta las guías al límite servidor/cliente de Next.js y a las clases CSS del proyecto. Confirma el soporte de los navegadores objetivo antes de elegir fallbacks. La propuesta enumera guías, cambios, riesgos y pruebas. El agente sólo aplica cambios cuando el usuario aprueba el alcance. [Guía de uso](../docs/modern-web-guidance.md) · [Workflow de cambio controlado](../workflows/cambio-controlado.md#modernización-frontend)
