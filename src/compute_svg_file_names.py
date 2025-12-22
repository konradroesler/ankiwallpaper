import sqlite3
import hashlib
import html
import re

DB_PATH = r"/home/konrad/.local/share/Anki2/User 1/collection.anki2"

PREAMBLE = r"""\documentclass[12pt]{article}
\special{papersize=3in,5in}
\usepackage[utf8]{inputenc}
\usepackage{amssymb,amsmath}
\usepackage{bbold,enumitem}
\usepackage{mathrsfs}
\pagestyle{empty}
\setlength{\parindent}{0in}
\begin{document}"""


# Function to compute Anki-style LaTeX SVG filename
def latex_to_svg_filename(latex_code, preamble=PREAMBLE):
    # Normalize line endings
    latex_code = latex_code.replace("\r\n", "\n").replace("\r", "\n")
    # Combine preamble + code + end document
    full_code = preamble + latex_code + r"\end{document}"
    # Compute MD5 hash
    md5_hash = hashlib.md5(full_code.encode("utf-8")).hexdigest()
    return f"latex-{md5_hash}.svg"


# Connect to the SQLite database
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Get the field names from the 'notetypes' table
cur.execute("SELECT id, fldnames FROM notetypes")
notetype_fields = {row[0]: row[1].split("\x1f") for row in cur.fetchall()}

# Query notes
cur.execute("SELECT id, mid, flds FROM notes")
notes = cur.fetchall()

# Regex to extract LaTeX snippets (inline \(..\), \[..\], or $$..$$)
latex_pattern = re.compile(r"(\\\(.*?\\\)|\\\[.*?\\\]|(?<!\$)\${2}.*?\${2})", re.DOTALL)

mapping = []

for note_id, notetype_id, flds in notes:
    fields = flds.split("\x1f")
    field_names = notetype_fields.get(notetype_id, [])
    for i, content in enumerate(fields):
        field_name = field_names[i] if i < len(field_names) else f"Field{i}"
        content = html.unescape(content)
        matches = latex_pattern.findall(content)
        for latex_code in matches:
            svg_filename = latex_to_svg_filename(latex_code)
            mapping.append(
                {
                    "note_id": note_id,
                    "field_name": field_name,
                    "latex": latex_code,
                    "svg_filename": svg_filename,
                }
            )

# Output results
for entry in mapping:
    print(
        f"Note {entry['note_id']} | Field '{entry['field_name']}' | SVG: {entry['svg_filename']}"
    )
    print(f" LaTeX: {entry['latex']}\n")

conn.close()
