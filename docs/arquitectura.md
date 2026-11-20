# Arquitectura de la biblioteca

Una ficha identifica una capacidad por su función. Un perfil expresa cuándo conviene utilizarla. Una propuesta combina ambas cosas y termina antes de instalar software. La selección se puede reproducir con el mismo checkout, perfil, agente y condiciones locales.

## Decisiones de la versión 0.1.0

| Decisión | Motivo y consecuencia |
| --- | --- |
| Un documento por ID en `catalog/` y `profiles/` | El historial Git y las revisiones quedan acotados. Un agente puede pedir un ID o un tipo antes de leer una ficha. |
| YAML o JSON para datos y JSON Schema 2020-12 para contratos | Python con PyYAML y jsonschema permite detectar errores de forma antes de recorrer el grafo. Se rechazan claves repetidas. |
| Separar requisitos técnicos de dependencias del catálogo | Node, Docker o un navegador son prerrequisitos de operación. Sólo un ID del Hub puede ser una dependencia resoluble. |
| Una ubicación canónica por skill | Las tres skills de producto se distribuyen desde `skills/`. La de mantenimiento se distribuye directamente desde `.agents/skills/hub-maintainer/`, donde la descubren los dos clientes. Funciona en checkouts de Windows sin enlaces simbólicos. |
| Evidencia documental y ejecución en campos independientes | Un commit identifica fuentes, no acredita que un servidor haya funcionado con una versión concreta del cliente. |
| CLI de consulta, sin credenciales | Listar, inspeccionar, validar y recomendar son operaciones locales. La CI trata las contribuciones como datos. |

## Vocabulario

| Objeto | Qué aporta | Ejemplo |
| --- | --- | --- |
| Agent Skill | Un directorio portable con metadatos de selección y un procedimiento en SKILL.md | domain-discovery |
| Servidor MCP | Expone herramientas o recursos a un cliente mediante un transporte | Angular CLI por stdio |
| Rule | Instrucciones permanentes con alcance de directorio o usuario | AGENTS.md del Hub |
| Workflow | Procedimiento humano o asistido con entrada, decisiones y evidencia de salida | Cambio controlado |
| Project Profile | Reglas declarativas para elegir capacidades según stack y tarea | angular-frontend |
| Herramienta de desarrollo | Ejecutable que realiza una operación concreta | Codex CLI en una evaluación |
| Plugin | Unidad de distribución que puede agrupar skills, MCP y otras extensiones | Plugin de Cloudflare |

El directorio `mcp/` contiene recetas inertes. `templates/` da forma a la evidencia, `workflows/` conecta decisiones de ingeniería y `examples/` muestra cómo verificar el resultado. Los contratos viven en `schemas/` y la lógica ejecutable propia en `scripts/`; las pruebas construyen variantes del catálogo en directorios temporales.

## Recorrido de una solicitud

1. Identificar el perfil y recoger hechos observables del proyecto.
2. Obtener candidatos con `list` o `recommend` y abrir sólo las fichas relevantes con `show`.
3. Evaluar permisos, dependencias, capacidades existentes y evidencia de compatibilidad.
4. Entregar una propuesta con inclusiones y exclusiones justificadas.
5. Si se solicita una instalación, revisar la referencia exacta y el destino del proyecto. La CLI del Hub termina en el paso 4.

Una nueva integración entra por una ficha y sus pruebas de coherencia. Una nueva superficie de agente requiere además verificar el descubrimiento, el formato de invocación y los permisos antes de extender los contratos.
