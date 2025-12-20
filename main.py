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
    partition = removeAllOccurrences('<br>', partition)
    for i in range(len(partition)):
        if starts_with_math and i % 2 == 0 or not starts_with_math and i % 2 == 1:
            tokens.append((partition[i], 1))
        else:
            tokens.append((partition[i], 0))
    return tokens

def generate_tokens(front, back):
    tokens = []
    # generate tokens from front
    tokens = tokens + generate_tokens_from_non_display_math(front)
    # generate tokens from back
    starts_with_display_math = True if back[0:2] == "$$" else False
    display_math_partition = back.split("$$")
    display_math_partition = removeAllOccurrences('', display_math_partition)
    for i in range(len(display_math_partition)):
        if starts_with_display_math and i % 2 == 0 or not starts_with_display_math and i % 2 == 1:
            tokens.append((display_math_partition[i], 2))
        else:
            tokens = tokens + generate_tokens_from_non_display_math(display_math_partition[i])
    return tokens

def generate_tex_objects(tokens):
    tex_objects = []
    for token in tokens:
        if token[1] == 0:
            tex_objects.append(mn.Tex(token[0]))
        elif token[1] == 1:
            tex_objects.append(mn.MathTex(token[0]))
        elif token[1] == 2:
            # TODO: handle display math to be actual display math
            tex_objects.append(mn.MathTex(token[0]))
    return tex_objects

def total_width(tex_objects):
    return sum([obj.width for obj in tex_objects])

def generate_groupings(tokens, tex_objects):
    groupings = []
    current_grouping = []
    for i in range(len(tokens)): 
        if tokens[i][1] != 2 and total_width(current_grouping) + tex_objects[i].width < 8:
            current_grouping.append(tex_objects[i])
        elif tokens[i][1] != 2 and total_width(current_grouping) + tex_objects[i].width >= 8:
            groupings.append((current_grouping, False))
            current_grouping = [tex_objects[i]]
        elif tokens[i][1] == 2:
            # relevant if two tokens of type 2 occur in succession
            if current_grouping != []:
                groupings.append((current_grouping, False))
                current_grouping = []
            groupings.append(([tex_objects[i]], True))
    if current_grouping != []:
        groupings.append((current_grouping, False))
    return groupings

class AnkiCard(mn.Scene):
    """
    Convert a plaintext string containing the content of 
    an anki card into an animated wallpaper format (mp4).

    Issues: 

    I assume that anki correctly puts a tab character
    between fields (so front and back exist always).

    Any occurence of '$$$' will break the code.
    generate_tokens("token1", "$token2$$$token3$$")
    May be resolved because of the wonderful <br> (which is later removed).

    Automatic linebreaking.
    Tokens are grouping according to their type and width of their tex object.
    TODO: Improve the tokenizer to tokenize every word instead of transitions 
    from/to math mode. Even tokenize math mode objects further?

    TODO: Center display math vgroups using setx
    """
    def construct(self):
        line = r"Markov chain	$$\mathbb{P}(X_n \in B | \mathcal{F}_m) = \mathbb{P}(X_n \in B | X_m)$$"
        line = r"Lokalisierung von $R$ nach $S$	$$S^{-1} R := (R \times S)/\sim$$<br>wobei $\sim$ definiert ist durch<br>$$(r_1, s_1) \sim (r_2, s_2) :\iff \exists s \in S: s \cdot (r_1 s_2 - r_2 s_1) = 0$$<br>Elemente sind definiert durch&nbsp;<br>$$\frac{r}{s} := [(r, s) \ \text{modulo} \ \sim]$$<br>Addition und Multiplikation machen $S^{-1} R$ zu einem Ring		"
        if "paste" not in line:
            line = line.replace("&nbsp;", '')
            # Seperate heading (card front) from body (card back)
            fields = line.split('\t')
            fields = removeAllOccurrences('', fields)
            fields.append('')
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
            tex_objects = generate_tex_objects(tokens)
            """
            A grouping is a tuple containing a list of tex objects and a 
            boolean used to flag display math, which later needs to be centered.
            """
            groupings = generate_groupings(tokens, tex_objects)
            """
            Each groupings content is then turned into a vgroup. So here we have tuples
            containing a vgroup and again a boolean to flag display math.
            """
            print(f"LOG: {groupings}")
            vgroup_tuples = [(mn.VGroup(*grouping[0]).arrange(mn.RIGHT, buff=0.4), grouping[1]) for grouping in groupings]
            """
            Actual list of vgroups.
            """
            vgroups = [group[0] for group in vgroup_tuples]
            # The * operator unpacks the list
            group = mn.VGroup(*vgroups).arrange(
                    mn.DOWN,
                    aligned_edge=mn.LEFT,
                    buff=0.4
            )
            """
            Move display math to the center of the screen.
            """
            for i in range(len(vgroups)):
                if vgroup_tuples[i][1]:
                    group[i].set_x(0)
            self.play(mn.Write(group), run_time=5)
