import re


def substring(a: str, b: str) -> bool:
    for i in range(len(b) - len(a) + 1):
        yes = True
        for j in range(len(a)):
            if a[j] != b[i + j]:
                yes = False
        if yes:
            return True
    return False


def get_all_regex_matches():
    with open("Lernen.txt", "r") as file:
        result = []
        lines = file.readlines()
        for line in lines:
            found = re.findall(r"\\[a-zA-Z]+_.{1,20}^.{1,20}", line)
            for find in found:
                if find not in result:
                    result.append(find)
        print(result)
        for result in result:
            for result2 in result:
                if substring(result, result2):
                    print("substring")


text = r"\sum_{\sum^m_{j=1} j}^n i"
result = r"\sum^n_{\sum^m_{j=1} j} i"


depth = 0
ran_through = False
while True:
    current_depth = 0
    caret_flag = False
    underscore_flag = False
    part1, part2, part3, part4 = "", "", "", ""

    """
    Iterates the text and finds the first occurrence of a _ followed
    by a ^, cuts the text along those symbols into 4 parts and switches
    the second and third part. For _ and ^ to belong to the same object,
    no space should occurr in between.
    """

    for i in range(len(text)):
        if text[i] == "{":
            current_depth += 1
        elif text[i] == "}":
            current_depth -= 1
        """
        We iterate through the text for depth up to x.
        """
        if current_depth == depth:
            """
            Either we encounter _ and have already encountered ^,
            then the order is already correct. Or we have not
            encountered ^, so the underscore flag is set and part1
            is defined.
            """
            if text[i] == "_":
                if caret_flag:
                    caret_flag = False
                else:
                    part1 = text[:i]
                    underscore_flag = True
            """
            If we encounter ^ and have already encountered _, then
            we define part2. The caret flag is set either way.
            """
            if text[i] == "^":
                if underscore_flag:
                    part2 = text[len(part1) : i]
                caret_flag = True
            """
            If both flags are set and we encounter a space, i.e. the 
            end of a sequence \\command_sub^sup, part3 and part4 are
            defined.
            """
            if text[i] == " " and caret_flag and underscore_flag:
                part3 = text[len(part1) + len(part2) : i]
                part4 = text[i:]
            """
            If the end of a sequence is met and one of the flags is 
            not set, the search is reset.
            """
            if text[i] == " " and (not caret_flag or not underscore_flag):
                caret_flag = False
                underscore_flag = False
        print(f"{i}: {text[i]}, {caret_flag}, {underscore_flag}")
        """
        If all flags have been defined, part2 and part3 are switched.
        """
        if part1 != "" and part2 != "" and part3 != "" and part4 != "":
            text = part1 + part3 + part2 + part4
            part1, part2, part3, part4 = "", "", "", ""
            break
        """
        If at depth all sequences of interest have 
        been found, the depth is incremented.
        """
        if i == len(text) - 1:
            ran_through = True
    if ran_through:
        depth += 1
        ran_through = False
    """
    Search up to depth n.
    """
    if depth >= 2:
        break

print(text)
