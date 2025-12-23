import os
import re
from typing import Tuple
from src.alphabet import alphabet


def log(*args):
    print("--- LOG START ---")
    for arg in args:
        print(arg)
    print("---  LOG END  ---")


class Note:
    def __init__(self, uid, deck, front, back):
        self.uid = uid
        self.deck = deck
        self.front = front
        self.back = back


def get_notes() -> list[Note]:
    """
    Returns a list of notes.
    """
    notes = []
    with open("Lernen.txt", "r") as text_file:
        lines = text_file.readlines()
        for line in lines:
            fields = line.split("\t")
            if len(fields) == 1:
                continue
            uid = fields[0]
            deck = fields[1]
            front = fields[2] + fields[6]
            back = fields[3]
            notes.append(Note(uid, deck, front, back))
    return notes


def to_roman(count: int) -> str:
    """
    Takes an integer up to 10 and returns its
    representation as a roman numeral.
    """
    romans = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "iix", "ix", "x"]
    result = "(" + romans[count - 1] + ")"
    return result


def generate_numbering(count: int, numbering: str) -> str:
    """
    Returns the correct string representation of
    count in the given numbering.
    """
    match numbering:
        case "alph":
            return chr(ord("a") - 1 + count)
        case "roman":
            return to_roman(count)
        case _:
            return str(count) + ")"


def preprocess_numbering(text: str) -> str:
    r"""
    Takes text and returns the processed text.

    It works like this: we go through the text and each time
    we meet a \begin{...}[label=...], we set the numbering
    accordingly and also start at 1.

    This assumes that there are no nested environments.
    """
    accum = ""
    numbering = ""
    count = 0
    counting = False
    partition = text.split(r"\item")
    for part in partition:
        if counting:
            count += 1
        if r"\end{numbering}" in part:
            counting = False
        if r"\begin{enumerate}" in part:
            counting = True
            count = 0
            if r"\alph*)" in part:
                numbering = "alph"
            elif r"(\roman*)" in part:
                numbering = "roman"
            else:
                numbering = "arabic"
        accum = (
            accum + generate_numbering(count, numbering) + part
            if part != partition[0]
            else accum + part
        )
    return accum


def preprocess_notes(notes: list[Note]):
    r"""
    Takes a list of notes and returns a list of notes
    where each \item has been substituted for the correct
    numbering.

    """
    new_notes = []
    for note in notes:
        note.back = preprocess_numbering(note.back)
        new_notes.append(note)
    return new_notes


def get_svg_file_paths() -> list[str]:
    """
    Returns a list of file paths to all
    svg files in ./svgs.
    """
    paths = []
    dir_path = "./svgs"
    directory = os.fsencode(dir_path)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        file_path = dir_path + "/" + filename
        paths.append(file_path)
    return paths


def parse_svg_file(file):
    """
    Takes a file object and returns a list of
    parsed href attributes in any found use tag.

    #g1-54 -> 54.
    """
    ids = []
    lines = file.readlines()
    for line in lines:
        if "use" in line:
            hrefs = re.findall(r'href="#g[0-9]{1}-[0-9]+"', line)
            if len(hrefs) != 1:
                raise ValueError("There should be exactly one href.")
            href = hrefs[0]
            split = href.split("-")
            """
            Cut off the last ".
            """
            id = split[1][:-1]
            ids.append(id)
    return ids


def get_sym_from_id(id: str) -> str:
    """
    Takes an id and returns the associated symbol.
    """
    for key in alphabet.keys():
        if id in alphabet[key]:
            return key
    return ""


def get_id_from_sym(sym: str) -> list[str]:
    """
    Takes a symbol and returns a list of associated ids.
    """
    return alphabet[sym]


def translate_from_ids(ids: list[str]) -> list[str]:
    """
    Takes a list of ids and return a list of symbols
    associated with each id.
    """
    symbols = []
    for id in ids:
        sym = get_sym_from_id(id)
        if sym != "":
            symbols.append(sym)
    """
    This is a special case because my card template adds 
    two points at the end.
    """
    if len(symbols) >= 2 and symbols[-1] == "." and symbols[-2] == ".":
        symbols = symbols[:-2]
    return symbols


def translate_to_ids(symbols: list[str]) -> list[str]:
    """
    Takes a list of symbols and returns a list of lists
    of ids associated with each symbol.
    """
    ids = []
    for sym in symbols:
        ids.append(get_id_from_sym(sym))
    return []


def matches(symbols: list[str], text: str) -> bool:
    """
    This takes a symbol list and a text and returns True if all
    symbols in that list occurr in text in that specific order.
    """
    symbols_left = symbols.copy()

    for char in text:
        print(f"char: {char}, sym: {symbols_left[0]}")
        if char == symbols_left[0]:
            symbols_left.pop(0)
        if symbols_left == []:
            return True
    return False


def get_matching_note(symbols: list[str], notes: list[Note]) -> Tuple[str, str]:
    """
    The heart of the search process.
    This should return the uid of the matching note and the field, so front or back.
    """
    for note in notes:
        if matches(symbols, note.front):
            return (note.uid, "front")
        elif matches(symbols, note.back):
            return (note.uid, "back")
    raise ValueError("This svg does not match any field, but it should!")


if __name__ == "__main__":
    """
    First all svg paths and notes are fetched. The notes also
    go through a little preprocessing.

    Then this does the following for every svg file in svgs:

    1. All use tags are parsed for their href attribute
    which is further parsed to get the ascii 'id' the symbol.

    2. The id list is translated into the corresponding
    symbols using the translation table in alphabet.py.

    3. Using this symbollist, the (hopefully) unique anki note is found
    by making sure that all symbols in the symbol are contained by
    the plain text representation of that card and in the right order.
    This note and field is returned in tuple format: (uid, field).

    4. The svg is written into a directory which has the uid as the name
    and the svg is renamed to front or back and moved into the directory.
    This dir might exist already, but it does not have to.
    """
    paths = get_svg_file_paths()
    notes = get_notes()
    notes = preprocess_notes(notes)
    for path in paths:
        with open(path, "r") as file:
            ids = parse_svg_file(file)
            symbols = translate_from_ids(ids)
            print(symbols)
            matching_note = get_matching_note(symbols, notes)
            break
