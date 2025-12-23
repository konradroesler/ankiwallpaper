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


def parse_svg_file(file) -> list[str]:
    """
    Takes a file object and returns a list of
    parsed href attributes in any found use tag.

    For example: #g1-54 -> 54.
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


def get_possible_symbols_from_id(id: str) -> list[str]:
    """
    Takes an id and returns a list of symbols
    that might be associated to that id.
    """
    keys = []
    for key in alphabet.keys():
        if id in alphabet[key]:
            keys.append(key)
    return keys


def generate_symbol_filter(ids: list[str]) -> list[list[str]]:
    """
    Takes a list of ids and returns symbol filter.

    A symbol is a list of symbol sets (lists), where
    a symbol set means intuitively: we are looking for
    one of the symbols in the set, but it does not matter
    which one is found.
    """
    symbol_filter = []
    for id in ids:
        possible_symbols = get_possible_symbols_from_id(id)
        if possible_symbols != []:
            symbol_filter.append(possible_symbols)
    """
    This is a special case because my card template adds 
    two points at the end.
    """
    if (
        len(symbol_filter) >= 2
        and "." in symbol_filter[-1]
        and "." in symbol_filter[-2]
    ):
        symbol_filter = symbol_filter[:-2]
    return symbol_filter


def matches(symbol_filter: list[list[str]], text: str) -> bool:
    """
    This takes a symbol filter and a text and returns True if
    that symbol filter runs through succesfully, meaning that
    is is emptied. The filter gets emptied by matching every
    entry in the filter, meaning that there is a way we can
    pick symbols where the filter has more than one possible
    symbol, and have that choosen sequence of symbols be
    contained in the text the order specified by the filter.
    """

    symbols_left = symbol_filter.copy()

    for char in text:
        if char in symbols_left[0]:
            symbols_left.pop(0)
        if symbols_left == []:
            return True
    return False


def get_matching_note(symbols: list[list[str]], notes: list[Note]) -> Tuple[str, str]:
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

    2. Each id is translated into a list of symbols according to the
    alphabet, where each symbol in this list could be the symbol
    associated to that id. This mechanic arises since the same id
    might be generated by multiple symbols.

    3. Using this symbollist, the (hopefully) unique anki note is found
    by making sure that all symbols in the symbollist are contained by
    the plain text representation of that card and in the right order.
    Entries in the symbollist where the list has more than one entry,
    i.e. ['.', ':'] means next we are looking for '.' OR ':'.
    The correct note's uid and field (front/back) are returned in tuple
    format: (uid, field).

    TODO
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
            symbol_filter = generate_symbol_filter(ids)
            matching_note = get_matching_note(symbol_filter, notes)
            print(matching_note)
