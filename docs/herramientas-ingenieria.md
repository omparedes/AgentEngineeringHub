# Herramientas de ingeniería por fase

El catálogo permite consultar y proponer estas capacidades con el entorno local del Hub. Elegir una capacidad deja la instalación, la ejecución y el acceso a datos sujetos al alcance del proyecto. Esta guía recoge los criterios de la ampliación del 23 de noviembre de 2026.

## Del análisis a la operación

| Fase | Qué aporta valor | Cuándo basta lo que ya tienes |
| --- | --- | --- |
| Investigación y análisis | `domain-discovery` para reglas y requisitos. Context7 para una duda pública de una biblioteca concreta. | Los requisitos ya tienen fuente y la documentación de la versión instalada resuelve la pregunta. |
| Arquitectura y diseño | ASVS para convertir riesgos en criterios. Figma MCP para recuperar componentes y variables de un diseño autorizado. | El alcance está respaldado por un checklist trazable y las especificaciones de diseño ya están disponibles localmente. |
| Implementación | Skills del framework y Modern Web Guidance orientan decisiones. Next.js DevTools MCP aporta rutas, logs y errores del servidor local compatible. | El manifiesto, la documentación y la terminal del proyecto aportan evidencia suficiente. |
| Testing funcional y E2E | Playwright Test conserva pruebas repetibles. Playwright MCP explora un recorrido para reproducir un fallo. | La suite existente ya reproduce y verifica el comportamiento. |
| Accesibilidad | axe-core + Playwright aporta regresiones sobre estados concretos. Completar con revisión humana de teclado, foco, lector de pantalla y criterios que requieren juicio. | Una inspección puntual puede empezar con la revisión manual ya disponible. |
| Rendimiento | Chrome DevTools aporta una traza diagnóstica. Lighthouse CI aplica presupuestos a páginas reproducibles. | Para una duda puntual basta una traza local. Para experiencia real hacen falta métricas de campo. |
| Seguridad | ASVS ayuda a definir qué comprobar en autenticación, autorización, validación y APIs. | Un checklist propio sirve cuando ya traza el alcance y las evidencias al estándar o al requisito aplicable. |
| Despliegue | `cambio-controlado` registra pruebas, reversión y aprobación. GitHub MCP puede aportar el estado de checks y Cloudflare MCP documentación de Pages o Workers. | El historial local, los checks existentes y la configuración versionada bastan para preparar el cambio. |
| Observabilidad y mantenimiento | Sentry MCP aporta incidencias y trazas cuando Sentry está en el alcance. Supabase MCP contrasta esquemas en desarrollo cuando las migraciones resultan insuficientes. | Logs saneados, dashboard autorizado o fixtures locales cubren una inspección puntual. |

## Selección contextual

Los contextos representan hechos que confirma el operador. En `generic-web`, `nextjs-16-dev` exige verificar la versión efectiva con el lockfile o paquete instalado y justificar el uso de `next dev` local. La CLI registra esa declaración como condición y carece de introspección del consumidor. Las dos variantes de Angular excluyen Next.js DevTools mediante la ausencia de la condición y de la opción en sus perfiles.

| Contexto | Capacidad propuesta | Perfiles |
| --- | --- | --- |
| `nextjs-16-dev` | `next-devtools-mcp` | `generic-web` |
| `auditoria-accesibilidad` | `axe-core-playwright` | Tres perfiles web |
| `presupuesto-lighthouse` | `lighthouse-ci` | Tres perfiles web |
| `seguridad-aplicacion` | `owasp-asvs` | `angular-supabase-cloudflare`, `generic-web` |
| `sentry-en-alcance` | `sentry-mcp` | `angular-supabase-cloudflare`, `generic-web`, `python-ai` |
| `diseno-figma` | `figma-mcp` | Tres perfiles web |
| `prueba-navegacion` y `--include playwright-mcp` | `playwright-mcp` | Tres perfiles web |

`business-discovery` conserva su alcance de análisis previo al stack. Sigue siendo posible consultar Filesystem MCP por ID si hay una carencia específica de acceso nativo. [Perfiles del Hub](catalogo-y-perfiles.md)

```console
python scripts/hub.py recommend generic-web --context nextjs-16-dev
python scripts/hub.py recommend angular-supabase-cloudflare --context auditoria-accesibilidad --context presupuesto-lighthouse --context seguridad-aplicacion
python scripts/hub.py recommend angular-frontend --context diseno-figma --context prueba-navegacion --include playwright-mcp
python scripts/hub.py recommend python-ai --context sentry-en-alcance
```

Cada comando añade las capacidades de su contexto a la propuesta. El último exige Sentry confirmado o adoptado, además de una necesidad de diagnóstico. Con `recommend python-ai` se conserva la selección base.

## Capacidades incorporadas

- **Next.js DevTools MCP.** El adaptador `next-devtools-mcp` descubre el endpoint `/_next/mcp` que expone el servidor de desarrollo desde Next.js 16. Para diagnosticar un problema concreto, limita la tarea a la instancia local del consumidor y usa datos sintéticos. La documentación y los logs locales suelen bastar para una consulta de API o compilación aislada. [Ficha](../catalog/next-devtools-mcp.yaml) · [Guía de Next.js](https://nextjs.org/docs/app/guides/mcp)
- **axe-core + Playwright.** En una suite Playwright Test, prepara el estado de interfaz, aplica `AxeBuilder` a `page`, limita tags o selectores si el caso lo exige y comprueba la lista de violaciones. Conserva fuera del repositorio los reportes con contenido privado. Una ejecución sin violaciones sólo acredita las reglas automáticas que se aplicaron al estado probado. [Ficha](../catalog/axe-core-playwright.yaml) · [Accesibilidad con Playwright](https://playwright.dev/docs/accessibility-testing)
- **Lighthouse CI.** En un consumidor con el paquete ya disponible, `lhci collect` ejecuta auditorías sobre URLs reproducibles y `lhci assert` aplica los umbrales acordados en la configuración. En GitHub Actions, un flujo autorizado puede ejecutar esos pasos después del build en un runner con Chrome. Conserva informes en el ámbito privado aprobado. `temporary-public-storage` da acceso mediante enlace público. [Ficha](../catalog/lighthouse-ci.yaml) · [Configuración de Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci/blob/main/docs/configuration.md)
- **OWASP ASVS.** La edición estable examinada es **5.0.0**. Acordar el nivel L1, L2 o L3 en función del riesgo y los datos. En una matriz, anotar el ID con prefijo `v5.0.0-`, el control, la prueba y la evidencia o justificación de exclusión. Es una referencia para verificar aplicaciones y APIs web, especialmente cuando manejan activos sensibles. [Ficha](../catalog/owasp-asvs.yaml) · [Edición estable](https://asvs.owasp.org/downloads/)
- **Sentry MCP.** El servicio alojado usa OAuth y permite limitar el endpoint a organización y proyecto. El CLI oficial permite `sentry mcp` por stdio con su sesión autorizada y selección de skills. Para Sentry autogestionado se documenta el host en el CLI. Revisa las herramientas efectivas para evitar gestionar incidencias, configuración o datos cuando sólo necesitas inspección. [Ficha](../catalog/sentry-mcp.yaml) · [Servicio alojado](https://mcp.sentry.dev/) · [Comando Sentry CLI](https://cli.sentry.dev/commands/mcp/)
- **Filesystem MCP.** El servidor ofrece lectura, búsqueda y metadatos. Los modos de escritura pueden crear, editar y mover archivos. En stdio, pasa sólo un directorio necesario y usa `--read-only`. En la revisión examinada, `--confine-roots` acota los Roots del cliente a su intersección con los directorios permitidos en la era de protocolo que admite Roots. Comprueba el alcance efectivo y mantén los permisos del sistema operativo. El acceso nativo del agente tiene prioridad cuando cubre el workspace. [Ficha](../catalog/filesystem-mcp.yaml) · [Servidor de referencia](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)
- **Figma MCP.** El servidor remoto usa una cuenta autorizada y acceso al archivo. Codex puede usar el plugin oficial o configurar el transporte remoto. La alternativa de Figma Desktop usa `http://127.0.0.1:3845/mcp` y depende del asiento, el plan y la aplicación abierta. El flujo de lectura parte de un frame, variables y componentes autorizados y los relaciona con el código. Las escrituras al canvas requieren autorización propia. [Ficha](../catalog/figma-mcp.yaml) · [Figma en Codex](https://help.figma.com/hc/en-us/articles/39888629089175-Codex-and-Figma-Set-up-the-MCP-server)

## Capacidades revisadas y relaciones

- **Chrome DevTools for Agents** conserva su ID `chrome-devtools` y su selección principal MCP. El CLI de DevTools y `chrome-devtools-cli` son vías alternativas del mismo producto para consultar consola, red y rendimiento. La skill orienta al agente para usar el CLI. Compartir la ficha registra el acceso al mismo navegador y evita sugerir dos integraciones para un diagnóstico. Una futura ficha tendría sentido si hubiera que seleccionarlas de manera independiente en un perfil. [Ficha](../catalog/chrome-devtools.yaml) · [CLI del proveedor](https://developer.chrome.com/docs/devtools/agents/cli)
- **Playwright MCP** sigue siendo exploración interactiva. Las regresiones viven en Playwright Test. `axe-core-playwright` requiere el runner y un navegador del consumidor y puede ejecutarse con el MCP ausente. [Ficha](../catalog/playwright-mcp.yaml) · [Playwright MCP](https://github.com/microsoft/playwright-mcp)
- **Context7** aporta consultas versionadas de bibliotecas. Modern Web Guidance orienta sobre la plataforma web. Usa la documentación de origen si ya resuelve la duda y sanea las preguntas antes de enviarlas a Context7. [Ficha](../catalog/context7.yaml) · [Configuración de Context7 para Codex](https://github.com/upstash/context7/blob/master/docs/clients/codex.mdx)
- **GitHub MCP** conserva el enfoque de mínima lectura. Seleccionar `/mcp/readonly` o su equivalente y toolsets reducidos limita las operaciones disponibles. El acceso a repositorios depende también de la credencial. [Ficha](../catalog/github-mcp.yaml) · [Servidor alojado](https://github.com/github/github-mcp-server/blob/main/docs/remote-server.md)
- **Supabase MCP** separa el servidor alojado del entorno local. En alojamiento se puede reducir el ámbito con `project_ref`, `read_only=true` y `features`. Las migraciones y fixtures suelen bastar para preparar una modificación. [Ficha](../catalog/supabase-mcp.yaml) · [Guía de Supabase](https://supabase.com/docs/guides/ai-tools/mcp)
- **Cloudflare MCP** conserva el servidor documental como primera opción. La API de cuenta tiene su propio endpoint, permisos y alcance. Una consulta sobre límites o referencias no necesita acceso administrativo a la cuenta. [Ficha](../catalog/cloudflare-mcp.yaml) · [Servidores de Cloudflare](https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/)

Las relaciones anteriores son alternativas o complementos. `depends_on` sigue vacío para estas incorporaciones porque sus requisitos técnicos se satisfacen en el consumidor. Tampoco hay conflictos inherentes. Dos herramientas pueden quedar disponibles cuando verifican aspectos distintos de la tarea.

## Evidencia y límites de la revisión

Las fichas guardan fecha, referencia Git, documentación, licencia cuando se comprobó y resultados pendientes. Se consultaron fuentes públicas y metadatos de npm para requisitos versionados. Ningún servidor se conectó durante la revisión. La autenticación, el alcance efectivo, el comportamiento de las herramientas y la compatibilidad en Codex y Antigravity necesitan verificaciones por cliente. La licencia de implementación del servidor Figma queda sin confirmar. Antes de habilitar cualquier capacidad remota, valida su acceso y herramientas en un proyecto desechable y conserva los datos en los ámbitos autorizados.
