# Auditoría de aceptación de Agent Engineering Hub 0.1.0

**19 de noviembre de 2026.** La revisión se hizo sobre la etiqueta `v0.1.0` y el commit `bb83ee0`. Los cambios de preparación están en `audit/aceptacion-0.2.0`. La versión cerrada pasa la validación del repositorio y es apta para una publicación inicial del código y la documentación. La aceptación funcional en consumidores queda **parcial** por los bloqueos de ejecución observados en los dos clientes.

## 1. Revisión de la entrega

| Área | Resultado |
| --- | --- |
| Árbol versionado | 63 archivos. `main` y `v0.1.0` identifican el mismo commit. El historial alcanzable desde ambos contiene el commit inicial. |
| Contratos y catálogo | `validate` devolvió 20 capacidades, cinco perfiles y cuatro skills propias. Los catálogos MCP representan evidencia documental; la auditoría no abrió sesiones MCP. |
| CLI y pruebas | Las 20 pruebas de la etiqueta pasaron con Python 3.13.5. La suite comprueba selección en ambos agentes como política del catálogo, sin ejecutar los clientes. La ruta de CLI admite una llamada desde fuera del Hub. |
| Instrucciones | Se cotejaron README, AGENTS, perfiles, guías y workflow con las entradas y argumentos del código. La CLI propone capacidades según el perfil y las condiciones indicadas. La copia se realiza en un paso separado solicitado por el operador. |
| Fuentes de interoperabilidad | Los dos clientes documentan `.agents/skills/` para skills del proyecto, con diferencias entre superficies para invocación. Agent Skills contempla recursos relativos al directorio de la skill y carga progresiva. [Codex](https://learn.chatgpt.com/docs/build-skills) · [Antigravity](https://antigravity.google/docs/skills) · [Agent Skills](https://agentskills.io/specification) |

## 2. Matriz de pruebas

Los cuatro consumidores, con una sola skill copiada en cada uno, se generaron desde los archivos de la etiqueta. Se usó Codex CLI **0.169.1** con sesión existente, modo efímero, sólo lectura y configuración de usuario omitida para los turnos. Antigravity IDE reportó **1.107.0** por su CLI y mostraba **Gemini 3.8 Flash High** en el selector.

| Skill | Codex descubrimiento local | Codex explícito / implícito / negativo con modelo | Codex con datos adjuntos | Antigravity IDE |
| --- | --- | --- | --- | --- |
| `project-bootstrap` | Habilitada. Ruta dentro del consumidor. | Explícito e implícito bloqueados al leer stack y catálogo. El control se limitó a pedir la versión de Angular, pero la lectura de `package.json` también se bloqueó. | Seleccionó los cinco IDs correctos y excluyó alojamiento y MCP. Inicialmente declaró las condiciones como inactivas pese a usar el resultado de una consulta condicionada. | Pendiente. |
| `domain-discovery` | Habilitada. Ruta dentro del consumidor. | Explícito e implícito bloqueados al leer E-07. El control definió «folio» en una frase, sin llamada a herramientas observada. | Trazó el flujo a E-07 y dejó abiertas moneda, umbral, aprobación y excepción fuera de horario. | Nombre y descripción visibles y selección explícita realizada. El turno y una consulta de disponibilidad sin herramientas fallaron con `Agent execution terminated due to error`. |
| `change-impact-analysis` | Habilitada. Ruta dentro del consumidor. | Explícito e implícito bloqueados al leer el cambio, móvil y migración. En el control se observó un intento de lectura pese a que sólo se pidió definir `text`; quedó bloqueado. Sin evidencia de activación de la skill en ese control. | Identificó riesgo crítico, firma antigua incompatible, filas nulas, coexistencia de clientes y reversión que preserva datos. | Pendiente. |
| `hub-maintainer` | Habilitada. Ruta dentro del consumidor. | Explícito e implícito bloqueados al leer el aviso y el Hub de referencia. El control definió semver sin llamada a herramientas observada. | Elaboró un borrador de Issue, mantuvo la referencia y fecha y dejó el supuesto cambio de permisos sin confirmar. | Pendiente. |

### Evidencia y alcance

- **Descubrimiento sin modelo.** `skills/list` del servidor local de Codex devolvió la skill exacta en cada consumidor y ninguna skill del Hub en el control con copia únicamente en `skills/domain-discovery/`. Antigravity mostró `domain-discovery` y su descripción al teclear el nombre en el menú de acciones. La etiqueta de la skill quedó visible en el mensaje enviado.
- **Turnos con archivos locales.** Codex completó doce turnos nuevos, cuatro con prefijo `$nombre`, cuatro sin nombre y cuatro controles. Los intentos de lectura registraron `blocked by policy`. Las respuestas implícitas positivas mencionaron la skill pertinente o su lectura bloqueada. Eso acredita selección aparente, mientras que la carga efectiva y la lectura de referencias quedan pendientes. Se compararon hashes de los escenarios y el Hub de referencia antes y después y coincidieron.
- **Prueba complementaria con modelo.** Cuatro turnos nuevos en Codex recibieron el caso y las fuentes de prueba como texto adjunto, sin adjuntar el cuerpo de la skill. Los cuatro completaron la respuesta sin herramientas observadas. Al repetir bootstrap con el resumen corregido de la CLI, la respuesta enumeró `cambio-existente` y `cambio-sql` y conservó los cinco IDs esperados. Esta prueba mide respuesta con evidencia controlada. El acceso a archivos y la activación automática requieren sus propios resultados.
- **Control de Antigravity.** El IDE terminó con el mismo error al enviar un caso pertinente y una pregunta general que no necesitaba acceso al proyecto. La causa del error no quedó determinada. Antigravity App estaba instalada y activa en otro proyecto. `agy` no se encontró en PATH ni entre los binarios de las instalaciones inspeccionadas. Los ensayos de esas superficies quedan pendientes.
- **Referencias probadas.** Las skills originales contienen sus instrucciones en un único `SKILL.md`. La prueba distingue los archivos del consumidor, como `entrevista.md` y `migration.sql`, del catálogo externo al consumidor que necesitan las dos skills orientadas al Hub. Sus resultados con adjuntos no acreditan una lectura realizada por el cliente.

## 3. Distribución selectiva

Se copiaron las cuatro carpetas individualmente y Codex enumeró exactamente la solicitada en cada consumidor. El comando documentado de bootstrap produjo un único `SKILL.md` idéntico al original. Un segundo intento sobre la misma ruta falló y preservó su contenido. Desde el consumidor, el operador ejecutó la CLI del Hub desde su propio checkout y obtuvo `angular-skills`, `change-impact-analysis`, `project-bootstrap`, `supabase-skills` y `cambio-controlado`. Pages ya estaba decidido y el SQL local bastaba para la preparación.

`domain-discovery` y `change-impact-analysis` pueden usar la carpeta copiada con las fuentes del consumidor. `project-bootstrap` necesita acceso a un checkout del Hub para proponer IDs verificados y puede comenzar inventariando sin él. `hub-maintainer` requiere leer el Hub que audita. Ninguna de las cuatro depende de una ruta absoluta fija.

Se conserva `skills/` para las tres fuentes distribuibles y `.agents/skills/` como origen del mantenedor y destino de descubrimiento del consumidor. Una copia de proyecto puede desactualizarse o coincidir con una skill global del mismo nombre. Registrar su referencia y comprobar su origen evita ambigüedad al actualizarla. El Hub no necesita un instalador ni una segunda copia permanente para resolver esto. [Guía de incorporación](agentes.md)

## 4. Hallazgos y acciones

| Severidad para la aceptación | Hallazgo | Acción |
| --- | --- | --- |
| Alta | Codex descubre las cuatro skills, pero la política de ejecución bloqueó incluso comandos de lectura en los consumidores. No se pudo observar la cadena completa de lectura en ese entorno. | Repetir con un entorno aprobado que permita lecturas acotadas. Mantener turnos y evidencias de activación separados. |
| Alta | Antigravity IDE descubre la skill de dominio, pero su agente falla aun en un control sin herramientas. | Repetir cuando el motor responda. La matriz manual ya es reproducible. |
| Media | `recommend` no mostraba las condiciones activas. Una respuesta con datos adjuntos interpretó la ausencia como «ninguna». | En la rama de auditoría, la CLI imprime las condiciones y tiene una comprobación de regresión. La skill pide registrarlas y describe la lectura directa si la CLI no está disponible. Las 20 pruebas volvieron a pasar. |
| Media | El README podía leerse como cobertura funcional en ambos clientes. La receta inicial ejemplificaba dominio y dejaba al lector adaptar bootstrap. | Se acotó la afirmación y se añadió la receta de bootstrap, las dependencias de checkout y el [protocolo de aceptación](aceptacion-consumidores.md). |
| Media | La CI de PR valida datos candidatos con la base revisada. Cambios de código o contratos necesitan revisión y ejecución de la suite candidata en un entorno aislado. El workflow candidato también puede cambiar en un PR. | Al publicar, habilitar revisión de workflows de colaboradores, revisión de cambios en CI y protección de `main`. Observar la primera ejecución alojada. [Seguridad de GitHub Actions](https://docs.github.com/en/actions/reference/security/secure-use) |

## 5. Preparación para publicación

**Resultado.** `main` y `v0.1.0` están preparados como snapshot inicial de fuentes. La etiqueta identifica la evidencia original de 0.1.0. La disponibilidad de GitHub Actions y la interoperabilidad completa quedan como verificaciones operativas aparte.

- **Historial y privacidad.** Se inspeccionaron la lista de archivos y el único commit alcanzable. El escaneo de patrones de credenciales, rutas personales y claves privadas no devolvió coincidencias. La revisión de los TOML encontró ejemplos inertes y el marcador `PROJECT_REF`. Es una inspección estática y acotada.
- **Dependencias y licencias.** MIT está presente para el Hub. Las fichas conservan licencias de terceros. No se distribuyen implementaciones de las integraciones externas. OSV no informó avisos para las dos versiones directas declaradas y las cuatro versiones transitivas instaladas examinadas. Dependencias transitivas y paquetes de Ubuntu pueden resolver otras versiones en una máquina nueva. [OSV](https://osv.dev/)
- **Workflow.** `pull_request` y push a `main`, permisos `contents: read`, persistencia de credenciales deshabilitada y acción fijada a un commit oficial comprobado. La base ejecuta pruebas revisadas; el checkout candidato se pasa como datos. El runner de GitHub queda pendiente de la primera publicación autorizada. [Commit de actions/checkout](https://github.com/actions/checkout/commit/d23441a48e516b6c34aea4fa41551a30e30af803)

## 6. Propuesta de alcance para v0.2.0

1. Completar la matriz por skill y por cliente en proyectos temporales. Cerrar cada caso positivo con evidencia de activación, lectura de referencia y resultado. Registrar falsos positivos en los controles.
2. Probar bootstrap con checkout disponible y sin acceso a la CLI para verificar la lectura directa. Probar dominio e impacto con la sola carpeta copiada. Probar mantenimiento como propuesta de Issue basada en un checkout accesible.
3. Incorporar los cambios mínimos de esta rama y conservar en el catálogo los estados de verificación por evidencia observada. Realizar una primera CI pública únicamente tras autorización.
4. Considerar una comprobación automatizada de descubrimiento cuando exista una interfaz estable por cliente. Mantener la instalación selectiva y posponer nuevas integraciones hasta cerrar los casos anteriores.
