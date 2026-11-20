# Agent Engineering Hub

Biblioteca de ingeniería para equipos que desarrollan con agentes. La versión **0.1.0** permite pasar de una necesidad concreta a una propuesta de skills, herramientas y procedimientos con dependencias, permisos y fuentes revisables. La CLI funciona sobre un checkout local y las skills usan el formato de descubrimiento por proyecto de Codex y Antigravity.

**English overview.** Use this repository to discover capabilities, compare their permissions, and select a minimal set for a project. The CLI works offline after its Python dependencies are available. Start with the [quick start](docs/inicio-rapido.md) and [worked examples](examples/escenarios.md).

## Primera consulta

Con Python 3.11 o posterior y las dependencias del proyecto disponibles, ejecuta desde la raíz:

```console
python scripts/hub.py validate
python scripts/hub.py recommend angular-supabase-cloudflare --context cambio-sql
python scripts/hub.py show supabase-skills
```

La primera orden comprueba **20 capacidades, cinco perfiles y cuatro skills propias**. La segunda propone `project-bootstrap`, `angular-skills` y `supabase-skills` para revisar SQL local. La tercera muestra la evidencia y las condiciones de uso de una sola ficha. Si partes de un entorno limpio, sigue el [inicio rápido para Windows y POSIX](docs/inicio-rapido.md).

## Qué incluye

| Busco… | Entrada |
| --- | --- |
| Seleccionar herramientas para una aplicación | [Perfiles y selección](docs/catalogo-y-perfiles.md) |
| Usar el Hub desde mi agente | [Codex y Antigravity](docs/agentes.md) · [ejemplos reproducibles](examples/escenarios.md) |
| Investigar negocio o preparar un cambio de producción | [Descubrimiento](workflows/descubrimiento.md) · [cambio controlado](workflows/cambio-controlado.md) |
| Consultar una integración y sus permisos | [Catálogo](catalog/) · [ejemplos MCP](mcp/README.md) |
| Entender el diseño y los formatos | [Arquitectura](docs/arquitectura.md) · [contratos](schemas/) |
| Crear skills, registrar MCP o extender perfiles | [Guía de autoría](docs/autoria.md) |
| Revisar versiones y decisiones | [Mantenimiento](docs/mantenimiento.md) · [historial](CHANGELOG.md) |
| Validar, contribuir o evaluar riesgos | [Pruebas](docs/pruebas.md) · [contribuciones](CONTRIBUTING.md) · [seguridad](SECURITY.md) |
| Consultar próximos hitos | [Roadmap](docs/roadmap.md) |
| Revisar la entrega 0.1.0 | [Inventario, resultados y limitaciones](docs/informe-0.1.0.md) |
| Repetir las pruebas desde un proyecto consumidor | [Protocolo de aceptación](docs/aceptacion-consumidores.md) · [Auditoría de 0.1.0](docs/auditoria-aceptacion-0.1.0.md) |

Las skills originales cubren [arranque](skills/project-bootstrap/SKILL.md), [dominio](skills/domain-discovery/SKILL.md), [impacto](skills/change-impact-analysis/SKILL.md) y [mantenimiento](.agents/skills/hub-maintainer/SKILL.md). Los datos se pueden leer directamente como YAML o consultar por tipo, tecnología e ID. Consultar una ficha o elegir un perfil no instala nada.

## Alcance de la evidencia

Las 14 fichas externas identifican fuentes primarias, fecha y commit consultado. Para las skills de Angular y las dos skills de sistema de Codex se inspeccionaron metadatos y licencias. Para la CLI de evaluación se comprobó la ayuda local. Los MCP se registraron sin establecer sesiones con servicios externos. Entre las skills propias, `project-bootstrap` cuenta además con un ensayo de comportamiento en Codex. Cada ficha delimita su evidencia en `review`.

El contenido original se distribuye bajo [MIT](LICENSE). Los recursos enlazados conservan sus licencias. Una licencia pendiente de confirmar se indica en su ficha.
