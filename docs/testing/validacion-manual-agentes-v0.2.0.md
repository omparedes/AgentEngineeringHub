# Validación manual rápida de v0.2.0

Ejecuta un turno por skill en Antigravity App. Si quieres comparar Codex Desktop, repite los mismos cuatro prompts. La [regresión completa](../aceptacion-consumidores.md) conserva los turnos explícito, implícito y negativo para mantenimiento y cierre.

## Preparar los proyectos

Desde la raíz del Hub, ejecuta una vez en Windows con PowerShell 7 y Python 3.11 o posterior. El bloque crea cuatro proyectos sintéticos, cada uno con su propia skill en `.agents/skills/<nombre>/SKILL.md`. Guarda el SHA y la ubicación que imprime.

```powershell
$aehManual = Join-Path ([IO.Path]::GetTempPath()) ('aeh-v020-manual-' + [guid]::NewGuid().ToString('N'))
python tests/fixtures/prepare_consumers.py $aehManual
if ($LASTEXITCODE -ne 0) { throw 'Falló la preparación de los consumidores.' }

@'
# Proyecto Faro (ficticio)
Estamos iniciando un sistema administrativo para solicitar y revisar anticipos.
Angular y Supabase están elegidos. Cloudflare Pages ya está decidido para Preview.
La primera entrega es una pantalla para solicitantes y aprobadores.
Finanzas confirma que un solicitante nunca aprueba su propio anticipo.
Falta decidir quién reemplaza al aprobador. Queremos validar la navegación de los
dos roles con datos sintéticos antes de diseñar la persistencia o conectar servicios.
'@ | Set-Content -LiteralPath (Join-Path $aehManual 'project-bootstrap/project.md') -Encoding utf8

@'
# Consumidores ficticios de registrar_envio
Despacho usa mobile.ts. Ese cliente anterior seguirá en servicio durante una semana.
Facturación también invoca registrar_envio(peso) mediante un adaptador de lotes.
Auditoría lee registros históricos de envios. Algunos tienen zona nula.
'@ | Set-Content -LiteralPath (Join-Path $aehManual 'change-impact-analysis/consumidores.md') -Encoding utf8

@'
# Aviso A-04 (ficticio)
Un boletín sin autor identificado afirma que la supuesta versión v99.0 de Context7
amplía los permisos de herramientas. No adjunta repositorio, release ni changelog.
El aviso no confirma que exista esa versión ni autoriza una conexión.
'@ | Set-Content -LiteralPath (Join-Path $aehManual 'hub-maintainer/aviso.md') -Encoding utf8

git rev-parse HEAD
$aehManual
```

## Abrir y ejecutar

1. **Antigravity App.** En **Projects**, pulsa **+** o **New Project**, elige **Add Folder** y selecciona la carpeta del caso. Para A y D añade también `hub-reference` al mismo Project. Pulsa **Create**, abre una conversación dentro del Project y selecciona **Local** si aparece el selector. El botón **Open IDE** abre el IDE independiente.
2. En la conversación escribe el prefijo `/nombre-de-la-skill`, elige la entrada del proyecto y pega el prompt. Si aparece más de una entrada, usa el origen del Project cuando el cliente lo muestre. **Customizations** permite revisar las skills disponibles.
3. **Codex Desktop.** Abre la carpeta del caso como proyecto local, inicia un chat y elige la skill escribiendo `$`. En A y D el agente necesita leer `../hub-reference` según los permisos normales del cliente. Registra los bloqueos de acceso.
4. Guarda la señal de selección o lectura de la skill y el resultado. Si la política impide leer una skill o un archivo, conserva el mensaje y marca el caso `BLOQUEADA`.

Instrucciones oficiales. [Proyectos de Antigravity App](https://antigravity.google/docs/projects) · [Skills de Antigravity App](https://antigravity.google/docs/skills) · [Skills de Codex](https://learn.chatgpt.com/docs/build-skills)

## A. Arranque de Faro

Abre `project-bootstrap`. Elige `/project-bootstrap` en App o `$project-bootstrap` en Codex.

```text
Lee package.json y project.md del consumidor. Usa el catálogo local en ../hub-reference. Propón el perfil y las capacidades mínimas para iniciar Faro, con exclusiones y el siguiente resultado verificable. Trabaja en sólo lectura. No instales, conectes servicios ni consultes la web.
```

**Resultado esperado.** Angular y Supabase en el manifiesto, Pages ya decidido en la descripción, perfil `angular-supabase-cloudflare`, suplencia pendiente y una propuesta local para revisar el flujo de los dos roles. Debe evitar integraciones remotas y cambios de SQL prematuros.

**Evidencia.** Skill seleccionada, manifiesto y perfil consultados, capacidades elegidas y exclusiones.

## B. Descubrimiento de devoluciones

Abre `domain-discovery`. Elige `/domain-discovery` en App o `$domain-discovery` en Codex.

```text
Lee entrevista.md. Describe actores, flujo, reglas, excepciones y requisitos verificables. Cita la fuente y separa decisiones pendientes. Propón qué preguntar antes de diseñar. Trabaja en sólo lectura, sin programar ni usar recursos externos.
```

**Resultado esperado.** Operadora, cliente y supervisor. La entrevista E-07 sustenta el inicio con folio y la confirmación al cliente. Umbral, moneda, obligatoriedad y manejo fuera de horario quedan abiertos.

**Evidencia.** Skill seleccionada, lectura de E-07 y salida con al menos un requisito verificable y una pregunta abierta.

## C. Cambio en PostgreSQL

Abre `change-impact-analysis`. Elige `/change-impact-analysis` en App o `$change-impact-analysis` en Codex.

```text
Lee change.md, consumidores.md, mobile.ts y migration.sql. Evalúa exigir zona en registrar_envio y envios. Identifica consumidores, riesgos, pruebas y reversión. Trabaja en sólo lectura. No ejecutes SQL ni conectes bases de datos.
```

**Resultado esperado.** Riesgo crítico por el contrato compartido de Despacho y Facturación y los nulos históricos que afectan a Auditoría. Propone coexistencia de contratos, pruebas de ambos y reversión compatible con datos previos.

**Evidencia.** Skill seleccionada, archivos consultados y propuesta de pruebas, orden y reversión.

## D. Revisión de Context7

Abre `hub-maintainer`. Elige `/hub-maintainer` en App o `$hub-maintainer` en Codex.

```text
Lee aviso.md y audita la supuesta actualización de Context7 con el catálogo local de ../hub-reference. Recupera proveedor, fuente, referencia y estado de runtime. Distingue lo conocido de lo pendiente y propone una prueba futura. Trabaja en sólo lectura, sin actualizar, autenticar ni usar la web.
```

**Resultado esperado.** Upstash, enlace y referencia registrados en la ficha, estado `documented` y runtime `untested`. El aviso v99.0 queda sin confirmar y se propone contrastar una fuente oficial y observar permisos.

**Evidencia.** Skill seleccionada, ficha consultada, contraste con el aviso y propuesta de revisión.

## Matriz rápida

| Caso | Antigravity App | Codex Desktop | Evidencia |
| --- | --- | --- | --- |
| A. Arranque | PENDIENTE | PENDIENTE | — |
| B. Dominio | PENDIENTE | PENDIENTE | — |
| C. Impacto | PENDIENTE | PENDIENTE | — |
| D. Mantenimiento | PENDIENTE | PENDIENTE | — |

Usa `APROBADA` si se confirma el origen local y se cumplen el resultado y las restricciones. Registra `FALLIDA` si el turno se ejecuta pero incumple un criterio. Usa `BLOQUEADA` para un impedimento técnico y `PENDIENTE` si aún falta evidencia. `NO APLICABLE` se reserva para controles de interfaz ausentes en una superficie concreta. Envía por caso el SHA, versión del cliente, modelo, señal de carga, salida o captura saneada y cualquier error.

La guía se preparó y comprobó con datos locales. Los ocho turnos previos de Codex CLI `0.171.0-alpha.13` con `gpt-6.2-sol` quedaron `BLOQUEADA` para lectura. El ensayo anterior de Antigravity **IDE** `1.107.0` llegó al diálogo de confianza y la prueba con modelo quedó `NO EJECUTADA`. Esta matriz por skill queda pendiente. El responsable sí aprobó dos escenarios prácticos en Antigravity **App**, recogidos en el [informe de versión](../informe-0.2.0.md).

## Cerrar o limpiar

La ronda rápida y la [regresión completa](../aceptacion-consumidores.md) sirven para mantener la cobertura por skill. Consulta en el [informe de versión](../informe-0.2.0.md) los escenarios ya aceptados y el requisito de CI alojada.

Cuando termines, guarda la evidencia fuera del temporal y cierra los consumidores. En Projects puedes quitar sus accesos directos. En el Explorador, envía a la Papelera sólo el directorio temporal que imprimió el bloque, cuyo nombre empieza por `aeh-v020-manual-`.
