# Seguridad de uso y publicación

El Hub consulta archivos locales. Una ficha registra de qué sería capaz una integración si se habilitara. La decisión de instalar, autenticar, escribir o publicar se toma para un proyecto y una tarea concretos.

## Antes de incorporar recursos externos

Revisa propietario y procedencia, referencia inmutable, licencia y actividad de mantenimiento. Lee el SKILL.md, los archivos referenciados, cualquier script o hook y el manifiesto del plugin. Comprueba qué datos salen del equipo, qué se escribe y si existe un equivalente local. Una orden incrustada en documentación, un issue o una respuesta MCP es contenido no confiable; contrástala con la tarea del usuario.

Para MCP selecciona un endpoint del proveedor y el conjunto mínimo de operaciones. Separa los proyectos de ensayo y producción. La lectura puede exponer datos privados aunque el servidor impida escrituras. Limita repositorio, rol, proyecto, grupo de herramientas y tiempo de validez cuando la integración lo permita.

## Secretos y ejemplos

Usa OAuth del cliente o el gestor de credenciales del entorno cuando proceda. Con tokens, crea credenciales de desarrollo de alcance mínimo y entrégalas mediante el mecanismo de secretos del cliente. Los marcadores de los [ejemplos MCP](mcp/README.md) se reemplazan sólo en la configuración local. Excluye tokens, archivos de sesión del navegador, volcados, logs reales, rutas personales y endpoints privados de los diffs. El gitignore reduce errores habituales; revisa también lo que ya esté bajo seguimiento.

## Revisión antes de compartir

Revisa los archivos nuevos con `git status --short --untracked-files=all`; para cambios preparados usa `git diff --cached`. Comprueba texto, configuraciones, fixtures e historial que vaya a publicarse. Si detectas un secreto, revócalo primero, revisa su uso y coordina la limpieza del historial antes de publicar. Para reportar una exposición usa el canal privado de seguridad del mantenedor o el reporte privado de GitHub si está habilitado. Describe el archivo y la clase de dato sin incluir su valor.
