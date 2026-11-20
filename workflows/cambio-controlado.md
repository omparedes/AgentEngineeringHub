# Cambio controlado en una aplicación existente

**Entrada.** Petición concreta, comportamiento reproducible y versión o referencia de partida.

1. Aplica `change-impact-analysis` y completa el [análisis de impacto](../templates/impacto.md). Un recorrido de petición a almacenamiento establece qué consumidores deben probarse.
2. Para un cambio menor verifica el área afectada. Para uno funcional prueba regla, excepción y regresión. Para uno crítico ensaya datos históricos, convivencia entre versiones, permisos y recuperación en un entorno de prueba.
3. Presenta el orden de cambios con una señal de aceptación y una de parada por fase. Si restaurar código deja datos incompatibles, describe la compensación o restauración y cómo verificarla.
4. Registra quién revisó las pruebas y quién puede autorizar despliegue. El procedimiento del Hub entrega evidencia y una decisión pendiente; el equipo propietario controla su despliegue.

**Salida observable.** Un revisor puede repetir las pruebas y decidir si el cambio se despliega, se corrige o se pospone.
