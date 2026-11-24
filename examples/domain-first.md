# Ejemplos de Domain-First Agile Engineering

Los proyectos, fuentes y reglas de esta página son ficticios. Los ejemplos muestran decisiones y evidencias que un equipo podría registrar. [Metodología](../docs/metodologia/domain-first-agile-engineering.md)

## Sistema administrativo con varios roles

En una cooperativa ficticia, gerencia pide un tablero de anticipos. Operaciones indica en `E-01` que el problema inmediato es identificar solicitudes devueltas. Finanzas confirma en `E-02` que un solicitante nunca aprueba su propia solicitud. La cobertura de reemplazos queda pendiente. El backlog prioriza un incremento de solicitud, rechazo con motivo y nueva presentación. Asocia `RN-01` a `HU-01`, a un criterio que deniega la autoaprobación y a una prueba por rol. El prototipo cubre bandeja vacía, falta de permiso y corrección. Valídalo con operadores y finanzas antes de maquetar. Materializa la auditoría y persistencia cuando se acuerde el contrato. Aplica la variante empresarial y evalúa requisitos ASVS para datos y permisos.

## Seguimiento de órdenes de servicio técnico

Un taller ficticio recibe equipos y los asigna a técnicos. `E-03`, una observación en recepción, muestra que una orden puede esperar una pieza. El encargado todavía debe decidir quién cambia ese estado. Prioriza registrar, asignar y consultar órdenes. Presenta el estado de espera como hipótesis en el prototipo móvil y limita los fixtures a órdenes ficticias. En el segundo incremento incorpora persistencia y la transición aprobada. La prueba une el rol de recepción, la asignación del técnico y el resultado visible en la cola. Si el prototipo resuelve el estado con un boceto, basta una revisión breve.

## Sitio web o portafolio

Un estudio ficticio quiere que potenciales clientes encuentren proyectos y puedan abrir el contacto desde una pantalla estrecha. Usa la variante ligera. Registra audiencia y acción principal, bosqueja galería y contacto y valida navegación por teclado y estados sin proyectos. Emplea Stitch sólo si interesa comparar variantes visuales. Si usas su exportación, conserva las decisiones de `DESIGN.md` y adapta el resultado al framework, a la semántica y a Baseline. Entrega la galería primero y verifica navegación, contraste y carga de imágenes. Un mapa de módulos independiente sobra cuando la aplicación carece de esas dependencias.

## Modificación de una aplicación empresarial existente

Una distribuidora ficticia quiere que la RPC `registrar_envio` exija zona. El cliente móvil anterior sigue en uso. Parte del contrato actual y activa análisis de impacto. Confirma qué llamadas omiten el campo y qué filas históricas están incompletas. Planifica convivencia de contratos, validación en Preview y reversión con evidencia. El cambio afecta al backend y la persistencia. Una maquetación o una herramienta de diseño no aporta evidencia a ese alcance. La variante de mantenimiento concentra el trabajo en contratos, regresiones, datos y recuperación. [Cambio controlado](../workflows/cambio-controlado.md)

## Consultas locales del Hub

```console
python scripts/hub.py recommend business-discovery
python scripts/hub.py recommend generic-web --agent antigravity --context prototipado-visual --include google-stitch
python scripts/hub.py recommend angular-supabase-cloudflare --context cambio-existente --context cambio-sql
```

La primera consulta propone descubrimiento de dominio. La segunda incluye Stitch como opción solicitada de prototipado. La última incluye análisis de impacto, cambio controlado y revisión de SQL. Mantiene fuera las herramientas de interfaz mientras el alcance siga siendo de backend.
