import manim as mn
import src.utils as utils
import src.aw_tokens as aw_tokens 
import src.constants as constants
from src.aw_tokens import StringToken, TexToken, VGroupToken

def generate_tex_tokens(str_tokens: list[StringToken]) -> list[TexToken]:
    """
    Takes tokenlist and return list of tex objects.
    """
    tex_tokens = []
    for token in str_tokens:
        if token.content_type == 0:
            tex_tokens.append(TexToken(mn.Tex(token.content), token.content_type))
        elif token.content_type == 1 or token.content_type == 2:
            tex_tokens.append(TexToken(mn.MathTex(token.content), token.content_type))
    return tex_tokens 

def compute_total_width(tex_objects: list[mn.MathTex]) -> float:
    """
    Sums the width of a list of tex objects.
    """
    return sum([obj.width for obj in tex_objects])

class Grouping:
    def __init__(self, content: list[mn.MathTex], is_display_math: bool, is_indented: bool):
        self.content = content
        self.is_display_math = is_display_math
        self.is_indented = is_indented

    def __str__(self):
        return f"Grouping({self.content.__str__()}, {self.is_display_math}, {self.is_indented})"

    def __repl__(self):
        return f"Grouping({self.content.__str__()}, {self.is_display_math}, {self.is_indented})"

def generate_groupings(textokens: list[TexToken]) -> list[Grouping]:
    """
    Takes a list of tokens and a list of tex objects and returns a list of groupings.
    A grouping is a tuple containing a list of tex objects and a boolean flagging
    display math. Display math groupings by design consist of just one tex object.

    In gerenal we check for empty list before adding the current grouping to groupings.
    """
    groupings = []
    current_grouping = []
    for token in textokens:
        if token.content_type != 2 and compute_total_width(current_grouping) + token.content.width < constants.MAX_WIDTH:
            current_grouping.append(token.content)
        elif token.content_type != 2 and compute_total_width(current_grouping) + token.content.width >= constants.MAX_WIDTH:
            """
            The case where the current grouping is empty but tex_objects[i] has width greater than MAX_WIDTH
            needs to be better dealt with. Right now I just explicitly prevent the current grouping to
            be added to groupings by checking for an empty list and then add tex_objects[i] to the 
            current grouping. I think this is a ugly.
            """
            if current_grouping != []:
                groupings.append(Grouping(current_grouping, is_display_math=False, is_indented=False))
            current_grouping = [token.content]
        elif token.content_type == 2:
            """ 
            If two tokens of type 2 (display math) occur in succession.
            """
            if current_grouping != []:
                groupings.append(Grouping(current_grouping, is_display_math=False, is_indented=False))
                current_grouping = []
            groupings.append(Grouping([token.content], is_display_math=True, is_indented=False))
    if current_grouping != []:
        groupings.append(Grouping(current_grouping, is_display_math=False, is_indented=False))
    return groupings

def compute_run_time(vgroup: mn.VGroup) -> float:
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

def generate_vgroup(line: str) -> mn.VGroup:
    """
    Generate tokens from the anki cards string representation.
    """
    str_tokens = aw_tokens.generate_tokens(line)
    """
    Generate tex_objects
    """
    tex_tokens = generate_tex_tokens(str_tokens)
    """
    A grouping is a tuple containing a list of tex objects and a 
    boolean used to flag display math, which later needs to be centered.
    """
    groupings = generate_groupings(tex_tokens)
    """
    Each groupings content is then turned into a vgroup. So here we have tuples
    containing a vgroup and again a boolean to flag display math.
    """
    vgroup_tokens = [VGroupToken(mn.VGroup(*grouping.content).arrange(mn.RIGHT, buff=0.4), grouping.is_display_math) for grouping in groupings]
    """
    Actual list of vgroups.
    """
    vgroups = [token.content for token in vgroup_tokens]
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
        if vgroup_tokens[i].is_display_math:
            group[i].set_x(0)
    return group
