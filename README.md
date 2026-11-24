# Agent Engineering Hub

Biblioteca de ingeniería para equipos que desarrollan con agentes. El alcance de **v0.2.0** reúne el catálogo ampliado, Domain-First Agile Engineering y `hub-guide`, la puerta de entrada para revisar las herramientas de un proyecto y elegir cuáles utilizar. La CLI funciona sobre un checkout local. Consulta el [informe de versión](docs/informe-0.2.0.md) para ver el estado de publicación y la evidencia.

**English overview.** Use this repository to discover capabilities, compare their permissions, and select a minimal set for a project. The CLI works offline after its Python dependencies are available. Start with the [quick start](docs/inicio-rapido.md) and [worked examples](examples/escenarios.md).

## Primera consulta

Con Python 3.11 o posterior y las dependencias del proyecto disponibles, ejecuta desde la raíz:

```console
python scripts/hub.py validate
python scripts/hub.py recommend angular-supabase-cloudflare --context cambio-sql
python scripts/hub.py show supabase-skills
```

La primera orden comprueba **29 capacidades, cinco perfiles y cinco skills propias**. La segunda propone `project-bootstrap` y `supabase-skills` para revisar SQL local. La tercera muestra la evidencia y las condiciones de uso de una sola ficha. Si partes de un entorno limpio, sigue el [inicio rápido para Windows y POSIX](docs/inicio-rapido.md).

## Qué incluye

| Busco… | Entrada |
| --- | --- |
| Seleccionar herramientas para una aplicación | [Perfiles y selección](docs/catalogo-y-perfiles.md) |
| Usar el Hub desde mi agente | [Codex y Antigravity](docs/agentes.md) · [ejemplos reproducibles](examples/escenarios.md) |
| Pasar de ideas a un incremento verificable | [Domain-First Agile Engineering](docs/metodologia/domain-first-agile-engineering.md) · [cuatro casos ficticios](examples/domain-first.md) |
| Revisar un prototipo antes de implementar | [Workflow de prototipado](workflows/prototipado-validacion.md) · [Stitch y Figma](docs/prototipado.md) |
| Investigar negocio o preparar un cambio de producción | [Descubrimiento](workflows/descubrimiento.md) · [cambio controlado](workflows/cambio-controlado.md) |
| Consultar una integración y sus permisos | [Catálogo](catalog/) · [ejemplos MCP](mcp/README.md) |
| Elegir herramientas según la fase de ingeniería | [Testing, diseño, seguridad y observabilidad](docs/herramientas-ingenieria.md) |
| Orientar un cambio frontend con Baseline | [Modern Web Guidance en Codex y Antigravity](docs/modern-web-guidance.md) |
| Entender el diseño y los formatos | [Arquitectura](docs/arquitectura.md) · [contratos](schemas/) |
| Crear skills, registrar MCP o extender perfiles | [Guía de autoría](docs/autoria.md) |
| Revisar versiones y decisiones | [Mantenimiento](docs/mantenimiento.md) · [historial](CHANGELOG.md) |
| Preparar el equipo, iniciar o retomar un proyecto | [Empezar con el Hub](docs/guia-hub.md) |
| Validar, contribuir o evaluar riesgos | [Pruebas](docs/pruebas.md) · [contribuciones](CONTRIBUTING.md) · [seguridad](SECURITY.md) |
| Consultar próximos hitos | [Roadmap](docs/roadmap.md) |
| Revisar la entrega 0.1.0 | [Inventario, resultados y limitaciones](docs/informe-0.1.0.md) |
| Repetir las pruebas desde un proyecto consumidor | [Pruebas manuales de 0.2.0](docs/testing/validacion-manual-agentes-v0.2.0.md) · [Protocolo de aceptación](docs/aceptacion-consumidores.md) · [Auditoría de 0.1.0](docs/auditoria-aceptacion-0.1.0.md) |

Las skills originales cubren [guía y decisiones de herramientas](skills/hub-guide/SKILL.md), [arranque](skills/project-bootstrap/SKILL.md), [dominio](skills/domain-discovery/SKILL.md), [impacto](skills/change-impact-analysis/SKILL.md) y [mantenimiento](.agents/skills/hub-maintainer/SKILL.md). Con `hub-guide` puedes pedir «Revisa las herramientas de este proyecto», examinar el informe y decidir por herramienta. Cualquier instalación, configuración o activación requiere autorización específica.

## Alcance de la evidencia

Las 22 fichas externas identifican las fuentes y referencias consultadas. El responsable aprobó en Antigravity App los escenarios de preparación del entorno y revisión de un proyecto existente. Los ensayos exhaustivos por skill y cliente y las pruebas funcionales de MCP, Stitch y Figma conservan el estado que documenta el [informe de versión](docs/informe-0.2.0.md). Cada ficha delimita su evidencia en `review`.

El contenido original se distribuye bajo [MIT](LICENSE). Los recursos enlazados conservan sus licencias. Una licencia pendiente de confirmar se indica en su ficha.
