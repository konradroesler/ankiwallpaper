import re

"""
Ansatz: Search the text for valid latex expressions,
so \\command, \\command{...}{...} or {...} and check
for every term1, term2, term3 the string:
f"{term1}^{term2}_{term3}" or f"{term1}_{term2}^{term3}
is contained in the text.
"""


def substring(a: str, b: str) -> bool:
    for i in range(len(b) - len(a) + 1):
        yes = True
        for j in range(len(a)):
            if a[j] != b[i + j]:
                yes = False
        if yes:
            return True
    return False


def get_terms1_candidates(text: str) -> list[str]:
    candidates = []
    for i in range(len(text)):
        if text[i] == "{":
            for j in range(i, len(text)):
                if text[j] == "}":
                    candidates.append(text[i : j + 1])

    return candidates


def get_terms1(text: str) -> list[str]:
    """
    Terms of form {...}.
    """
    candidates = get_terms1_candidates(text)
    terms = []
    for term in candidates:
        depth = 0
        flag = True
        for i in range(len(term)):
            if term[i] == "{":
                depth += 1
            elif term[i] == "}":
                depth -= 1
            if (depth == 0 and i != len(term) - 1) or (
                depth != 0 and i == len(term) - 1
            ):
                flag = False
        if flag:
            terms.append(term)
    return terms


def get_terms2(text: str) -> list[str]:
    """
    Terms of form \\command.
    """
    terms2 = re.findall(r"\\[a-zA-Z]+", text)
    return terms2


def is_letter(char):
    letters = [i for i in range(65, 91)] + [i for i in range(97, 123)]
    return ord(char) in letters


def validate1(text: str) -> bool:
    letters = [j for j in range(65, 91)] + [k for k in range(97, 123)]
    if text[0] == "\\" and all([ord(text[i]) in letters for i in range(1, len(text))]):
        return True
    return False


def get_terms3(text):
    candidates = []
    for i in range(len(text)):
        bs_flag = False  # BackSlash flag
        fl_flag = False  # First Letter flag
        fbo_flag = False  # First Brace Open flag
        for j in range(i, len(text)):
            """
            Pattern:
            if not current_flag:
                if condition_for_advancing:
                    current_flag = True
                    continue
                elif condition_for_break:
                    break
                else:
                    pass
            """
            if not bs_flag:
                if text[j] == "\\":
                    bs_flag = True
                    continue
                elif text[j] != "\\":
                    break
                else:
                    pass
            elif not fl_flag:
                if is_letter(text[j]):
                    fl_flag = True
                    continue
                elif not is_letter(text[j]):
                    break
                else:
                    pass
            elif not fbo_flag:
                if text[j] == "{":
                    fbo_flag = True
                    continue
                elif not is_letter(text[j]):
                    break
                else:
                    pass
            else:
                for k in range(i, len(text)):
                    if text[k] == "}":
                        candidates.append(text[i : k + 1])
                break
    """
    Validate candidates.
    """
    terms = []
    for candidate in candidates:
        a_flag = False  # Argument flag
        depth = 0
        v_flag = True  # Validation flag
        for i in range(len(candidate)):
            if candidate[i] == "{":
                depth += 1
                a_flag = True
            elif candidate[i] == "}":
                depth -= 1
            if a_flag and depth == 0:
                if i == len(candidate) - 1:
                    pass
                elif candidate[i + 1] != "{":
                    v_flag = False
            if a_flag and depth != 0 and i == len(candidate) - 1:
                v_flag = False
        if v_flag:
            terms.append(candidate)
    return terms


def get_terms(text: str) -> list[str]:
    return get_terms1(text) + get_terms2(text) + get_terms3(text)


def get_expressions(text: str) -> list[str]:
    expressions = []
    terms1 = get_terms1(text)
    terms2 = get_terms2(text)
    terms3 = get_terms3(text)
    for term1 in terms2 + terms3:
        for term2 in terms1 + terms2 + terms3:
            for term3 in terms1 + terms2 + terms3:
                exp1 = term1 + "_" + term2 + "^" + term3
                exp2 = term1 + "^" + term2 + "_" + term3
                if exp1 in text:
                    expressions.append(exp1)
                if exp2 in text:
                    expressions.append(exp2)
    return expressions


def get_expressions_from_file() -> list[str]:
    expressions = []
    with open("Lernen.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            new_expressions = get_expressions(line)
            print(new_expressions)
            expressions = expressions + new_expressions

    return expressions


if __name__ == "__main__":
    text = "\\sum_\\mathbb{N}^\\mathbb{N}"
    candidates = get_expressions(text)
    expressions = []
    for exp in expressions:
        flag = True
        for exp1 in expressions:
            if substring(exp, exp1) and not exp == exp1:
                flag = False
                break
        if flag:
            expressions.append(exp)
    print(expressions)
