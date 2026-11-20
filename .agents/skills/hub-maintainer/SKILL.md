---
name: hub-maintainer
description: Audita una ficha, una fuente nueva o una skill del Hub y prepara una decisión de mantenimiento con evidencia, impacto y pruebas.
license: MIT
---

# Revisión de una capacidad

1. Delimita el recurso y la pregunta de revisión. Lee AGENTS.md en la raíz del Hub. Busca por ID, proveedor y función con la CLI local o con búsqueda de texto en catalog/. Si otra ficha describe el mismo servidor, compara transportes, permisos y casos de uso antes de proponer un alta.
2. Conserva el valor anterior de review.reference. Si se ha autorizado consultar fuentes públicas, compara el commit o tag con el README, la licencia, los releases y el changelog del proveedor. Identifica archivos o secciones concretas y distingue el cambio del upstream de tu inferencia. Sin acceso a la fuente, registra qué queda pendiente y conserva la fecha de la última revisión efectiva.
3. Traza el impacto en perfiles, dependencias, ejemplos y permisos. Para cambios de una skill, ensaya una entrada realista y una próxima pero fuera de su alcance. Indica cómo observar que se activó correctamente y qué acción debe seguir requiriendo autorización.
4. Entrega una propuesta por recurso con evidencia anterior y nueva, estado del ciclo de revisión, campos que cambiarían, prueba necesaria y responsable de decidir. Si el cambio se descarta, deja su motivo. Una versión detectada por sí sola no acredita compatibilidad.
5. En modo auditoría devuelve el borrador de Issue o diff en la respuesta. Edita únicamente las fichas solicitadas cuando se pida implementar el cambio; entonces ejecuta el validador y las pruebas. La decisión de publicar o aprobar pertenece al mantenedor.

## Ejemplo

Entrada: «Supabase anunció nuevas herramientas de escritura. Revisa nuestra ficha».
Salida esperada: alcance del endpoint, enlace y referencia contrastados, diferencia de permisos, perfiles consumidores y prueba con proyecto desechable propuesta. Mantén runtime sin probar hasta disponer de resultados. La auditoría termina con la propuesta, sin autenticar clientes, actualizar en lote ni abrir el PR.
