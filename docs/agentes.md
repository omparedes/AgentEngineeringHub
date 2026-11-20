# Usar las skills con Codex y Antigravity

El formato común es una carpeta con un `SKILL.md` de nombre y descripción declarados en YAML. El cliente puede descubrir primero esos metadatos, leer el cuerpo cuando se active la skill y consultar recursos auxiliares bajo demanda. El Hub conserva las instrucciones permanentes en el [AGENTS.md raíz](../AGENTS.md). [Especificación Agent Skills](https://agentskills.io/specification)

| Superficie | Alcance de proyecto | Uso |
| --- | --- | --- |
| Codex | Lee `.agents/skills/` desde el directorio actual hacia la raíz del repositorio; acepta instrucciones `AGENTS.md` en el recorrido | En un chat del Hub solicita `$hub-maintainer audita la ficha context7`. Una tarea compatible también puede activar la skill por descripción. |
| Antigravity App y CLI | Descubren las skills de `.agents/skills/` del workspace y sus padres hasta la raíz. Admiten reglas raíz como `AGENTS.md` | Desde el Hub solicita `/hub-maintainer revisa la evidencia de angular-skills`. En CLI usa `/skills reload` o inicia una conversación nueva tras incorporar una skill. |
| Antigravity IDE | Reconoce `.agents/skills/` en el workspace | Inspecciona Customizations en el panel del agente y pide la skill por nombre. Comprueba en tu versión qué reglas se cargaron; si hace falta, indica explícitamente que lea el AGENTS.md raíz. |

Fuentes del comportamiento por cliente. [Codex Skills](https://learn.chatgpt.com/docs/build-skills) · [Codex AGENTS.md](https://developers.openai.com/codex/guides/agents-md/) · [Antigravity Skills](https://antigravity.google/docs/skills) · [Antigravity Rules](https://antigravity.google/docs/rules)

## Incorporar una sola skill a otro proyecto

Este paso **instala por proyecto**. Úsalo únicamente cuando se haya decidido instalar esa skill. Desde la raíz del proyecto **destino**, establece la ruta del checkout revisado del Hub. El ejemplo utiliza Python y la biblioteca estándar en Windows, macOS y Linux.

```console
python -c "import pathlib, shutil, sys; src=pathlib.Path(sys.argv[1])/'skills/domain-discovery'; dst=pathlib.Path('.agents/skills/domain-discovery'); shutil.copytree(src,dst)" "RUTA_AL_HUB"
```

El resultado es `.agents/skills/domain-discovery/SKILL.md` en el destino. Si ya existe el directorio, la copia falla y conserva el contenido previo. Para actualizarlo, compara contra la nueva referencia y revisa el diff del proyecto. Para `hub-maintainer` la ruta fuente comienza en `.agents/skills/`. Para `project-bootstrap`, conserva un checkout del Hub y comunica su ruta para que pueda consultar el catálogo.

**Alcance de usuario.** Codex documenta `~/.agents/skills/` y Antigravity App/CLI documentan `~/.gemini/config/skills/` para skills compartidas entre proyectos. El instalador de sistema de Codex tiene su propio destino. Ninguno de esos directorios se necesita para esta guía. Una distribución mediante plugin puede incluir herramientas adicionales. Revisa su manifiesto antes de elegirla.

## Comprobar el descubrimiento

Abre el destino como workspace, inicia un chat nuevo y pide que enumere el nombre y descripción de la skill instalada. Invócala con uno de los [casos de ejemplo](../examples/escenarios.md) y comprueba la salida indicada. Registra superficie, versión y resultado si haces un ensayo. En esta entrega se validaron los archivos y las convenciones documentadas; la ejecución interactiva de Antigravity queda pendiente.
