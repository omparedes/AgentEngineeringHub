# Cambio controlado en una aplicación existente

**Entrada.** Petición concreta, comportamiento reproducible y versión o referencia de partida.

1. Aplica `change-impact-analysis` y completa el [análisis de impacto](../templates/impacto.md). Un recorrido de petición a almacenamiento establece qué consumidores deben probarse.
2. Para un cambio menor verifica el área afectada. Para uno funcional prueba regla, excepción y regresión. Para uno crítico ensaya datos históricos, convivencia entre versiones, permisos y recuperación en un entorno de prueba.
3. Presenta el orden de cambios con una señal de aceptación y una de parada por fase. Si restaurar código deja datos incompatibles, describe la compensación o restauración y cómo verificarla.
4. Registra quién revisó las pruebas y quién puede autorizar despliegue. El procedimiento del Hub entrega evidencia y una decisión pendiente; el equipo propietario controla su despliegue.

**Salida observable.** Un revisor puede repetir las pruebas y decidir si el cambio se despliega, se corrige o se pospone.

## Modernización frontend

Aplica esta variante cuando un cambio autorizado afecte una interfaz existente. Para consultas puntuales usa la búsqueda de guías. Para una revisión amplia solicitada, autoriza primero el directorio del escaneo.

1. Identifica framework y versiones, límites entre servidor y cliente, recorrido afectado, navegadores objetivo y restricciones de accesibilidad y rendimiento.
2. Selecciona [Modern Web Guidance](../docs/modern-web-guidance.md) con `trabajo-frontend` y consulta una guía por necesidad. Si corresponde un escaneo, delimita la ruta y conserva los candidatos para revisión.
3. Contrasta cada guía o hallazgo con la implementación vigente. Aplica los criterios `keepWhen` y `dropWhen`, confirma Baseline y conserva los fallbacks que requiere el proyecto.
4. Usa `change-impact-analysis` para registrar componentes y usuarios afectados, regresiones de comportamiento, impacto en navegadores antiguos y reversión.
5. Propón cambios concretos con sus beneficios, riesgos, alternativas y pruebas. Fija criterios observables, como navegación por teclado o una métrica tomada antes y después bajo las mismas condiciones.
6. Implementa el alcance aprobado en el consumidor. Mantén los contratos del framework y comprueba el comportamiento con y sin la mejora progresiva.
7. Ejecuta TypeScript, lint y build según el proyecto. Comprueba el recorrido visual, accesibilidad, compatibilidad y regresiones con los navegadores objetivo. Usa Playwright para recorridos repetibles o Chrome DevTools para medidas cuando estén disponibles.
8. Registra la guía y su versión, el cambio aplicado, los resultados de prueba y los pendientes en el [análisis de impacto](../templates/impacto.md). Si el proveedor cambió su orientación, usa `hub-maintainer` para revisar la ficha con esa evidencia.
