---
name: domain-discovery
description: Convierte entrevistas, documentos y ejemplos de un proceso de negocio en actores, reglas, excepciones y requerimientos trazables antes del diseño.
license: MIT
---

# Descubrir el dominio

1. Define con el solicitante el proceso, su inicio, su fin y la decisión que necesita tomar. Distingue a quienes piden o deciden del personal que opera cada paso. Identifica quién autoriza, recibe el resultado o puede aclarar una excepción. Usa roles y fuentes saneadas.
2. Reconstruye un caso normal de principio a fin. En cada paso registra actor, entrada, acción, regla, dato que cambia y salida observable. Pregunta por un caso real de excepción, el tratamiento actual y su coste o problema. Si faltan testimonios, deja el paso abierto.
3. Separa estado actual, problema y resultado deseado. Asigna IDs estables a evidencia, reglas y requisitos. Por afirmación conserva fuente, fecha si se conoce y estado (confirmada, hipótesis o por resolver). Un desacuerdo conserva ambas fuentes y la persona o rol que puede resolverlo.
4. Transforma sólo necesidades respaldadas en requisitos verificables. Asocia actor, regla, criterio observable y excepción. Formula los supuestos como preguntas cuya respuesta pueda cambiar el alcance. Una propuesta técnica no es evidencia de negocio.
5. Devuelve una ficha reutilizable con alcance, mapa de actores, proceso, reglas y excepciones, problemas, requisitos, supuestos y preguntas priorizadas. Señala qué se puede diseñar y qué depende de validación. Si el paso siguiente es consolidar entrevistas o ideas, conserva sus IDs y decisiones para el backlog. Si se solicita guardarla, utiliza el destino autorizado y usa sólo referencias saneadas en artefactos públicos. Compartir material externamente requiere una instrucción expresa.

## Ejemplo

Una entrevista dice «los supervisores suelen aprobar las devoluciones grandes». Registra la práctica y su fuente. Deja sin confirmar el umbral, la moneda y si la aprobación es obligatoria. Pregunta quién los define y qué ocurrió en la última devolución fuera de horario. El criterio de aceptación del umbral queda pendiente.
