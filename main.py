import manim as mn

class MultipleTabsError(Exception):
    def __init__(self, message):
        super().__init__(message)

class DoesNotEncapsulateError(Exception):
    def __init__(self, message):
        super().__init__(message)

def endsWith(literal,text):
    if len(text) < len(literal):
        return False
    elif text[-len(literal):] == literal:
        return True
    else:
        return False

def startsWith(literal, text):
    if len(text) < len(literal):
        return False
    elif text[0:len(literal)] == literal:
        return True
    else:
        return False

def encapsulates(literal, text):
    if startsWith(literal, text) and endsWith(literal, text):
        return True
    else:
        return False

def truncate(literal, text):
    if encapsulates(literal, text):
        return text[len(literal), -len(literal)]
    else:
        raise DoesNotEncapsulateError("Can't trucate what's not there.")

def removeAllOccurrences(literal, mylist):
    for entry in mylist:
        if entry == literal:
            mylist.remove(literal)
    return mylist 

def generate_tokens_from_non_display_math(text):
    tokens = []
    starts_with_math = True if text[0] == '$' else False
    partition = text.split('$')
    partition = removeAllOccurrences('', partition)
    for i in range(len(partition)):
        if starts_with_math and i % 2 == 0 or not starts_with_math and i % 2 == 1:
            tokens.append((partition[i], 1))
        else:
            tokens.append((partition[i], 0))
    return tokens

def generate_tokens(front, back):
    tokens = []
    if front[0] == '$':
        tokens.append((front, 1))
    else:
        tokens.append((front, 0))
    starts_with_display_math = True if back[0:2] == "$$" else False
    display_math_partition = back.split("$$")
    display_math_partition = removeAllOccurrences('', display_math_partition)
    for i in range(len(display_math_partition)):
        if starts_with_display_math and i % 2 == 0 or not starts_with_display_math and i % 2 == 1:
            tokens.append((display_math_partition[i], 2))
        else:
            tokens = tokens + generate_tokens_from_non_display_math(display_math_partition[i])
    return tokens

def toManimTexObject(text, math):
    if math:
        return mn.MathTex(text)
    else:
        return mn.Tex(text)

class AnkiCard(mn.Scene):
    """
    Convert a plaintext string containing the content of 
    an anki card into an animated wallpaper format (mp4).

    Issues: 

    I assume that anki correctly puts a tab character
    between fields (so front and back exist always).

    TODO: Any occurence of '$$$' will break the code.
    generate_tokens("token1", "$token2$$$token3$$")
    """

    def construct(self):
        line = r"Markov chain	$\mathbb{P}(X_n \in B | \mathcal{F}_m) = \mathbb{P}(X_n \in B | X_m)$"
        if "paste" not in line:
            line.replace("&nbsp;", '')
            # Seperate heading (card front) from body (card back)
            fields = line.split('\t')
            fields = removeAllOccurrences('', fields)
            front = fields[0]
            back = fields[1]

            """
            A token is a tuple containing a string ready to be turned
            into Tex and an integer between 0 and 2 determining if its 
            0: text
            1: inline math
            2: display math
            """
            tokens = generate_tokens(front, back)

            tex1 = mn.Tex(r'Markov chain')
            tex2 = mn.MathTex(r'\mathbb{P}(X_n \in B | \mathcal{F}_m) = \mathbb{P}(X_n \in B | X_m)')
            # The * operator unpacks the list
            group = mn.VGroup(*[tex1, tex2]).arrange(
                    mn.DOWN,
                    aligned_edge=mn.LEFT,
                    buff=0.4
            )
            self.play(mn.Write(group))
