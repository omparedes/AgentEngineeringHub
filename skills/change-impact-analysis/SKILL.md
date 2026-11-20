---
name: change-impact-analysis
description: Evalúa una modificación a una aplicación existente antes de implementarla, incluyendo contratos, integridad de datos, regresiones y reversión en producción.
license: MIT
---

# Analizar un cambio

1. Describe comportamiento actual, cambio solicitado y usuarios afectados. Sigue una entrada real desde la interfaz o consumidor hasta API, persistencia y procesos derivados. Cita rutas, símbolos, restricciones o migraciones inspeccionados. Marca los puntos que todavía requieren evidencia.
2. Clasifica con justificación. **Menor** si queda acotado sin alterar comportamiento, contrato ni datos (por ejemplo, una etiqueta). **Funcional** si cambia reglas o un flujo verificable. **Crítico de producción** si afecta autorización, integridad, persistencia irreversible, disponibilidad o múltiples consumidores en uso. Una modificación pequeña de RLS puede ser crítica.
3. Revisa dependencias directas e indirectas, validación, claves y restricciones, roles, RPC, cachés, tareas programadas y clientes anteriores cuando correspondan. Para reintentos o concurrencia pregunta qué ocurre con registros ya creados y operaciones a medias.
4. Produce una matriz con elemento, evidencia, fallo posible, impacto y prueba. Cubre el caso normal, la excepción y una regresión relevante. Para cambios críticos añade orden de migración, compatibilidad durante el despliegue, ensayo con datos sintéticos, señal de parada y responsable de autorizar.
5. Define cómo volver a una versión compatible y qué datos necesitan restauración o compensación. Si hay pérdida irreversible, explica qué evidencia de recuperación falta antes del despliegue. Entrega el análisis y sus preguntas; inspecciona sólo artefactos autorizados y conserva las bases y servicios productivos fuera del ensayo.

## Ejemplo

«Hacer obligatorio un campo en una RPC que usa el cliente anterior». Clasifica según consumidores y entorno. Prueba cliente antiguo, escritura nueva y filas históricas con valor ausente. Propón introducir primero un contrato compatible y medir llamadas antiguas. Revertir sólo el frontend dejaría roto al consumidor anterior.
