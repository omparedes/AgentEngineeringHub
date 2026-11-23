# Inicio rápido

Abre la raíz del checkout, donde están `README.md` y `scripts/`. Necesitas Python 3.11+ con `venv`. Si ya puedes importar `yaml` y `jsonschema`, puedes pasar a la primera consulta.

## Preparación por proyecto

Estos comandos crean `.venv/` dentro del Hub. La instalación inicial de dependencias puede requerir PyPI o un repositorio local de ruedas. No instala Codex, herramientas npm ni servidores MCP. Activa el entorno en esa terminal antes de usar `python` en las demás guías.

**Windows PowerShell**

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\Activate.ps1
```

Si tu política de PowerShell limita la activación, usa `.\.venv\Scripts\python.exe` en lugar de `python` para todas las consultas. No hace falta cambiar la política del equipo.

**Linux o macOS**

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
. .venv/bin/activate
```

Con un almacén de ruedas ya preparado, usa el Python del entorno y `python -m pip install --no-index --find-links RUTA_A_RUEDAS -r requirements.txt`. PyYAML interpreta los datos YAML y jsonschema valida sus contratos. La suite utiliza unittest, incluido en Python.

## Primera consulta

```console
python scripts/hub.py validate
python scripts/hub.py profiles
python scripts/hub.py list --type mcp --tech angular
python scripts/hub.py show angular-cli-mcp
python scripts/hub.py recommend business-discovery --agent antigravity
```

El validador informa 27 capacidades, cinco perfiles y cuatro skills propias en este árbol. El filtro devuelve `angular-cli-mcp` y la ficha muestra los límites de lectura del CLI. El último comando selecciona `domain-discovery` antes de `descubrimiento` por su dependencia. Las consultas funcionan con datos locales.

Si el resultado no coincide, comprueba que ejecutaste desde la raíz y que el intérprete pertenece a tu entorno. Un ID mal escrito o una combinación incompatible produce un mensaje en stderr y código de salida distinto de cero. Continúa con los [ejemplos completos](../examples/escenarios.md).
