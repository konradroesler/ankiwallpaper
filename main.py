import os
import re
import html
import hashlib

import anki
from anki.collection import Collection

LATEX_NEWLINES = re.compile(
    r"""(?xi)
        <br( /)?>
        |
        <div>
    """
)

HTML = re.compile(
    r"""(?si)
        (<!--.*?-->)              # wrapped text: HTML comments
        |
        (<style.*?>.*?</style>)   # style blocks
        |
        (<script.*?>.*?</script>) # script blocks
        |
        (<.*?>)                   # HTML tags
    """
)


def strip_html(latex):
    # print(f'strip_html::TOP::({latex})')
    out = LATEX_NEWLINES.sub("\n", latex)
    # print(f'strip_html::MIDDLE::({out})')
    out = HTML.sub("", out)
    # print(f'strip_html::MIDDLE::({out})')
    if "&" in out:
        out = html.unescape(out)
        out = out.replace("\u00a0", " ")
    # print(f'strip_html::BOTTOM::({out})')
    return out


def fname_for_latex(latex):
    # print(f'fname_for_latex::TOP::({latex})')
    normalized = strip_html(latex)
    # print(f'fname_for_latex::MIDDLE::({normalized})')
    digest = hashlib.sha1(normalized.encode("utf-8")).hexdigest()
    # print(f'fname_for_latex::BOTTOM::(latex-{digest}.svg)')
    return f"latex-{digest}.svg"


def get_cards() -> list[list[str]]:
    """
    Returns a list of lists where each small list contains the raw latex of the front side
    in the first entry and the raw latex of the back side in the second entry.
    """

    cards = []
    collection_path = r"/home/konrad/.local/share/Anki2/User 1/collection.anki2"
    col = Collection(collection_path)

    rows = col.db.all("SELECT flds FROM notes")
    col.close()

    for flds in rows:
        fields = flds[0].split("\x1f")
        if len(fields) != 2:
            continue
        fields[1] = fields[1] + r"\phantom\\\\.\hfill."
        cards.append([fields[0], fields[1]])
    return cards

def get_svg_file_names():
    directory_path = r"/home/konrad/.local/share/Anki2/User 1/collection.media/"
    directory = os.fsencode(directory_path)

    file_names = []

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".svg"):
            file_names.append(filename)

    return file_names 