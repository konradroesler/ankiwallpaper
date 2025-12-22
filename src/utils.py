class DoesNotEncapsulateError(Exception):
    """
    Raised if some literal is truncated from a string
    not ending and starting on it.
    """

    def __init__(self, message):
        super().__init__(message)


class NonMathTexTypeError(Exception):
    """
    Raised on objects neither of type Tex nor MathTex.
    """

    def __init__(self, message):
        super().__init__(message)


def ends_with(literal: str, text: str) -> bool:
    """
    Wether text ends with literal.
    """
    if len(text) < len(literal):
        return False
    elif text[-len(literal) :] == literal:
        return True
    else:
        return False


def starts_with(literal: str, text: str) -> bool:
    """
    Wether text starts with literal.
    """
    if len(text) < len(literal):
        return False
    elif text[0 : len(literal)] == literal:
        return True
    else:
        return False


def encapsulates(literal: str, text: str) -> bool:
    """
    Wether text starts and ends with literal.
    """
    if starts_with(literal, text) and ends_with(literal, text):
        return True
    else:
        return False


def truncate(literal: str, text: str) -> str:
    """
    Returns modified text where literal is removed
    from the front and back.
    """
    if encapsulates(literal, text):
        return text[len(literal) : -len(literal)]
    else:
        raise DoesNotEncapsulateError("Can't trucate what's not there.")


def removeAllOccurrences(literal: str, mylist: list[str]) -> list[str]:
    """
    Remove all (exact) occurences of literal in mylist.
    """
    for entry in mylist:
        if entry == literal:
            mylist.remove(literal)
    return mylist


"""
Honestly some of these aren't used.
"""


def occurrs_in(mylist: list[str], literal: str) -> bool:
    """
    Wether the string literal is contained
    in any string entry of mylist.
    """
    for item in mylist:
        if literal in item:
            return True
    return False


def is_any_empty(mylist: list[str]) -> bool:
    """
    Wether any entry of mylist is an emptry string.
    """
    for item in mylist:
        if item == "":
            return True
    else:
        return False


def remove_empty(mylist: list[str]) -> list[str]:
    """
    Return new list where all empty string
    entries in mylist are removed.
    """
    new_list = []
    for item in mylist:
        if item != "":
            new_list.append(item)
    return new_list


def get_lines() -> list[str]:
    """
    Return parsed list of line strings of
    my anki collection in plain text.
    """
    with open("Lernen.txt") as anki_file:
        anki_text = anki_file.read()
        lines = anki_text.split("\n")
        new_lines = []
        for line in lines:
            if "paste" not in line:
                new_lines.append(line)
        lines = remove_empty(new_lines)
    """
    Leaving out the first two might
    be totally case specific.
    """
    return lines[2:]
