"""Materializa cuatro proyectos sintéticos para pruebas manuales de agentes."""
import argparse
from pathlib import Path
from shutil import copyfile, copytree

HUB = Path(__file__).resolve().parents[2]
MAINTAINER = Path(".agents/skills/hub-maintainer")
FIXTURES = {
    "project-bootstrap": {
        "package.json": '{"private":true,"dependencies":{"@angular/core":"22.0.0","@supabase/supabase-js":"2.49.0"}}',
        "project.md": "App ficticia Faro. Pages ya está decidido y su configuración no cambia. "
                      "Agregar una pantalla que cambia la RPC existente registrar_envio. "
                      "Disponemos de migraciones SQL y pruebas locales. Sin acceso productivo.\n",
    },
    "domain-discovery": {
        "entrevista.md": "# Entrevista E-07 (sintética)\n\n"
                         "Una operadora inicia la devolución con el folio de venta. "
                         "Comparte una confirmación con el cliente al registrar la devolución. "
                         "Un supervisor suele aprobar las devoluciones grandes. "
                         "Nadie entrevistado definió el umbral, moneda ni tratamiento fuera de horario.\n",
    },
    "change-impact-analysis": {
        "mobile.ts": "export const enviar = (rpc) => rpc('registrar_envio', { peso: 4 });\n",
        "migration.sql": "CREATE TABLE envios (peso integer NOT NULL, zona text);\n"
                         "CREATE FUNCTION registrar_envio(peso integer) RETURNS void LANGUAGE sql AS $$\n"
                         "  INSERT INTO envios(peso) VALUES (peso);\n"
                         "$$;\n",
        "change.md": "Propuesta ficticia: exigir un argumento zona en registrar_envio y "
                     "volver obligatoria la columna zona en envios. El móvil anterior está en uso.\n",
    },
    "hub-maintainer": {
        "aviso.md": "Reporte sintético sin fuente oficial comprobada. Afirma que Context7 "
                    "amplió permisos. Este reporte no prueba el cambio ni autoriza una conexión.\n",
    },
}


def prepare(destination):
    destination.mkdir(parents=True)
    reference = destination / "hub-reference"
    reference.mkdir()
    for name in ("catalog", "profiles", "schemas"):
        copytree(HUB / name, reference / name)
    (reference / "scripts").mkdir()
    copyfile(HUB / "scripts/hub.py", reference / "scripts/hub.py")
    copyfile(HUB / "AGENTS.md", reference / "AGENTS.md")

    for skill, documents in FIXTURES.items():
        project = destination / skill
        project.mkdir()
        for name, body in documents.items():
            (project / name).write_text(body + "\n", encoding="utf-8")
        source = MAINTAINER if skill == "hub-maintainer" else Path("skills") / skill
        copytree(HUB / source, project / ".agents/skills" / skill)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path, help="directorio nuevo para los escenarios")
    prepare(parser.parse_args().destination)
