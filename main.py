import utils
import textokens
import manim as mn


def generate_tex_objects(tokens):
    """
    Takes tokenlist and return list of tex objects.
    """
    tex_objects = []
    for token in tokens:
        if token[1] == 0:
            tex_objects.append(mn.Tex(token[0]))
        elif token[1] == 1 or token[1] == 2:
            tex_objects.append(mn.MathTex(token[0]))
    return tex_objects

def total_width(tex_objects):
    """
    Sums the width of a list of tex objects.
    """
    return sum([obj.width for obj in tex_objects])

def generate_groupings(tokens, tex_objects):
    """
    Takes a list of tokens and a list of tex objects and returns a list of groupings.
    A grouping is a tuple containing a list of tex objects and a boolean flagging
    display math. Display math groupings by design consist of just one tex object.

    In gerenal we check for empty list before adding the current grouping to groupings.
    """
    groupings = []
    current_grouping = []
    for i in range(len(tokens)): 
        if tokens[i][1] != 2 and total_width(current_grouping) + tex_objects[i].width < 8:
            current_grouping.append(tex_objects[i])
        elif tokens[i][1] != 2 and total_width(current_grouping) + tex_objects[i].width >= 8:
            """
            The case where the current grouping is empty but tex_objects[i] has width greater than 8
            needs to be better dealt with. Right now I just explicitly prevent the current grouping to
            be added to groupings by checking for an empty list and then add tex_objects[i] to the 
            current grouping. I think this is a ugly.
            """
            if current_grouping != []:
                groupings.append((current_grouping, False))
            current_grouping = [tex_objects[i]]
        elif tokens[i][1] == 2:
            """ 
            If two tokens of type 2 (display math) occur in succession.
            """
            if current_grouping != []:
                groupings.append((current_grouping, False))
                current_grouping = []
            groupings.append(([tex_objects[i]], True))
    if current_grouping != []:
        groupings.append((current_grouping, False))
    return groupings

def compute_run_time(vgroup):
    """
    Takes a vgroup object and returns the write animations runtime.

    The vgroup is assumed to contain vgroups which contain Tex and MathTex objects.
    """
    run_time = 0
    for subvgroup in vgroup:
        for obj in subvgroup:
            if type(obj) == mn.Tex:
                """
                The Tex.tex_string attribute is a manim community addon.
                """
                run_time += len(obj.tex_string) * 0.05
            elif type(obj) == mn.MathTex:
                run_time += len(obj.submobjects) * 0.1
            else: 
                raise utils.NonMathTexTypeError("This object should be of type Tex or MathTex.")
    return run_time

def generate_group(line) -> mn.VGroup:
    """
    &nbsp; might acutally need to be addressed when 
    improving tokenization, but I don't know.
    """
    line = line.replace("&nbsp;", '')
    # Seperate heading (card front) from body (card back)
    fields = line.split('\t')
    fields = utils.removeAllOccurrences('', fields)
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
    tokens = textokens.generate_tokens(front, back)
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
    return group

class WriteAnimation(mn.Scene):
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

    Center display math vgroups using set_x
    """
    def construct(self):
        line = r"Lokalisierung von $R$ nach $S$	$$S^{-1} R := (R \times S)/\sim$$<br>wobei $\sim$ definiert ist durch<br>$$(r_1, s_1) \sim (r_2, s_2) :\iff \exists s \in S: s \cdot (r_1 s_2 - r_2 s_1) = 0$$<br>Elemente sind definiert durch&nbsp;<br>$$\frac{r}{s} := [(r, s) \ \text{modulo} \ \sim]$$<br>Addition und Multiplikation machen $S^{-1} R$ zu einem Ring		"
        if "paste" not in line:
            group = generate_group(line)
            run_time = compute_run_time(group)
            self.play(mn.Write(group), run_time=run_time)

class Image(mn.Scene):
    def construct(self):
        line = r"Lokalisierung von $R$ nach $S$	$$S^{-1} R := (R \times S)/\sim$$<br>wobei $\sim$ definiert ist durch<br>$$(r_1, s_1) \sim (r_2, s_2) :\iff \exists s \in S: s \cdot (r_1 s_2 - r_2 s_1) = 0$$<br>Elemente sind definiert durch&nbsp;<br>$$\frac{r}{s} := [(r, s) \ \text{modulo} \ \sim]$$<br>Addition und Multiplikation machen $S^{-1} R$ zu einem Ring		"
        if "paste" not in line:
            group = generate_group(line)
            self.add(group)

class FadeoutAnimation(mn.Scene):
    def construct(self):
        line = r"Lokalisierung von $R$ nach $S$	$$S^{-1} R := (R \times S)/\sim$$<br>wobei $\sim$ definiert ist durch<br>$$(r_1, s_1) \sim (r_2, s_2) :\iff \exists s \in S: s \cdot (r_1 s_2 - r_2 s_1) = 0$$<br>Elemente sind definiert durch&nbsp;<br>$$\frac{r}{s} := [(r, s) \ \text{modulo} \ \sim]$$<br>Addition und Multiplikation machen $S^{-1} R$ zu einem Ring		"
        if "paste" not in line:
            group = generate_group(line)
            self.play(mn.FadeOut(group), run_time=5)
