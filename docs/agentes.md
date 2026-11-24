# Usar las skills con Codex y Antigravity

El formato común es una carpeta con un `SKILL.md` de nombre y descripción declarados en YAML. El cliente puede descubrir primero esos metadatos, leer el cuerpo cuando se active la skill y consultar recursos auxiliares bajo demanda. El Hub conserva las instrucciones permanentes en el [AGENTS.md raíz](../AGENTS.md). [Especificación Agent Skills](https://agentskills.io/specification)

| Superficie | Alcance de proyecto | Uso |
| --- | --- | --- |
| Codex | Lee `.agents/skills/` desde el directorio actual hacia la raíz del repositorio; acepta instrucciones `AGENTS.md` en el recorrido | En un chat del Hub solicita `$hub-maintainer audita la ficha context7`. Una tarea compatible también puede activar la skill por descripción. |
| Antigravity App | Descubre `.agents/skills/` en las carpetas del Project. | En **Projects**, crea un proyecto con **Add Folder** y selecciona el checkout local del Hub. Abre una conversación en ese proyecto y selecciona `/hub-maintainer` en el campo de mensaje. |
| Antigravity CLI | Descubre `.agents/skills/` desde el directorio de trabajo. | En la TUI ejecuta `/hub-maintainer revisa la evidencia de angular-skills`. Usa `/skills reload` o inicia una conversación nueva tras copiar una skill. |
| Antigravity IDE | Reconoce `.agents/skills/` en el workspace | Inspecciona Customizations en el panel del agente y pide la skill por nombre. Comprueba en tu versión qué reglas se cargaron; si hace falta, indica explícitamente que lea el AGENTS.md raíz. |

En Antigravity App, usa la conversación del Project para tener acceso a sus carpetas. Si aparece el selector de entorno, elige **Local** para usar los archivos ya preparados. Revisa **Customizations** si necesitas comprobar el ámbito y usa el selector `/` en la conversación para confirmar disponibilidad. **Open IDE** abre una superficie separada. [Proyectos de Antigravity](https://antigravity.google/docs/projects) · [Inicio de Antigravity App](https://antigravity.google/docs/getting-started)

Fuentes del comportamiento por cliente. [Codex Skills](https://learn.chatgpt.com/docs/build-skills) · [Codex AGENTS.md](https://developers.openai.com/codex/guides/agents-md/) · [Antigravity Skills](https://antigravity.google/docs/skills) · [Antigravity Rules](https://antigravity.google/docs/rules)

## Incorporar una sola skill a otro proyecto

Este paso **instala por proyecto**. Úsalo únicamente cuando se haya decidido instalar esa skill. Desde la raíz del proyecto **destino**, establece la ruta del checkout revisado del Hub. El ejemplo utiliza Python y la biblioteca estándar en Windows, macOS y Linux.

```console
python -c "import pathlib, shutil, sys; src=pathlib.Path(sys.argv[1])/'skills/domain-discovery'; dst=pathlib.Path('.agents/skills/domain-discovery'); shutil.copytree(src,dst)" "RUTA_AL_HUB"
```

El resultado es `.agents/skills/domain-discovery/SKILL.md` en el destino. Si ya existe el directorio, la copia falla y conserva el contenido previo. Para actualizarlo, compara contra la nueva referencia y revisa el diff del proyecto. Para copiar `hub-maintainer`, cambia la ruta fuente a `.agents/skills/hub-maintainer` y usa el mismo ID en el destino.

### Comenzar únicamente con project-bootstrap

Desde la raíz del consumidor, copia sólo `project-bootstrap` desde un checkout revisado:

```console
python -c "import pathlib, shutil, sys; hub=pathlib.Path(sys.argv[1]); shutil.copytree(hub/'skills/project-bootstrap', pathlib.Path('.agents/skills/project-bootstrap'))" "RUTA_AL_HUB"
```

Abre un chat nuevo y selecciona `project-bootstrap`. Indícale qué deseas preparar, las restricciones y la ruta del Hub. La ruta puede ser relativa al consumidor. La skill obtiene el inventario del consumidor y consulta los perfiles en ese checkout. Si Python o sus dependencias faltan, puede leer los YAML directamente. Sin el checkout, puede inventariar el proyecto e indicar qué recomendaciones quedan pendientes. `hub-maintainer` también necesita acceso de lectura al checkout que va a auditar.

`skills/` guarda la distribución canónica y `.agents/skills/` es el destino que descubre el cliente. Copia siempre la carpeta completa para incluir posibles recursos relativos. Conserva la referencia Git utilizada para poder revisar copias desactualizadas. Evita dos copias activas con el mismo nombre en ámbitos de usuario o proyecto.

**Alcance de usuario.** Codex documenta `~/.agents/skills/` y Antigravity App/CLI documentan `~/.gemini/config/skills/` para skills compartidas entre proyectos. El instalador de sistema de Codex tiene su propio destino. Ninguno de esos directorios se necesita para esta guía. Una distribución mediante plugin puede incluir herramientas adicionales. Revisa su manifiesto antes de elegirla.

## Comprobar el descubrimiento

Abre el destino como workspace e inicia un chat nuevo. Comprueba el nombre y la descripción en el selector del cliente, y verifica el origen del proyecto cuando el cliente lo muestre. Repite los casos positivos y negativos del [protocolo de aceptación](aceptacion-consumidores.md) y registra superficie, versión y resultado.
