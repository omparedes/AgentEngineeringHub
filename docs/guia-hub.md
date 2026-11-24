# Empieza con Agent Engineering Hub

## Primera vez

Abre un chat de **Codex Desktop** o una conversación en **Antigravity App**. Pega este mensaje:

```text
Usa https://github.com/omparedes/AgentEngineeringHub para preparar mi equipo. Revisa qué herramientas y permisos ya tengo. Propón el mínimo para empezar con la última versión estable y espera mi autorización antes de copiar o instalar.
```

El agente puede usar la URL para identificar la publicación estable y proponer un destino local. La opción reutilizable instala una sola skill de usuario y guarda la ubicación del checkout en su propia carpeta. Una vez disponible, inicia las conversaciones nuevas con las instrucciones siguientes. [Publicaciones y etiquetas del Hub](https://github.com/omparedes/AgentEngineeringHub/releases)

**Estado de esta propuesta.** `hub-guide` está en desarrollo para una versión posterior a v0.2.0. La edición estable actual, `v0.1.0`, ofrece [sus procedimientos de agentes](https://github.com/omparedes/AgentEngineeringHub/blob/v0.1.0/docs/agentes.md). Úsala mientras llega una edición aprobada que incluya `hub-guide`.

## Para trabajar

| Quiero | Mensaje que puedes pegar |
| --- | --- |
| Iniciar un proyecto | «Usa Agent Engineering Hub. Quiero iniciar este proyecto. Lee lo que ya existe, pregúntame sólo lo que falte y propón el primer resultado y las herramientas mínimas». |
| Continuar o revisar un proyecto | «Usa Agent Engineering Hub. Quiero retomar este proyecto para [objetivo]. Revisa las decisiones y herramientas existentes. Dime qué puedo reutilizar, qué falta y qué harías primero». |

**Codex Desktop.** Abre la carpeta del proyecto y empieza un chat. Para invocar la skill de forma explícita, escribe `$` y selecciona `hub-guide` antes de pegar el mensaje.

**Antigravity App.** En **Projects**, elige un proyecto existente o crea uno con **New Project → Add Folder**. Abre la conversación desde ese Project y elige **Local** si se muestra el selector. Escribe `/hub-guide` y selecciónala antes de pegar el mensaje. Si App limita el acceso al checkout del Hub, puedes incluir ese checkout como segunda carpeta del Project y mantener sus permisos habituales. [Proyectos de Antigravity](https://antigravity.google/docs/projects) · [Skills de Antigravity](https://antigravity.google/docs/skills)

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

Si autorizas la copia, repite **sólo el comando elegido** con `--apply SHA_MOSTRADO` y reemplaza `SHA_MOSTRADO` por el commit de la previsualización. El script comprueba que la revisión sigue siendo la misma, crea el destino si está libre y copia `SKILL.md` y `hub-source.json`. El último archivo conserva la referencia y la ruta del Hub en el equipo para consultas futuras. Abre una conversación nueva y comprueba `$hub-guide` o `/hub-guide`. [Destinos oficiales de Codex](https://learn.chatgpt.com/docs/build-skills) · [Destinos oficiales de Antigravity App](https://antigravity.google/docs/skills)

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
