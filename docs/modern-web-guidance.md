# Modern Web Guidance

Modern Web Guidance es una capacidad externa de Google Chrome. La skill aporta instrucciones a un agente. El CLI consulta guías y examina patrones heredados de la plataforma web. Los plugins son canales de distribución para determinados clientes. La ficha del Hub es de tipo `skill` y se consulta sin configurar servidores MCP. [Ficha del catálogo](../catalog/modern-web-guidance.yaml) · [Documentación de Chrome](https://developer.chrome.com/docs/modern-web-guidance)

| Área | Preguntas que puede orientar |
| --- | --- |
| HTML y accesibilidad | Semántica, formularios, validación, controles nativos, `dialog`, popovers, foco y teclado. |
| CSS | Container queries, Grid y Subgrid, tamaños fluidos, funciones y espacios de color, transiciones, animaciones y View Transitions. |
| JavaScript y APIs web | Interacciones accesibles, manejo de eventos, APIs de navegador y mejoras progresivas. |
| Rendimiento | LCP, INP y CLS, imágenes responsivas, prioridades y carga de recursos, y reducción de JavaScript cuando el navegador resuelve la necesidad. |
| Compatibilidad | Baseline, soporte de Chrome, Edge, Firefox y Safari, fallbacks y coste de polyfills. |
| Seguridad y privacidad | Prácticas para las APIs web que aborda el catálogo. Valida aparte la política de seguridad del proyecto y utiliza sus herramientas especializadas cuando corresponda. |

## Descubrir y elegir

Desde el Hub, estas consultas funcionan sin red y dejan la instalación como decisión aparte.

```powershell
python scripts/hub.py list --type skill --tech css
python scripts/hub.py show modern-web-guidance
python scripts/hub.py recommend generic-web --agent codex --context trabajo-frontend
python scripts/hub.py recommend angular-frontend --agent antigravity --context trabajo-frontend
```

Activa `trabajo-frontend` cuando el trabajo incluya interfaz, accesibilidad, compatibilidad, rendimiento de interfaz o modernización. También está disponible en `angular-supabase-cloudflare`. Los perfiles de Python/IA y descubrimiento de negocio quedan fuera de esta selección. La capacidad se recomienda por contexto y conserva `depends_on: []`. [Selección de perfiles](catalogo-y-perfiles.md)

## Incorporación por cliente

Comprueba primero el nombre y el origen de la skill en el cliente. Si existe una entrada habilitada, úsala. Revisa el ámbito del proyecto, del usuario y de los plugins antes de copiar archivos o activar otra distribución. Un ámbito de usuario cubre los proyectos locales de la misma cuenta del sistema operativo. El ámbito de proyecto se comparte mediante el checkout cuando se versionan sus archivos.

### Codex Desktop en Windows

1. Abre un chat del proyecto y escribe `$modern-web-guidance` para comprobar si el selector ofrece la skill. El backend de Codex devuelve además la ruta, `scope` y `enabled` mediante `skills/list`. Las skills del usuario se descubren bajo `~/.agents/skills/`; las del proyecto se descubren bajo `.agents/skills/` en el árbol correspondiente. [Skills en Codex](https://learn.chatgpt.com/docs/build-skills)
2. Si falta la skill y se autorizó instalarla, ejecuta desde una terminal interactiva el instalador de Chrome. Para alcance de **proyecto**, abre la terminal en el consumidor, ejecuta el primer comando y confirma **proyecto** en el asistente. Para alcance de **usuario**, usa el segundo comando. `--global` en ese instalador representa el ámbito de la cuenta de usuario. Seleccionar una copia de usuario o de proyecto es suficiente para el mismo cliente. [Instalación oficial](https://developer.chrome.com/docs/modern-web-guidance/get-started) · [Opciones del instalador delegado](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)

   ```powershell
   npx.cmd modern-web-guidance@latest install --agent codex
   npx.cmd modern-web-guidance@latest install --global --agent codex
   ```

3. Inicia un chat nuevo. Selecciona la skill y pide que investigue una tarjeta responsive con consultas de contenedor y contraste Baseline. Comprueba en la traza que ejecutó `search` y `retrieve`, e identifica qué guía consultó. El selector comprueba descubrimiento y la traza acredita uso.
4. Si prefieres el canal de plugins y tu versión de Codex Desktop permite gestionarlos, usa el marketplace oficial. Añadir el marketplace e instalar el plugin cambia la configuración del cliente. Comprueba el alcance que muestre tu versión y verifica el plugin y la skill en Desktop después de ejecutar los comandos de Codex CLI. La ayuda local confirma que existen ambas operaciones. Esta revisión no ejecutó su instalación.

   ```powershell
   codex plugin marketplace add GoogleChrome/modern-web-guidance
   codex plugin add modern-web-guidance@googlechrome
   ```

   [Canal de Codex del proveedor](https://github.com/GoogleChrome/modern-web-guidance#alternative-installation-methods) · [Plugins en Codex](https://learn.chatgpt.com/docs/plugins?surface=app)

### Google Antigravity

- **Aplicación de escritorio.** Chrome indica activar `modern-web-guidance` durante la configuración inicial o desde **Settings → Customizations → Build with Google Plugins**. Revisa el alcance y las capacidades visibles antes de habilitar. En App, el selector admite `/modern-web-guidance` cuando la skill está disponible.
- **Antigravity CLI.** Con `agy` disponible y la instalación autorizada, ejecuta el comando oficial. En una sesión interactiva, reinicia la conversación o ejecuta `/skills reload` si la entrada no aparece. Usa el mismo caso sintético de Codex y observa la consulta y la guía recuperada.
- **Distribución compartida por proyecto.** Los clientes que admiten Agent Skills pueden descubrir una carpeta revisada del proveedor en `.agents/skills/modern-web-guidance/`. Conserva sus recursos relativos y registra la referencia de origen. Separa esta copia de cualquier instalación global o plugin que ya ofrezca el mismo nombre.

```powershell
agy plugin install https://github.com/GoogleChrome/modern-web-guidance
```

La instalación y la invocación en Antigravity quedan pendientes de ensayo. [Instalación de Chrome por superficie](https://developer.chrome.com/docs/modern-web-guidance/get-started) · [Descubrimiento en Antigravity](https://antigravity.google/docs/skills)

### Actualizar y diagnosticar

| Situación | Comprobación |
| --- | --- |
| La skill no aparece | Confirma el workspace, la ruta de usuario o proyecto y si la entrada está habilitada. Reinicia el cliente si el selector conserva un estado anterior. |
| Aparecen dos entradas | Identifica sus rutas y el plugin que pudo aportar una segunda copia. Elige la distribución que deba administrar las actualizaciones antes de retirar nada. |
| PowerShell bloquea `npx.ps1` | Usa `npx.cmd`. Comprueba `node --version` y el paquete ejecutado. Para la versión 1.0.1, el paquete declara Node.js `>=22.0.0`. |
| La consulta falla por red o permisos | Revisa el registro npm accesible y el acceso a su caché. Solicita el permiso de descarga cuando falte el paquete. Una versión exacta ya almacenada se puede invocar con `--offline`. |
| La skill y el CLI muestran versiones distintas | La versión npm y el identificador incorporado en `SKILL.md` pertenecen a artefactos distintos. Compara ambos con las fuentes de la revisión. |
| El paquete se actualiza y la skill queda igual | Para una instalación gestionada por el CLI oficial, Google documenta `npx.cmd modern-web-guidance@latest update`. En terminal interactiva revisa el ámbito que se va a actualizar. Para una copia manual, compara con una referencia pública nueva y sincroniza sólo la copia aprobada. Para un plugin, usa el mecanismo del cliente y comprueba la versión después. |

Para mantener esta ficha, aplica `hub-maintainer` y separa los cambios de la skill, del paquete y de los modos de distribución. Conserva las referencias anteriores y repite una consulta sintética después de revisar un cambio. [Mantenimiento del Hub](mantenimiento.md) · [Actualización oficial](https://github.com/GoogleChrome/modern-web-guidance#updating)

## Consultar y analizar con el CLI

Los comandos de demostración usan la versión comprobada. `npx` puede descargar el paquete público a la caché de npm. Una vez disponible, añade `--offline` a `npx.cmd` para impedir descargas de npm. Ejecuta las consultas desde la raíz del consumidor cuando necesites respetar su configuración de compatibilidad. Fija la carpeta de destino al usar `legacy-scan`.

```powershell
$env:DISABLE_TELEMETRY = '1'
npx.cmd -y modern-web-guidance@1.0.1 search "responsive container queries"
npx.cmd -y modern-web-guidance@1.0.1 retrieve "size-aware-styling"
npx.cmd -y modern-web-guidance@1.0.1 retrieve "animate-to-from-top-layer"
npx.cmd -y modern-web-guidance@1.0.1 legacy-scan ./src/components --json
```

La variable anterior afecta a la terminal actual y a sus procesos hijos. Ejecuta la prueba en una terminal dedicada si prefieres que deje de aplicarse al cerrarla.

| Operación | Alcance y salida |
| --- | --- |
| `search` | Recibe una pregunta breve y genérica en inglés y devuelve candidatos con ID y descripción. |
| `retrieve` | Lee la guía por ID. Las salidas grandes pueden guardarse en un archivo temporal indicado por el CLI. Lee ese archivo completo cuando corresponda. |
| `legacy-scan` | Lee la ruta indicada, incluidos formatos web y manifiestos compatibles. El JSON identifica archivo, línea, regla, guía y criterios `keepWhen` y `dropWhen`. Puede incluir fragmentos del código. La versión examinada aplicó 52 reglas de 38 guías. El escáner cubre un subconjunto del catálogo y carece de modo de reparación automática. |
| `install` y `update` | Operaciones de distribución que pueden escribir skills y metadatos del instalador. Ejecútalas con el alcance autorizado. |

Usa `search` para una necesidad concreta. Reserva el escaneo para una revisión de modernización solicitada y limita la carpeta. Verifica cada hallazgo en contexto, incluidos fallbacks deliberados. Un resultado vacío sólo habla de las reglas ejecutadas. [Workflow de modernización de Chrome](https://developer.chrome.com/docs/modern-web-guidance/modernization-workflow)

### Privacidad y telemetría

El registrador del CLI puede enviar eventos cuando se ejecutan comandos. El proveedor documenta recuentos de instalación, agente detectado, consultas de `search` e IDs de guías recuperadas. El código también registra resultado y duración. `list`, `legacy-scan`, `install`, `update` y `uninstall` registran eventos de operación. Para `legacy-scan`, la llamada de telemetría revisada contiene metadatos del comando. Los fragmentos aparecen en la salida local del escaneo. El proveedor indica que no recopila prompts íntegros.

Usa `DISABLE_TELEMETRY=1` para las consultas del Hub y comparte sólo preguntas genéricas. Mantén secretos, rutas privadas, nombres internos, código y salidas de escaneos privados fuera de las consultas y los registros compartidos. El ajuste desactiva la telemetría de Modern Web Guidance. npm, un instalador delegado o el cliente del agente mantienen su propia configuración de red y privacidad. [Privacidad del proveedor](https://github.com/GoogleChrome/modern-web-guidance/blob/64a6d708f5a43f2cd3fde5d4d7db3905ba1bdf65/README.md#telemetry--privacy) · [Registrador examinado](https://github.com/GoogleChrome/modern-web-guidance-src/blob/920ee542afc8785ddbadd9aee976c2eab9caf25f/src/cli/telemetry/clearcut-logger.ts)

## Baseline y aplicación en ingeniería

Usa el objetivo y los navegadores del consumidor, documentados en su `AGENTS.md` u otra configuración de proyecto. Cuando el proyecto no define un objetivo, Chrome documenta que Modern Web Guidance usa **Baseline Widely available**. El Hub sigue ese valor predeterminado del proveedor. Para requisitos más estrictos, verifica soporte por navegador y versión, incluidos WebViews si corresponden. Valora una base funcional, mejoras progresivas, detección de soporte y el coste de cargar y mantener un polyfill. Prueba el fallback con los navegadores objetivo. [Política Baseline de Chrome](https://developer.chrome.com/docs/modern-web-guidance/get-started#baseline)

| Función | Herramienta y evidencia |
| --- | --- |
| Orientación | Modern Web Guidance aporta guías, soporte y candidatos a cambios. |
| Documentación de framework | Skills oficiales y documentación versionada de Angular, React o Next.js. Context7 puede ayudar a encontrar referencias cuando su uso esté autorizado. |
| Implementación | Codex o Antigravity adaptan la propuesta al framework y al alcance aprobado. |
| Verificación | Chrome DevTools aporta trazas y métricas observadas. Playwright verifica recorridos y regresiones. Sus MCP, cuando se autoricen, son canales independientes. Lint, análisis estático y build cubren sus propias reglas. |

Para una interfaz existente, aplica [cambio controlado](../workflows/cambio-controlado.md#modernización-frontend) y conserva la decisión en el análisis de impacto. [Ejemplo React y Next.js](../examples/escenarios.md#frontend-react-y-nextjs)

## Revisión del 22 de noviembre de 2026

| Artefacto | Referencia o resultado |
| --- | --- |
| Distribución de la skill | Commit `64a6d708f5a43f2cd3fde5d4d7db3905ba1bdf65` del 16 de noviembre de 2026 UTC. El commit coincide con la revisión anterior. `SKILL.md` declara el identificador `2026_11_10-47b4c80e` en el comando de búsqueda. [Árbol distribuido](https://github.com/GoogleChrome/modern-web-guidance/tree/64a6d708f5a43f2cd3fde5d4d7db3905ba1bdf65) |
| Código fuente y mantenimiento | Commit fuente examinado `920ee542afc8785ddbadd9aee976c2eab9caf25f` del 22 de noviembre de 2026 UTC. Ambos repositorios estaban activos y sin archivar. El proyecto recibe incidencias y aportes en el repositorio fuente. [Código fuente](https://github.com/GoogleChrome/modern-web-guidance-src/tree/920ee542afc8785ddbadd9aee976c2eab9caf25f) |
| CLI | La etiqueta npm `latest` resolvió `1.0.1`, publicada el 16 de noviembre de 2026 UTC. Se ejecutó con Node 24.19.0 en Windows. [Metadatos del paquete](https://registry.npmjs.org/modern-web-guidance/1.0.1) |
| Consulta, escaneo y caché | `search` devolvió `size-aware-styling` entre sus candidatos. Se recuperaron esa guía y `animate-to-from-top-layer`. El escaneo devolvió JSON, detectó una regla de autorredimensionamiento de formulario en un JS sintético y conservó el hash del archivo. Se repitieron las operaciones desde la caché de npm con `--offline` y telemetría desactivada. |
| Codex Desktop | `skills/list` del backend 0.171.0-alpha.13 devolvió una copia de usuario habilitada desde el Hub y desde una carpeta externa. El ensayo del CLI se ejecutó por separado. Quedan por ensayar la invocación en una conversación de Desktop y el canal de plugins. |
| Antigravity | Documentación oficial cotejada. Instalación e invocación sin probar. |

### Licencias y atribución

Google Chrome, Microsoft Edge, Mozilla Firefox, MDN y la comunidad web mantienen el proyecto según el README oficial. El código se distribuye bajo **Apache-2.0** y la documentación en `guides/` bajo **CC-BY-4.0**, salvo avisos específicos. El Hub enlaza a los originales y mantiene su propia licencia para esta integración documental. [Licencias y atribuciones de Modern Web Guidance](https://github.com/GoogleChrome/modern-web-guidance/blob/64a6d708f5a43f2cd3fde5d4d7db3905ba1bdf65/README.md#license)
