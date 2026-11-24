# Ensayar hub-guide

Esta matriz sirve para ensayar `hub-guide` en la versión consolidada. La [prueba rápida](validacion-manual-agentes-v0.2.0.md) cubre las cuatro skills anteriores. El [informe de v0.2.0](../informe-0.2.0.md) distingue los escenarios aprobados por el responsable de las regresiones aún pendientes.

## Preparación

Usa la rama local revisada de la propuesta. Crea un proyecto temporal con una carpeta de skill que contenga una copia de `skills/hub-guide/SKILL.md` en `.agents/skills/hub-guide/SKILL.md`. Crea dos archivos sintéticos:

```json
{"private":true,"dependencies":{"react":"19.0.0"},"devDependencies":{"@playwright/test":"1.60.0"}}
```

Guarda este manifiesto como `package.json`. Declara Playwright Test sin instalar paquetes. Guarda en `proyecto.md`: «Agenda web para usuarios de un centro ficticio. React está elegido. Tenemos un plan de pruebas con Playwright Test. El próximo incremento es un formulario accesible en la web existente. Queda por decidir el mensaje tras el envío. Usa datos sintéticos».

Abre esa carpeta en Codex Desktop. En Antigravity App, crea un Project con **Add Folder**, elige la carpeta y abre la conversación dentro del Project. Para los dos turnos que usan catálogo, ten disponible el checkout revisado según los permisos normales de cada cliente. Puedes añadirlo como segunda carpeta de ese Project en Antigravity App. Selecciona `$hub-guide` en Codex o `/hub-guide` en App. Guarda la señal del origen local.

## Tres turnos

| Operación | Prompt para pegar en un chat nuevo | Qué debe observarse |
| --- | --- | --- |
| Preparar | Usa Agent Engineering Hub para diagnosticar este equipo. Propón cómo empezar desde la URL oficial si falta el catálogo. Explica qué harías si no encuentro Git o Python. Quiero una previsualización sin tocar archivos. | Identifica cliente y límites, referencia estable o ausencia de ella, y alternativa manual. Distingue el diagnóstico de un cambio autorizado. En un consumidor sin adjuntar el checkout, sólo inventaría el entorno y deja la recomendación de catálogo pendiente si no está accesible. |
| Iniciar | Usa Agent Engineering Hub. Estamos creando un sitio pequeño para informar horarios de una biblioteca ficticia. Propón el primer incremento y las herramientas mínimas con el catálogo local. Puedes preguntarme por las decisiones pendientes. No instales nada. | Hace pocas preguntas y propone una entrega pequeña con guía web si corresponde. Su propuesta evita Angular MCP, integración remota y prototipado extenso sin evidencia que los justifique. |
| Continuar | Usa Agent Engineering Hub. Retoma el formulario descrito en proyecto.md con los medios existentes. Indica qué puedes reutilizar y qué falta. No cambies archivos ni consultes la web. | Lee el manifiesto, reconoce Playwright Test como dependencia declarada y propone reutilizarlo para verificar el formulario. Sólo lo llama instalado si comprueba su disponibilidad. Descarta herramientas incompatibles, evita una segunda entrevista y usa el catálogo local. |

Para el control de herramienta realmente instalada, repite el último turno en un consumidor aislado donde ya tengas disponible un Playwright Test aprobado por ti, o con una skill local cuyo selector confirme disponibilidad. Registra la prueba de presencia. El manifiesto solo acredita una declaración.

Conserva SHA, superficie, versión, modelo, skill seleccionada, archivos consultados y salida saneada. Registra por separado una autorización solicitada, un intento de escritura y cualquier lectura bloqueada. Comprueba el contenido del consumidor antes y después.

## Informe y decisiones de herramientas

Usa otro consumidor desechable con la misma copia de `hub-guide`. Copia el [manifiesto sintético](../../templates/herramientas-proyecto.yaml) como `.agents/hub-tools.yaml`. Crea `proyecto.md` con estos datos:

> Faro administra anticipos en una asociación ficticia. Finanzas revisa las solicitudes de Operaciones. El sistema usa Angular, Supabase y Cloudflare Pages. La fase anterior sólo revisaba una RPC local. Ahora se quiere cambiar el formulario Angular y contrastarlo con un boceto en Figma. El stack ya está decidido. Los datos, equipos y verificaciones de integraciones en este caso son sintéticos.

En una conversación nueva del consumidor, selecciona la skill y pega este mensaje:

```text
Revisa las herramientas de este proyecto. Lee proyecto.md y .agents/hub-tools.yaml y usa el catálogo local. Para este ejercicio, toma estas observaciones simuladas del cliente actual: GitHub MCP ya está configurado y una consulta de lectura autorizada funcionó. Supabase MCP aparece registrado, sin prueba de conexión. Angular Agent Skills no aparece en los ámbitos relevantes, que sí pudieron inspeccionarse. Next.js DevTools no corresponde al stack Angular. Los permisos no permiten inspeccionar los plugins privados. Presenta el Informe de Herramientas Recomendadas y Estado del Entorno. Trabaja en sólo lectura, sin instalar, activar, conectar servicios ni cambiar archivos. Espera mi selección.
```

Después del informe, envía «**UTILIZAR** Angular Agent Skills. Mantén mis otras decisiones». El resultado esperado es un plan de copia con archivos, alcance, permisos y prueba propuesta, seguido de una solicitud de autorización específica. El consumidor debe seguir intacto. En una conversación distinta ensaya un cambio de equipo con «Revisa las herramientas de este proyecto en esta instalación nueva. Sólo tienes acceso a los archivos del consumidor y al catálogo local». El estado operativo anterior debe dejar de presentarse como evidencia actual.

| Caso | Resultado esperado |
| --- | --- |
| GitHub MCP ya preparado | Reconoce la evidencia simulada y propone reutilizarlo dentro del alcance aceptado. Un mero registro justificaría verificar, sin reinstalar. |
| Supabase MCP registrado | Configurado sin verificar. Propone una prueba acotada y espera autorización si requiere conexión. |
| Angular Agent Skills ausente | Recomendada por el trabajo de interfaz y pendiente de selección inicial. |
| Next.js DevTools MCP en Angular | Incompatible para ese proyecto. Queda fuera de la propuesta de instalación. |
| Figma MCP pospuesto | Conserva la decisión incluso si el diseño aporta una razón para reconsiderarlo. |
| Playwright MCP omitido | Mantiene la omisión aunque la herramienta esté disponible. |
| Cambio de computadora | Conserva selecciones. El estado previo de GitHub MCP sólo sirve como registro histórico. |
| Cambio de fase | Añade la capacidad de Angular al pasar de SQL a interfaz y conserva las decisiones previas. |
| Permisos insuficientes | Estado desconocido para el inventario bloqueado. |
| Respuesta UTILIZAR | Solicita autorización específica antes de instalar, configurar, activar o ampliar permisos. |

El informe debe poder leerse sin conocer IDs ni comandos. Comprueba que cada fila tenga finalidad, prioridad, evidencia, acción, riesgo y recomendación, y que el resumen explique qué decisión necesitas tomar. Guarda los dos turnos iniciales, la evidencia del cambio de equipo y un inventario antes y después. Una captura de un servidor registrado por sí sola deja su operatividad pendiente.

### Reproducción offline para mantenimiento

Desde la raíz del Hub, reproduce la decisión sobre GitHub y Supabase con señales sintéticas de la sesión:

```console
python scripts/hub.py tools-plan --manifest templates/herramientas-proyecto.yaml --tool github-mcp --observed github-mcp=uso-verificado --tool supabase-mcp --observed supabase-mcp=configuracion-observada
python scripts/hub.py tools-plan --manifest templates/herramientas-proyecto.yaml --tool github-mcp
```

El primer comando propone reutilizar GitHub y verificar Supabase con autorización específica. El segundo conserva la selección y el alcance deseado de GitHub con estado `desconocido`. El comando consulta sólo las herramientas indicadas y funciona en modo lectura. Usa `recommend` para comprobar el perfil y sus condiciones antes de proponer incorporaciones. Los estados proceden de la evidencia que se indica al comando. Su salida sirve para preparar el informe y para planificar cambios tras la selección. La autorización de ejecución se obtiene en la conversación.

## Evidencia

| Comprobación | Evidencia y estado |
| --- | --- |
| Previsualización, copia de revisión fijada y destino por cliente | Pruebas automatizadas con repositorio y directorios de usuario temporales. |
| Copia existente, ausencia de Git, versión estable sin la skill y ramas candidatas | Pruebas automatizadas que comprueban que no cambia el directorio de usuario. |
| Selección offline y rechazo de perfiles o capacidades incompatibles | Suite del catálogo con condiciones, stack, permisos y cliente. |
| Decisiones, evidencia actual, validación del manifiesto y consultas de sólo lectura | Diez pruebas sintéticas de `test_project_tools.py` aprobadas dentro de la suite local. |
| Descubrimiento con Codex CLI `0.171.0-alpha.13` | BLOQUEADA. El proceso local terminó antes de responder a la consulta de metadatos. No se ejecutó un turno con modelo. |
| Descubrimiento y tres turnos en Codex Desktop y Antigravity App | PENDIENTE de capturas y respuesta de cada cliente. |
| Preparación del entorno y revisión de un proyecto existente en Antigravity App | ACEPTADAS por el responsable. La evidencia recibida describe el flujo observado y no identifica la invocación de una skill concreta. |
| Primera preparación completa en un equipo recién configurado | PENDIENTE de un recorrido manual, incluido el descubrimiento tras la instalación de usuario. |
| Informe, diálogo de aprobación y persistencia por parte del agente | PENDIENTE de los ensayos manuales en Codex Desktop y Antigravity App. |

Desde la raíz del Hub, ejecuta el [procedimiento de pruebas](../pruebas.md). El instalador usa sólo la biblioteca estándar de Python y Git local. El conjunto de pruebas del catálogo requiere las dependencias habituales del Hub.
