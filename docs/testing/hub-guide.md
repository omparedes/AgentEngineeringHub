# Ensayar hub-guide

Esta matriz corresponde a la propuesta para v0.3.0. La [validación manual de v0.2.0](validacion-manual-agentes-v0.2.0.md) sigue evaluando las cuatro skills de esa candidata.

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

## Evidencia

| Comprobación | Evidencia y estado |
| --- | --- |
| Previsualización, copia de revisión fijada y destino por cliente | Pruebas automatizadas con repositorio y directorios de usuario temporales. |
| Copia existente, ausencia de Git, versión estable sin la skill y ramas candidatas | Pruebas automatizadas que comprueban que no cambia el directorio de usuario. |
| Selección offline y rechazo de perfiles o capacidades incompatibles | Suite del catálogo con condiciones, stack, permisos y cliente. |
| Descubrimiento con Codex CLI `0.171.0-alpha.13` | BLOQUEADA. El proceso local terminó antes de responder a la consulta de metadatos. No se ejecutó un turno con modelo. |
| Descubrimiento y tres turnos en Codex Desktop y Antigravity App | PENDIENTE de capturas y respuesta de cada cliente. |
| Primera preparación completa en un equipo recién configurado | PENDIENTE de un recorrido manual, incluido el descubrimiento tras la instalación de usuario. |

Desde la raíz del Hub, ejecuta el [procedimiento de pruebas](../pruebas.md). El instalador usa sólo la biblioteca estándar de Python y Git local. El conjunto de pruebas del catálogo requiere las dependencias habituales del Hub.
