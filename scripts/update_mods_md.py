import os
import glob
import re
import tomllib

MODS_DIR = "mods"
README_PATH = "README.md"
START_TAG = "<!-- MODS_START -->"
END_TAG = "<!-- MODS_END -->"

def generate_markdown_table():
    mods = []
    
    # Przeszukaj katalog mods w poszukiwaniu plików .pw.toml (dla Packwiz)
    for toml_path in sorted(glob.glob(os.path.join(MODS_DIR, "*.pw.toml"))):
        with open(toml_path, "rb") as f:
            data = tomllib.load(f)
            name = data.get("name", os.path.basename(toml_path))
            filename = data.get("filename", "")
            side = data.get("side", "both")
            
            # Próba wyciągnięcia linku do CurseForge lub Modrinth
            url = None
            update_data = data.get("update", {})
            if "modrinth" in update_data:
                mod_id = update_data["modrinth"].get("mod-id")
                if mod_id:
                    url = f"https://modrinth.com/mod/{mod_id}"
            elif "curseforge" in update_data:
                project_id = update_data["curseforge"].get("project-id")
                if project_id:
                    url = f"https://www.curseforge.com/projects/{project_id}"
            
            name_cell = f"[{name}]({url})" if url else name
            mods.append((name_cell, filename, side))

    # Budowa tabeli Markdown
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