# Validar una contribución

Con las dependencias de desarrollo disponibles, ejecuta desde la raíz:

```console
python scripts/hub.py validate
python -m unittest discover -s tests -v
```

El resultado esperado es un resumen `OK` de la biblioteca y otro de unittest. Los ensayos no necesitan navegador, modelo, cuenta GitHub ni proyecto cloud. El entorno temporal de Python debe admitir crear y eliminar directorios. En Windows se comprobó con Python 3.13; la CI declara Ubuntu 24.04.

## Cobertura

El [validador](../scripts/hub.py) comprueba los contratos, IDs de archivos, entradas locales, correspondencia de las skills y metadatos, referencias Markdown relativas, condiciones del perfil, stack requerido, dependencias y ciclos. El selector verifica también conflictos entre opciones pedidas y el agente elegido. Los enlaces HTTPS externos se revisan documentalmente, sin peticiones desde el validador.

La [suite](../tests/test_hub.py) cubre datos válidos, campo obligatorio ausente, clave duplicada, YAML con alias, ID repetido entre formatos, fecha imposible, incompatibilidad de agente o stack, opciones no aplicables, dependencia transitiva, conflicto indirecto, ciclo, enlace roto y errores desde la CLI. Los fixtures temporales no cambian las fichas distribuidas.

```console
python scripts/hub.py recommend angular-frontend --include supabase-mcp
```

Este control negativo debe terminar con código 1 y la razón `no aplicable`. Corrige el perfil o el objetivo real antes de cambiar una exclusión.

## Qué prueba GitHub Actions

La [CI](../.github/workflows/validate.yml) se activa en PR y en push a main. En PR obtiene la base por SHA y el árbol combinado del cambio en directorios distintos. Ejecuta scripts y tests de la base revisada, y aplica ese validador a los datos propuestos. No importa módulos Python de la contribución. El checkout oficial está fijado por SHA, el token tiene lectura y se descartan sus credenciales. El runner instala los paquetes Python firmados de Ubuntu. El workflow no establece sesiones MCP ni despliega.

Los cambios a scripts, esquemas, pruebas o CI requieren revisión de código. Antes de integrar, un mantenedor puede ejecutar la suite de la propuesta en un entorno desechable tras revisarla. El push a main ejecuta la suite de la versión integrada. Activa en GitHub la aprobación de workflows de colaboradores externos y protege main con revisión del PR y el check `validate`. Estas opciones del alojamiento requieren que exista el remoto.

## Ensayos de comportamiento

Para una skill nueva utiliza un caso sintético con un resultado observable. Ejemplo: con una RPC que usa un móvil antiguo, la propuesta debe mencionar retrocompatibilidad, identificar una prueba de contrato y justificar si necesita acceso remoto. Guarda el prompt, agente, referencia, salida saneada y juicio del revisor. La [ficha de evaluación Codex](../catalog/codex-skill-evals.yaml) describe una modalidad JSONL para evaluaciones autorizadas con modelo. Los escenarios cualitativos complementan la suite determinista.
