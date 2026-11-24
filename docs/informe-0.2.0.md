# Informe de versión 0.2.0

## Contenido consolidado

El inventario es de **29 capacidades, cinco perfiles y cinco skills propias**. Incluye Domain-First Agile Engineering, la actualización del catálogo y `hub-guide`. El [changelog](../CHANGELOG.md) resume las novedades y la [guía de inicio](guia-hub.md) muestra cómo revisar un proyecto, elegir herramientas y autorizar su configuración.

| Referencia examinada | Inventario | Qué contiene |
| --- | --- | --- |
| `bb83ee0` · `v0.1.0` | 20 capacidades, cinco perfiles, cuatro skills | Primera versión estable. |
| `7374c75` · cabecera publicada inicial del PR #1 | 28 capacidades, cinco perfiles, cuatro skills | Catálogo ampliado y metodología. |
| `67c5754` · candidata local previa | 28 capacidades, cinco perfiles, cuatro skills | Corrección de las instrucciones y prueba rápida para Antigravity App. |
| `5d05812` y `6137052` · `codex/hub-guide` | 29 capacidades, cinco perfiles, cinco skills | Entrada conversacional, instalador con vista previa, informe, decisiones por herramienta y manifiesto por proyecto. |

El inventario de las pruebas recientes coincide con la rama que incorpora `hub-guide`. La evidencia recibida carece del SHA exacto, la versión del cliente, el modelo y una traza de invocación de skill. Los commits anteriores permiten reproducir el inventario y las pruebas locales.

## Aceptación funcional

El responsable del proyecto aprobó los siguientes escenarios ejecutados personalmente en **Google Antigravity App**. Se omiten el nombre del proyecto consumidor y los detalles de su entorno.

| Escenario | Resultado aceptado |
| --- | --- |
| Preparar el entorno | Consultó el Hub y la versión estable, inventarió herramientas, versiones, skills, plugins y MCP, diferenció configuración de conexión verificada y evitó duplicados. Presentó opciones y pidió una decisión antes de actuar. |
| Revisar un proyecto Angular 22 con Supabase y Cloudflare | Leyó el contexto, validó el catálogo y seleccionó el perfil pertinente. Reconoció Modern Web Guidance como instalada, recomendó herramientas según el cambio, respetó las restricciones de producción y pidió autorización antes de configurar. |

Esta aceptación corresponde a los dos flujos observados. La [matriz por skill y cliente](testing/validacion-manual-agentes-v0.2.0.md) y los [casos de hub-guide](testing/hub-guide.md) quedan disponibles para regresiones posteriores. Los ensayos de Codex bloqueados y el ensayo previo en Antigravity IDE conservan su estado. La evidencia no acredita la invocación de cada skill ni la conexión de cada MCP.

## Metodología

La revisión usa escenarios sintéticos y el [procedimiento de Domain-First Agile Engineering](metodologia/domain-first-agile-engineering.md).

| Escenario | Resultado de la revisión |
| --- | --- |
| Sistema empresarial de anticipos | La regla de que un solicitante no aprueba su propio anticipo se vincula al requisito y al criterio de una historia. La suplencia queda como decisión abierta. El primer incremento del roadmap es un prototipo de los dos roles, seguido de maquetación, pruebas de permisos, implementación incremental y un despliegue de prueba controlado. |
| Sitio pequeño de horarios | El incremento inicial es publicar y corregir horarios accesibles con datos sintéticos. Una revisión del contenido y de la validación web basta para planificar ese incremento. Se dejan prototipado complejo y conexiones MCP fuera de la propuesta. |
| RPC existente con clientes en uso | Se priorizan impacto de contrato, clientes antiguos y filas históricas. Se propone compatibilidad temporal, pruebas de datos y reversión con criterios de parada. Se reutiliza el contexto ya documentado y se omite rehacer el descubrimiento o prototipar una interfaz ajena al cambio. |

Son ejercicios de planificación. Stitch y Figma conservan revisión documental y prueba funcional pendiente. El alcance y los permisos de una integración se revisan en su ficha antes de conectarla.

## Validación técnica

Desde la raíz puede repetirse la validación offline:

```console
python scripts/hub.py validate
python -m unittest discover -s tests -v
```

La suite cubre contratos, perfiles, compatibilidad, dependencias y conflictos, referencias, selección contextual, copia segura de la skill y decisiones por proyecto. La validación de un consumidor conserva por separado el estado deseado y la evidencia del entorno actual. El contenido original usa MIT y los recursos externos conservan sus licencias indicadas en el catálogo. El validador local y las regresiones de Windows complementan la ejecución alojada.

## Publicación y GitHub Actions

El [PR #2](https://github.com/omparedes/AgentEngineeringHub/pull/2) integró `36f0b3a` en `main` con un árbol idéntico en `9ae8f5a`. La consulta inicial devolvió cero ejecuciones para la candidata y para ese commit de integración. Actions estaba habilitado y el workflow activo. Las suites de Vercel y Cloudflare correspondían a otras aplicaciones. La publicación del tag estable requiere una ejecución alojada satisfactoria de `Validar Hub` para el SHA definitivo de `main`. Se admite [una ejecución manual](pruebas.md#qué-prueba-github-actions) con evidencia del SHA, validador y suite. El funcionamiento de los disparadores automáticos se comprueba por separado. [GitHub Actions](https://github.com/omparedes/AgentEngineeringHub/actions/workflows/validate.yml)

Para confirmar el estado vigente, revisa la referencia de `v0.2.0` y las ejecuciones por SHA. Si GitHub registra el push pero sigue sin generar una ejecución, conserva SHA, rama, workflow, hora y resultados de la API para diagnosticar la creación del run. [Etiquetas](https://github.com/omparedes/AgentEngineeringHub/tags) · [Diagnóstico oficial de workflows](https://docs.github.com/en/actions/how-tos/troubleshoot-workflows)
