# Recetas de conexión por proyecto

Estos archivos son ejemplos inertes. Para elegir un MCP consulta primero `python scripts/hub.py list --type mcp` y su ficha con `show ID`. Para ensayar una receta se necesita autorización para ese proyecto y cliente.

| Receta | Requisitos | Comprobación tras activación explícita |
| --- | --- | --- |
| [Angular CLI local para Codex](angular.codex.example.toml) | Proyecto POSIX con @angular/cli ya instalado; comprueba en su ayuda que admite mcp, --local-only y --read-only. | Listar los proyectos del workspace y contrastarlos con angular.json. |
| [Supabase de desarrollo para Codex](supabase.codex.example.toml) | Proyecto de prueba elegido, identificador público en lugar de PROJECT_REF, autorización OAuth del cliente. | Confirmar proyecto y lista de herramientas habilitadas antes de cualquier consulta. |

En Codex combina la sección elegida con la configuración `.codex/config.toml` del **proyecto de confianza**. Conserva las demás secciones existentes. Para Angular en Windows puedes apuntar el comando a `node` y pasar la ruta del `bin/ng.js` del paquete local como primer argumento tras verificarla en su package.json. Revisa las opciones contra la versión de Angular CLI del lockfile. [Codex MCP](https://developers.openai.com/codex/mcp/) · [Angular CLI MCP](https://angular.dev/ai/mcp)

En Antigravity CLI, el ámbito de workspace utiliza `.agents/mcp_config.json`. Para una conexión stdio define una entrada en `mcpServers` con `command` y `args`; toma el binario del proyecto verificado y los mismos argumentos de sólo lectura. Supervisar el primer arranque permite comprobar las herramientas anunciadas sin entregar credenciales. Consulta la sección correspondiente a tu superficie para servidores remotos. [Antigravity MCP](https://antigravity.google/docs/mcp)

Supabase admite acotar proyecto, grupos y lectura mediante parámetros de URL. El usuario completa la autorización en el cliente. Los tokens o sesiones se conservan en su almacén seguro. La guía pública y las migraciones locales suelen bastar cuando la tarea es de diseño. [Supabase MCP](https://supabase.com/docs/guides/ai-tools/mcp)

Para retirar una prueba, elimina sólo la entrada local correspondiente, reinicia el cliente y, si se concedió acceso remoto, revoca la autorización en el proveedor. Ningún comando de consulta del Hub inicia estos servidores.
