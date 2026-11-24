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

La [CI](../.github/workflows/validate.yml) se activa al abrir, actualizar o reabrir un PR y al publicar un commit en `main` o una rama candidata `release/v*-rc.*` de este repositorio. En PR obtiene por separado la base revisada y el árbol combinado. Ejecuta scripts y tests de la base y valida los datos propuestos. El checkout oficial está fijado por SHA, el token tiene lectura y se descartan sus credenciales. El runner instala los paquetes Python firmados de Ubuntu.

El push a una rama candidata ejecuta su propia suite y el push a `main` ejecuta la suite integrada. Reserva los pushes a ramas de release para cambios ya revisados por mantenedores. La ejecución del PR mantiene los scripts de la base separados de los datos aportados. Antes de cerrar una release, comprueba en Actions el evento, el SHA auditado, el resultado de los pasos y que el PR corresponde a esa revisión.

## Ensayos de comportamiento

Para una skill nueva utiliza un caso sintético con un resultado observable. Ejemplo: con una RPC que usa un móvil antiguo, la propuesta debe mencionar retrocompatibilidad, identificar una prueba de contrato y justificar si necesita acceso remoto. Guarda el prompt, agente, referencia, salida saneada y juicio del revisor. La [ficha de evaluación Codex](../catalog/codex-skill-evals.yaml) describe una modalidad JSONL para evaluaciones autorizadas con modelo. Los escenarios cualitativos complementan la suite determinista.
