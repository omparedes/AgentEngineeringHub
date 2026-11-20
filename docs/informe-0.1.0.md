# Informe de implementación · 0.1.0

**19 de noviembre de 2026.** El Hub convierte el inventario de un proyecto en una propuesta local y trazable. La primera entrega contiene 63 archivos de distribución, 14 fichas externas, cuatro skills propias, dos workflows y cinco perfiles. Cada propuesta explica sus inclusiones y exclusiones. Se eligieron YAML/JSON y Python por su portabilidad y por las dos dependencias de validación disponibles; el proyecto carece de servicios de ejecución externos propios.

## Inventario real de distribución

```text
AgentEngineeringHub/
├── .agents/
│   └── skills/
│       └── hub-maintainer/
│           └── SKILL.md
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   └── revision.md
│   ├── workflows/
│   │   └── validate.yml
│   └── pull_request_template.md
├── catalog/
│   ├── angular-cli-mcp.yaml
│   ├── angular-skills.yaml
│   ├── cambio-controlado.yaml
│   ├── change-impact-analysis.yaml
│   ├── chrome-devtools.yaml
│   ├── cloudflare-mcp.yaml
│   ├── cloudflare-skills.yaml
│   ├── codex-skill-creator.yaml
│   ├── codex-skill-evals.yaml
│   ├── codex-skill-installer.yaml
│   ├── context7.yaml
│   ├── descubrimiento.yaml
│   ├── domain-discovery.yaml
│   ├── github-mcp.yaml
│   ├── hub-maintainer.yaml
│   ├── modern-web-guidance.yaml
│   ├── playwright-mcp.yaml
│   ├── project-bootstrap.yaml
│   ├── supabase-mcp.yaml
│   └── supabase-skills.yaml
├── docs/
│   ├── agentes.md
│   ├── arquitectura.md
│   ├── autoria.md
│   ├── catalogo-y-perfiles.md
│   ├── informe-0.1.0.md
│   ├── inicio-rapido.md
│   ├── mantenimiento.md
│   ├── pruebas.md
│   └── roadmap.md
├── examples/
│   └── escenarios.md
├── mcp/
│   ├── angular.codex.example.toml
│   ├── README.md
│   └── supabase.codex.example.toml
├── profiles/
│   ├── angular-frontend.yaml
│   ├── angular-supabase-cloudflare.yaml
│   ├── business-discovery.yaml
│   ├── generic-web.yaml
│   └── python-ai.yaml
├── schemas/
│   ├── capability.schema.json
│   ├── profile.schema.json
│   └── skill.schema.json
├── scripts/
│   └── hub.py
├── skills/
│   ├── change-impact-analysis/
│   │   └── SKILL.md
│   ├── domain-discovery/
│   │   └── SKILL.md
│   └── project-bootstrap/
│       └── SKILL.md
├── templates/
│   ├── dominio.md
│   ├── impacto.md
│   └── propuesta.md
├── tests/
│   └── test_hub.py
├── workflows/
│   ├── cambio-controlado.md
│   └── descubrimiento.md
├── .gitignore
├── AGENTS.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── requirements.txt
└── SECURITY.md
```

El árbol enumera los archivos de la versión. Git mantiene sus propios metadatos en `.git/`; los archivos temporales de Python están excluidos de la distribución.

| Archivos | Finalidad |
| --- | --- |
| README, AGENTS y CHANGELOG | Entrada pública bilingüe, instrucciones permanentes y cambios de la versión. |
| CONTRIBUTING, SECURITY, LICENSE y .gitignore | Procedimiento de contribución, gestión de secretos, términos MIT para contenido propio y exclusiones locales. |
| requirements.txt, scripts/hub.py y tests/test_hub.py | Preparación del entorno, interfaz de consulta y validación, y suite de regresión. |
| Cada YAML de catalog/ | Una ficha para la capacidad del mismo ID. Incluye procedencia, requisitos, instalación, permisos, alternativas y evidencia. |
| Cada YAML de profiles/ | Selección por tecnologías y condiciones del proyecto representado por su nombre. |
| capability.schema.json, profile.schema.json y skill.schema.json | Contratos de fichas, perfiles y metadatos Agent Skills, respectivamente. |
| SKILL.md | Una entrada canónica para cada skill. El mantenedor reside en el directorio de descubrimiento compartido de los dos agentes. |
| workflows/ y templates/ | Procedimientos de descubrimiento y cambio controlado, más formatos de dominio, impacto y propuesta. |
| mcp/ y examples/ | Recetas inertes de Angular y Supabase con sus requisitos y escenarios de uso de la biblioteca. |
| docs/ | Guías de arranque, arquitectura, clientes, consulta, autoría, mantenimiento, pruebas, roadmap y esta entrega. |
| .github/ | Workflow de validación, formulario Markdown de revisión y plantilla de PR. |

## Capacidades y evidencia

| Integraciones externas | Evidencia a fecha de revisión | Pendiente |
| --- | --- | --- |
| Google Modern Web Guidance, Supabase Agent Skills, Cloudflare Skills | README en commit público y documentación del proveedor | Uso de las guías en un proyecto consumidor. |
| Angular Agent Skills | Documentación, referencia de compilación y frontmatter MIT de las dos skills, versión declarada 1.0 | Ensayo contra Angular 22. |
| Angular CLI MCP, Supabase MCP, Cloudflare MCP, GitHub MCP Server, Chrome DevTools for Agents, Microsoft Playwright MCP y Context7 | Fuentes primarias, transporte, requisitos y alcance de los permisos | Conexión y negociación funcional en clientes concretos. |
| Codex Skill Creator y Skill Installer | Fuentes públicas, metadatos y licencias de la distribución local. Se ejecutó el validador de Skill Creator sobre las cuatro skills | Flujo completo de creación o instalación con modelo y proyecto de destino. |
| Codex CLI para evaluación de skills | Documentación de evaluación y ayuda local de `codex exec --json`, CLI 0.169.1 | Evaluación instrumentada con JSONL y rúbrica. |

Cada ficha externa registra commit, fecha de revisión, fecha UTC del commit, indicador de archivo del repositorio y cadencia de mantenimiento. El indicador de GitHub y la declaración de deprecación del proveedor se valoran por separado. El código del servidor y un servicio alojado pueden evolucionar de forma independiente.

| Skill propia | Resultado implementado | Verificación |
| --- | --- | --- |
| project-bootstrap | Inventario y propuesta justificada por perfil, condiciones y permisos | Metadatos y ensayo de lectura explícita con Codex. |
| domain-discovery | Ficha con actores, proceso, reglas, excepciones, hipótesis y preguntas | Metadatos y ejemplo de salida cualitativa documentado. |
| change-impact-analysis | Clasificación, matriz de impacto, regresiones, pruebas y recuperación | Metadatos y escenario de contrato RPC. |
| hub-maintainer | Auditoría y propuesta por recurso, con referencias y criterios de decisión | Metadatos y descubrimiento configurado por proyecto. |

Los cinco perfiles funcionales son `angular-supabase-cloudflare`, `angular-frontend`, `python-ai`, `generic-web` y `business-discovery`. Las pruebas ejercitan la selección por defecto para ambos agentes y los límites ante dependencias, condiciones, conflictos o agentes incompatibles.

## Resultados comprobados localmente

- `validate` informó 20 capacidades, cinco perfiles y cuatro skills propias. La suite de **20 pruebas** pasó en Windows con Python 3.13.5, PyYAML 6.0.2 y jsonschema 4.23.0.
- Se ejecutaron **18 comandos distintos** de la CLI publicados en el README, las guías y los escenarios. Todos devolvieron el código de salida esperado, incluido el rechazo de una combinación no aplicable.
- El validador de skills integrado en Codex aceptó los cuatro directorios. Un ensayo de `project-bootstrap` detectó una selección innecesaria al confundir plataforma existente con cambio de alojamiento. Tras ajustar la instrucción, el segundo ensayo seleccionó cinco capacidades para la RPC y descartó Cloudflare y los MCP remotos.
- Se analizaron ambos ejemplos TOML y los controles de sólo lectura, alcance de proyecto y marcador de posición. En el YAML de CI se comprobaron los eventos de PR/push, permisos de lectura, checkout fijado por SHA y credenciales no persistentes.
- En una simulación local de CI, el validador de confianza aceptó un árbol candidato con un script centinela que fallaría si se ejecutara. Rechazó después un perfil incompleto. También se probó en un proyecto temporal la copia documentada de una skill y se comprobó la igualdad de su contenido.
- Se revisó el inventario público y se buscaron patrones comunes de claves privadas, tokens y rutas personales. La búsqueda no encontró coincidencias. No se añadieron credenciales ni se iniciaron servidores MCP.

## Límites y próximos pasos

Las convenciones de Codex y Antigravity se contrastaron con sus manuales. La carga automática en un proyecto consumidor, una sesión interactiva de Antigravity y las sesiones de MCP siguen pendientes. GitHub Actions está preparado para el primer PR tras la publicación autorizada; su resultado alojado no se ha observado. El indicador de revisión documental tampoco garantiza la vigencia futura de un servicio.

Para 0.2.0 se propone verificar primero descubrimiento e invocación con versiones concretas de ambos clientes; después, ensayar un MCP local de lectura con datos sintéticos. La detección programada de cambios quedaría limitada a producir un informe para revisión humana. Los criterios y prioridades se detallan en el [roadmap](roadmap.md).
