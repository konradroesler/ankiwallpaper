import os
import re
from typing import Tuple
from src.constants import VICTORY_MSG
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

    def __str__(self):
        return f"\nNote(\n\nUID:\n{self.uid}, \n\nDECK:\n{self.deck}, \n\nFRONT:\n{self.front}, \n\nBACK\n{self.back}\n\n)"


def get_note(text: str) -> Note:
    """
    Takes a string representation of
    a note and return a Note object.
    """
    fields = text.split("\t")
    uid = fields[0]
    deck = fields[1]
    front = fields[2] + fields[6]
    back = fields[3]
    return Note(uid, deck, front, back)


def get_notes() -> list[Note]:
    """
    Returns a list of notes read from
    a (hardcoded) file.
    """
    notes = []
    with open("Lernen.txt", "r") as text_file:
        lines = text_file.readlines()
        for line in lines:
            """
            Skip lines which are not
            acutal notes.
            """
            if "\t" not in line:
                continue
            note = get_note(line)
            notes.append(note)
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
            return chr(ord("a") - 1 + count) + ")"
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


def apply_exchange_rules(text: str) -> str:
    r"""
    Some math symbols are interpreted incorrectly when
    parsing the svg, so they are converted to normal
    ascii symbols. This should work since they have the
    same id.
    When the inline and display math id's differ from each other,
    both replacement symbols get inserted.

    \implies is substituted for =), they have the same id
    \lVert and \rVert is substituted for k, they have the same id
    \exists is substituted for 9, they have the same id
    \forall is substituted for 8, they have the same id
    \in is substituted for 2, they have the same id
    """
    text = (
        text.replace(r"\implies", "=)")
        .replace(r"\to ", "!")
        .replace(r"\to}", "!")
        .replace(r"\lVert", "k")
        .replace(r"\rVert", "k")
        .replace(r"\Vert", "k")
        .replace(r"\exists", "9")
        .replace(r"\forall", "8")
        .replace(r"\rightarrow", "!")
        .replace(r"\langle", "h")
        .replace(r"\rangle", "i")
        .replace(r"\dots", "...")
        .replace(r"\iff", "()")
        .replace(r"\prod", "QY")
        .replace(r"\hookrightarrow", ",!")
        .replace(r"\sum", "PX")
        .replace(r"\infty", "1")
        .replace(r"\setminus", "n")
        .replace(r"\bigcup", "S[")
        .replace(r"\mapsto", "7!")
        .replace(r"\omega", "!")
        .replace(r"\int", "RZ")
        .replace(r"\in ", "2")
        .replace(r"\rightharpoonup", "*")
        .replace(r"\longrightarrow", "-!")
        .replace(r"\subsetneq", "(")
        .replace(r"\\bigcap", "T\\")
        .replace(r"&gt;", ">")
        .replace(r"&lt;", "<")
        .replace("\\|", "k")
        .replace("ö", "o")
        .replace("Ö", "O")
        .replace("ü", "u")
        .replace("Ü", "U")
        .replace("ä", "a")
        .replace("Ä", "A")
    )
    return text


def preprocess_note(note: Note) -> Note:
    """
    Takes a Note and returns a Note where front and
    back fields have been parsed so that
    1. A lot of math symbols are exchanged for ascii symbols.
    2. The correct numbering is inserted.
    """
    note.front = apply_exchange_rules(note.front)
    note.back = apply_exchange_rules(note.back)
    r"""
    Substitues \item for the correct numbering.
    """
    note.back = preprocess_numbering(note.back)
    return note


def preprocess_notes(notes: list[Note]) -> list[Note]:
    """
    Takes a list of notes and returns
    a processed list of notes.
    """
    new_notes = []
    for note in notes:
        note = preprocess_note(note)
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


def filter_runs_through(symbol_filter: list[list[str]], text: str) -> bool:
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
        print(f"char: {char}, syms: {symbols_left[0]}")
        if char in symbols_left[0]:
            symbols_left.pop(0)
        if symbols_left == []:
            return True
    return False


def get_uppercase_in_latex_commands(text: str) -> list[str]:
    """
    Takes a string and returns all uppercase letters which
    occurr in some latex command like \\Omega or \\lVert.
    """
    uppercase_letters = []
    found = re.findall(r"\\[A-Za-z]+", text)
    for find in found:
        upper = re.findall(r"[A-Z]", find)
        for letter in upper:
            if letter not in uppercase_letters:
                uppercase_letters.append(letter)
    return uppercase_letters


def uppercase_letter_rule(symbols: list[str], text: str) -> bool:
    """
    Uppercase letter rule: all uppercase letters are rendered
    unless they are contained in a latex command. Namely greek
    uppercase letters like \\Omega or \\lVert.
    """
    for i in range(65, 91):
        if (
            chr(i) not in symbols
            and chr(i) in text
            and chr(i) not in get_uppercase_in_latex_commands(text)
        ):
            print("Wrong letter: " + chr(i))
            return False
    return True


def doublecheck(symbol_filter: list[list[str]], text: str) -> bool:
    """
    Does the negative check, meaning that of all symbols, if a
    symbol is not included in the symbol filter, it cannot show
    up in the text. Not quite, since text included latex code which
    is not actually rendered. Given latex code, I need to find out
    which characters are actually rendered.
    """
    symbols = []
    for entry in symbol_filter:
        for sym in entry:
            if sym not in symbols:
                symbols.append(sym)

    if uppercase_letter_rule(symbols, text):
        return True
    return False


def matches(symbol_filter: list[list[str]], text: str) -> bool:
    """
    Should return True if the svg matches the text.
    """
    if filter_runs_through(symbol_filter, text):
        print("filter ran through")
        if doublecheck(symbol_filter, text):
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
        print(path)
        with open(path, "r") as file:
            ids = parse_svg_file(file)
            symbol_filter = generate_symbol_filter(ids)
            matching_note = get_matching_note(symbol_filter, notes)
            print(matching_note)
    print(VICTORY_MSG)
