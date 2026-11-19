import os
import glob
import re
import tomllib

MODS_DIR = "mods"
README_PATH = ".github/README.md"
START_TAG = "<!-- MODS_START -->"
END_TAG = "<!-- MODS_END -->"

# Ręczne mapowanie dla modów spoza Modrinth/CurseForge (klucz = nazwa pliku bez .pw.toml)
CUSTOM_URLS = {
    "jlfix": "https://github.com/BartekClk/Just-Leveling-Fixed",
}


def resolve_mod_url(toml_path: str, data: dict) -> str | None:
    slug = os.path.basename(toml_path).removesuffix(".pw.toml")
    if slug in CUSTOM_URLS:
        return CUSTOM_URLS[slug]

    update_data = data.get("update", {})
    if "modrinth" in update_data:
        mod_id = update_data["modrinth"].get("mod-id")
        if mod_id:
            return f"https://modrinth.com/mod/{mod_id}"
    elif "curseforge" in update_data:
        project_id = update_data["curseforge"].get("project-id")
        if project_id:
            return f"https://www.curseforge.com/projects/{project_id}"

    # Automatyczne wykrycie repozytorium z linku GitHub Releases w sekcji [download]
    download_url = data.get("download", {}).get("url", "")
    gh_match = re.match(r"^(https://github\.com/[^/]+/[^/]+)/releases/", download_url)
    if gh_match:
        return gh_match.group(1)

    return None


def generate_markdown_table():
    mods = []

    for toml_path in sorted(glob.glob(os.path.join(MODS_DIR, "*.pw.toml"))):
        with open(toml_path, "rb") as f:
            data = tomllib.load(f)
            name = data.get("name", os.path.basename(toml_path))
            filename = data.get("filename", "")
            side = data.get("side", "both")

            url = resolve_mod_url(toml_path, data)
            name_cell = f"[{name}]({url})" if url else name
            mods.append((name_cell, filename, side))

    lines = [
        f"\n**Łącznie modów:** {len(mods)}\n",
        "| Nazwa moda | Wersja pliku | Strona |",
        "| :--- | :--- | :---: |"
    ]
    for name_cell, filename, side in mods:
        lines.append(f"| {name_cell} | `{filename}` | `{side}` |")

    return "\n".join(lines) + "\n"


def update_readme():
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(f"{re.escape(START_TAG)}.*?{re.escape(END_TAG)}", re.DOTALL)
    table_content = f"{START_TAG}\n" + generate_markdown_table() + f"{END_TAG}"

    new_content = pattern.sub(table_content, content)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)


if __name__ == "__main__":
    update_readme()