# Pruebas desde proyectos consumidores

Usa un checkout revisado del Hub. Cada escenario contiene una sola skill y archivos ficticios. El catálogo de referencia queda en un directorio hermano, fuera del alcance de descubrimiento del consumidor.

Este protocolo conserva la regresión completa. Para ejecutar un turno por skill empieza por la [prueba rápida de v0.2.0](testing/validacion-manual-agentes-v0.2.0.md).

## Preparar los escenarios

Desde el Hub, ejecuta el generador con un destino **que aún no exista**. Sólo necesita Python 3.11+ y la biblioteca estándar.

```console
python tests/fixtures/prepare_consumers.py RUTA_TEMPORAL_NUEVA
```

Abre cada subdirectorio de skill como un proyecto independiente. Conserva `hub-reference` como directorio hermano. Contiene una copia parcial del Hub para estas consultas. Para un proyecto real usa un checkout del Hub.

## Tres turnos independientes por skill

1. **Explícito.** Selecciona la skill del proyecto desde el menú del cliente y envía el caso positivo.
2. **Implícito.** Inicia una conversación nueva y envía únicamente el caso positivo sin nombrar la skill ni su ruta. Busca una lectura de `SKILL.md` o una señal de activación del cliente.
3. **Negativo.** Inicia otra conversación y envía el control fuera de alcance. Confirma que la respuesta se limita a la pregunta y registra si consultó la skill.

Añade a cada caso: «Trabaja en sólo lectura. Usa únicamente los archivos sintéticos pertinentes. No instales, modifiques, busques en la web ni conectes servicios». Comprueba los archivos antes y después. Si el cliente rechaza lecturas, registra el bloqueo. Un ensayo con los datos pegados puede acreditar la respuesta del modelo, pero deja la lectura por el cliente pendiente.

| Proyecto | Caso positivo | Control negativo | Resultado esperado |
| --- | --- | --- | --- |
| `project-bootstrap` | Lee `project.md` y `package.json`. Propón capacidades mínimas para preparar el cambio. El catálogo local está en `../hub-reference`. | Indica solamente la versión de `@angular/core` declarada en `package.json`. | Variante de mantenimiento. Perfil `angular-supabase-cloudflare` con `trabajo-frontend`, `cambio-existente` y `cambio-sql`. Seis candidatas en el perfil, alojamiento y MCP excluidos. La propuesta justifica las que usa. |
| `domain-discovery` | Lee `entrevista.md`. Entrega una ficha previa al diseño con actores, flujo, reglas, excepciones y requisitos con fuente. | Define «folio» en una frase sin inspeccionar el proyecto. | Operadora, cliente y supervisor. Evidencia E-07. Umbral, moneda, obligatoriedad y horario como decisiones abiertas. |
| `change-impact-analysis` | Evalúa `change.md`, `mobile.ts` y `migration.sql`. Clasifica riesgo e incluye impacto, pruebas y reversión. | Explica el tipo SQL `text` en una frase sin inspeccionar el proyecto. | Riesgo crítico por RPC móvil incompatible y filas históricas. Coexistencia de clientes, ensayos de datos nulos y reversión compatible. |
| `hub-maintainer` | Audita la afirmación de `aviso.md` sobre Context7. El checkout de referencia está en `../hub-reference`. | Define semver en una frase sin auditar ninguna ficha. | Lee la ficha Context7 y el perfil pertinente. Conserva referencia y estado, identifica falta de fuente oficial y propone prueba futura. |

## Codex

En una sesión interactiva desde el proyecto, escribe `$` y selecciona la skill con el nombre de ese proyecto. Usa la ruta mostrada por el selector para descartar una copia global. En una prueba automatizada del protocolo, `skills/list` con el `cwd` del consumidor permite comprobar el origen de la skill sin ejecutar un modelo.

Para guardar eventos en una prueba con Codex CLI, ejecuta desde el consumidor:

```console
codex --ask-for-approval never exec --ignore-user-config --ephemeral --sandbox read-only --skip-git-repo-check --json 'PROMPT_SINTETICO'
```

Añade `$nombre-de-la-skill` al texto para el caso explícito y deja el caso implícito sin ese prefijo. Registra una señal de carga aparte de la calidad de la salida. En PowerShell, las comillas simples preservan `$`. La prueba usa la sesión de Codex ya autenticada. Un turno completado con error de lectura deja pendiente la prueba de extremo a extremo.

## Antigravity App

1. En **Projects**, crea un Project con **Add Folder** y añade sólo el subdirectorio del caso. Para `project-bootstrap` y `hub-maintainer`, añade también `hub-reference` como carpeta de lectura del mismo Project. Inicia una conversación en ese Project y elige **Local** si aparece el selector.
2. Escribe `/nombre-de-la-skill` y selecciona la entrada del workspace. Si **Customizations** muestra el origen, comprueba que corresponde al consumidor. Registra por separado cualquier bloqueo de lectura.
3. Ejecuta los tres turnos de cada fila. Si el primer turno falla con un error del agente, haz una consulta de control sin herramientas para comprobar disponibilidad. Conserva el error como resultado de entorno y repite la matriz cuando el cliente pueda responder.
4. Registra superficie, versión, modelo, habilidad descubierta, archivos leídos, resultado y restricciones observadas. Un nombre visible acredita descubrimiento. La validación funcional requiere una respuesta y evidencia de las lecturas pertinentes.

## Otras superficies de Antigravity

- **IDE independiente:** abre el subdirectorio mediante **File > Open Folder**. Revisa **Customizations** en el panel del agente y usa el selector de skills si está disponible. Conserva este ensayo como evidencia específica del IDE.
- **CLI interactiva:** arranca en el subdirectorio del caso y usa `/nombre-de-la-skill`. Si acabas de copiarla, usa una conversación nueva o `/skills reload`.

Fuentes para los procedimientos de cliente. [Agent Skills](https://agentskills.io/specification) · [Codex](https://learn.chatgpt.com/docs/build-skills) · [Proyectos de Antigravity](https://antigravity.google/docs/projects) · [Skills de Antigravity](https://antigravity.google/docs/skills)
