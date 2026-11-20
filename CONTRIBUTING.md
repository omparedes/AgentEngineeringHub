# Contribuir

Puedes proponer una herramienta, corregir una ficha, aportar un caso reproducible o mejorar un procedimiento. Para una integración externa abre una [revisión de capacidad](.github/ISSUE_TEMPLATE/revision.md) con fuente primaria, utilidad, alternativa existente y riesgo. Las sugerencias comunitarias usan el mismo contrato y conservan su procedencia.

1. Crea una rama de trabajo para el cambio. Usa el ID existente cuando la función siga siendo la misma.
2. Sigue la [guía de autoría](docs/autoria.md). Mantén juntos datos, evidencia y el ejemplo que cambie. Para rediseños de esquema explica cómo seguirá funcionando el contenido anterior.
3. Ejecuta `python scripts/hub.py validate` y `python -m unittest discover -s tests -v`. Adjunta resultados reales y anota los clientes pendientes.
4. Prepara el PR con la [plantilla](.github/pull_request_template.md), el Issue relacionado y la referencia examinada. El revisor comprueba la procedencia, permisos y calidad de las pruebas antes de integrar.

Aporta sólo contenido original que puedas distribuir bajo [MIT](LICENSE) o referencias con su licencia identificada. Conserva licencias y atribución de terceros. Para asuntos sensibles utiliza la [política de seguridad](SECURITY.md).
