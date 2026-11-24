# Consultar el catálogo y seleccionar capacidades

```console
python scripts/hub.py list --type skill
python scripts/hub.py list --tech postgresql
python scripts/hub.py show supabase-mcp
python scripts/hub.py profiles
python scripts/hub.py show angular-supabase-cloudflare
```

`list` es un índice compacto. `show` emite JSON de una sola ficha o perfil. Puedes leer directamente el YAML por ID. Todas estas operaciones son locales y repetibles.

## Cómo interpretar una ficha

`origin` indica si procede del proveedor, de la comunidad o del Hub. Context7 es oficial de Upstash; su procedencia no lo convierte en fuente oficial de las bibliotecas que indexa. `type` clasifica la capacidad seleccionable y `integration` describe su mecanismo. Un producto puede distribuir varias superficies. Por ejemplo, la ficha de Chrome prioriza MCP y señala el CLI y las skills disponibles.

`technologies` permite buscar; `requires_stack` exige que el perfil contenga todas esas tecnologías. `agents` son candidatos por formato o transporte. `compatibility` y `review.pending` explican las reservas. `requirements` documenta prerrequisitos humanos o técnicos; `depends_on` y `conflicts_with` contienen IDs del catálogo.

`review.status` admite `documented` para revisión de fuentes, `pending` para investigación incompleta y `local` para material propio. `review.runtime` describe el ensayo realmente hecho: `untested`, `metadata-checked`, `cli-help-checked` o `tested`. Para reproducir una revisión externa, abre el repositorio en el commit de `reference` y contrasta su README con `docs`. La documentación en línea y los servicios alojados pueden evolucionar independientemente de ese commit.

En las fichas externas iniciales, `review.upstream` conserva el indicador de archivo y la fecha UTC del commit consultados en la API pública del repositorio. La fecha de revisión del Hub se registra en el día local del revisor. Un repositorio puede seguir abierto y declarar su línea de distribución obsoleta, como ocurre con `openai/skills`.

## Elegir un perfil

| Perfil | Cuándo usarlo | Ejemplo de decisión |
| --- | --- | --- |
| angular-supabase-cloudflare | Stack de aplicación, datos y alojamiento confirmado | Usa `trabajo-frontend` para interfaz y `cambio-sql` para revisión local de SQL. |
| angular-frontend | Interfaz Angular | `trabajo-frontend` sugiere Modern Web Guidance. El MCP del CLI requiere `inspeccion-cli` y una petición de inclusión. |
| python-ai | Python para modelos, datos o evaluación | Context7 sólo si una duda se puede formular públicamente. |
| generic-web | Plataforma web sin perfil más específico, incluidos React y Next.js | `trabajo-frontend` sugiere Modern Web Guidance. La navegación interactiva se incluye a demanda. |
| business-discovery | Requisitos y reglas antes de fijar el stack | Devuelve skill de dominio y workflow; evita accesos de cuenta. |

## Semántica de selección

1. El operador elige el perfil contrastando `activate_when` y `stack` con hechos del proyecto. El Hub no inspecciona cuentas ni infiere el stack a partir de credenciales.
2. Cada fila expresa una razón y condiciones acumulativas (`when`). Todas deben estar presentes en los `--context` recibidos. Las vacías siempre se cumplen.
3. Las filas esenciales y recomendadas se proponen cuando son aplicables. Las opcionales requieren `--include ID` o una dependencia efectiva; las no aplicables se excluyen incluso ante una petición explícita.
4. Se comprueban agente, stack, conflictos y dependencias transitivas. El resultado ordena las dependencias antes de las capacidades que las consumen y lista por qué se omite el resto. Una opción de recomendación sólo cambia la propuesta.
5. Contrasta la propuesta con el inventario real, permisos y evidencia. Documenta las exclusiones en la [plantilla de propuesta](../templates/propuesta.md).

```console
python scripts/hub.py recommend angular-frontend --agent codex --context inspeccion-cli --include angular-cli-mcp
python scripts/hub.py recommend python-ai --agent antigravity
```

En el primer caso aparece el CLI como opcional seleccionado. El segundo propone el arranque sin incorporar una herramienta Angular ni una consulta pública.

La condición `trabajo-frontend` corresponde a tareas de interfaz, accesibilidad, compatibilidad, rendimiento web o modernización. Una decisión de hosting o una migración SQL por sí sola deja esa condición inactiva. [Modern Web Guidance](modern-web-guidance.md)

Consulta los criterios de accesibilidad, Lighthouse, ASVS, Sentry, Figma y Next.js DevTools antes de activar sus contextos. `nextjs-16-dev` sólo existe en `generic-web` y requiere evidencia de la versión efectiva antes de recomendar el servidor. El Hub toma ese hecho del operador. [Herramientas y condiciones por fase](herramientas-ingenieria.md)

En los tres perfiles web, `prototipado-visual` permite incluir Stitch mediante `--include google-stitch` cuando el operador elige esa herramienta. Si el flujo ya usa Figma, `diseno-figma` permite considerar su ficha. Para SQL o mantenimiento sin cambios de interfaz deja inactivas ambas condiciones. En el perfil full-stack, `angular-skills` y Modern Web Guidance también requieren `trabajo-frontend`. [Criterios de prototipado](prototipado.md)
