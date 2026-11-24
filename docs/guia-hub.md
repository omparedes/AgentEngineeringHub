# Empieza con Agent Engineering Hub

## Primera vez

Abre un chat de **Codex Desktop** o una conversación en **Antigravity App**. Pega este mensaje:

```text
Usa https://github.com/omparedes/AgentEngineeringHub para preparar mi equipo. Quiero empezar con la última versión estable. Revisa qué herramientas y permisos ya tengo, muéstrame tu informe y espera mi selección.
```

El agente puede usar la URL para identificar la publicación estable y proponer un destino local. La opción reutilizable instala una sola skill de usuario y guarda la ubicación del checkout en su propia carpeta. Una vez disponible, inicia las conversaciones nuevas con las instrucciones siguientes. [Publicaciones y etiquetas del Hub](https://github.com/omparedes/AgentEngineeringHub/releases)

`hub-guide` forma parte del alcance de v0.2.0. Mientras la etiqueta estable aún esté pendiente, `v0.1.0` ofrece [sus procedimientos de agentes](https://github.com/omparedes/AgentEngineeringHub/blob/v0.1.0/docs/agentes.md). Consulta el [estado de publicación](informe-0.2.0.md) antes de elegir la referencia.

## Para trabajar

| Quiero | Mensaje que puedes pegar |
| --- | --- |
| Iniciar un proyecto | «Usa Agent Engineering Hub. Quiero iniciar este proyecto. Lee lo que ya existe, pregúntame sólo lo que falte y muéstrame el informe de herramientas». |
| Continuar o revisar un proyecto | «Revisa las herramientas de este proyecto. Quiero retomar el trabajo para [objetivo]. Conserva mis decisiones anteriores y dime qué puedo reutilizar y qué falta». |

**Codex Desktop.** Abre la carpeta del proyecto y empieza un chat. Para invocar la skill de forma explícita, escribe `$` y selecciona `hub-guide` antes de pegar el mensaje.

**Antigravity App.** En **Projects**, elige un proyecto existente o crea uno con **New Project → Add Folder**. Abre la conversación desde ese Project y elige **Local** si se muestra el selector. Escribe `/hub-guide` y selecciónala antes de pegar el mensaje. Si App limita el acceso al checkout del Hub, puedes incluir ese checkout como segunda carpeta del Project y mantener sus permisos habituales. [Proyectos de Antigravity](https://antigravity.google/docs/projects) · [Skills de Antigravity](https://antigravity.google/docs/skills)

### Cómo se eligen las herramientas

1. Explica el proyecto y qué quieres lograr ahora. El agente pregunta sólo por lo que no pueda deducir y cambie el plan.
2. El Hub identifica las capacidades pertinentes para la fase actual. En descubrimiento, el stack puede seguir abierto.
3. El agente revisa qué está disponible en tu entorno y qué puede comprobar con los permisos actuales.
4. Recibes el [Informe de Herramientas Recomendadas y Estado del Entorno](../templates/informe-herramientas.md). Incluye finalidad, prioridad, estado, acción, permisos y recomendación por herramienta.
5. Responde por nombre. Por ejemplo, «**UTILIZAR** GitHub MCP, **POSPONER** Figma MCP, **OMITIR** Playwright MCP». También puedes pedir una alternativa o cambiar de opinión después.
6. El agente reutiliza lo operativo dentro del alcance aceptado. Si hay que instalar, configurar o activar algo, te muestra los cambios y solicita autorización específica antes de ejecutarlos. Luego verifica el resultado y te informa de fallos o comprobaciones pendientes.
7. Con tu autorización, guarda las decisiones en el proyecto. En futuras conversaciones puede retomarlas y comprobar qué funciona en el equipo que estás usando.

## Preparación y mantenimiento técnico

### Obtener una copia revisada

En la [página de publicaciones](https://github.com/omparedes/AgentEngineeringHub/releases) elige la última edición estable aprobada que incluya la skill. Confirma la etiqueta y el commit con el mantenedor si hay ambigüedad. Desde una carpeta de trabajo, reemplaza `ETIQUETA_ESTABLE` por la referencia elegida:

```console
git clone --branch ETIQUETA_ESTABLE --single-branch https://github.com/omparedes/AgentEngineeringHub.git
cd AgentEngineeringHub
git rev-parse HEAD
```

La copia queda en `AgentEngineeringHub`. Si falta Git, descarga y extrae el ZIP oficial de la etiqueta. Si falta Python, puedes leer las fichas YAML y ejecutar la copia manual indicada abajo. Para usar la CLI del catálogo, prepara Python 3.11+ y sus dependencias en el [entorno del Hub](inicio-rapido.md).

### Previsualizar e instalar para el usuario

Desde el checkout revisado, con Git y Python 3.11+, elige sólo el cliente que vayas a usar.

```console
python scripts/install_hub_guide.py --client codex
python scripts/install_hub_guide.py --client antigravity
```

Por defecto muestra versión, commit, destino y hash de la skill. Trabaja sin red y lee el archivo de `HEAD` confirmado. Exige una etiqueta estable que apunte exactamente a `HEAD`. La revisión de la fuente oficial y de su aprobación corresponde al paso previo. Para ensayar una rama local, se puede añadir `--allow-unreleased` a la previsualización. Esa variante es para un checkout de prueba.

Después de revisar el informe, elegir utilizar la skill y autorizar su copia, repite **sólo el comando elegido** con `--apply SHA_MOSTRADO`. Usa el commit de la previsualización. El script comprueba la revisión, crea el destino si está libre y copia `SKILL.md` y `hub-source.json`. El segundo archivo conserva la referencia y ubicación local del Hub en ese equipo. Abre una conversación nueva y comprueba `$hub-guide` o `/hub-guide`. [Destinos oficiales de Codex](https://learn.chatgpt.com/docs/build-skills) · [Destinos oficiales de Antigravity App](https://antigravity.google/docs/skills)

| Alcance | Destino |
| --- | --- |
| Usuario Codex | `~/.agents/skills/hub-guide/` |
| Usuario Antigravity App | `~/.gemini/config/skills/hub-guide/` |
| Un proyecto en cualquiera de los dos | `.agents/skills/hub-guide/` desde la raíz del proyecto |

### Copia manual, actualización o retiro

- **Copia manual.** Abre la carpeta `skills/hub-guide/` de un checkout o ZIP revisado y comprueba que tenga `SKILL.md`. Revisa la carpeta de descubrimiento del cliente antes de copiar. Copia la carpeta al destino elegido si no existe allí y deja la ruta del Hub en la conversación o en las instrucciones locales del proyecto. Este procedimiento también permite una copia por proyecto.
- **Actualización.** Inspecciona la carpeta instalada y cualquier modificación local. Conserva la copia anterior moviéndola fuera de las carpetas de descubrimiento. Selecciona el nuevo checkout aprobado, previsualiza y copia. Abre un chat nuevo para confirmar la entrada y el catálogo. Si necesitas revertir, retira la nueva copia y restaura la anterior.
- **Retiro.** Mueve o elimina sólo `hub-guide/` del alcance donde la instalaste, después de revisar su contenido. Comprueba que ya no aparezca al abrir una conversación nueva. El checkout puede seguir disponible para otras consultas.

El procedimiento toca sólo esta skill. Consulta las [guías avanzadas](agentes.md) para incorporar capacidades a un proyecto y la [matriz de ensayo](testing/hub-guide.md) para comprobar el recorrido completo.

### Cómo se guardan las decisiones del proyecto

La ruta convencional es `.agents/hub-tools.yaml` dentro del consumidor. Si ya está ocupada por otro formato, el agente propone otra ubicación. El [ejemplo YAML](../templates/herramientas-proyecto.yaml) registra perfil, stack, referencia y fecha del catálogo, decisión por herramienta, alcance, ubicación lógica y motivo opcional. Las ubicaciones son categorías como `mcp-del-proyecto` o `skills-del-usuario`. El [contrato](../schemas/project-tools.schema.json) admite una última observación opcional con fecha, cliente y estado de verificación. Esa observación es histórica y la reutilización requiere evidencia actual. Conserva sólo motivos saneados y deja fuera secretos, identificadores privados, rutas personales y autorizaciones de ejecución.

La revisión técnica se apoya en selectores, inventarios del cliente y comprobaciones locales permitidas. Un MCP registrado puede seguir **configurado pero no verificado**, y una lectura bloqueada se registra como **estado desconocido**. La auditoría se limita a los metadatos disponibles y evita iniciar conexiones para completar el informe. [MCP en Codex](https://learn.chatgpt.com/docs/extend/mcp?surface=cli) · [MCP en Antigravity](https://antigravity.google/docs/mcp)
