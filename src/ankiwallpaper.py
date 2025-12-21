import manim as mn
import src.utils as utils
import src.textokens as textokens
import src.constants as constants
from src.textokens import Token
from typing import Tuple

def generate_tex_objects(tokens: list[Token]) -> list[mn.MathTex]:
    """
    Takes tokenlist and return list of tex objects.
    """
    tex_objects = []
    for token in tokens:
        if token.content_type == 0:
            tex_objects.append(mn.Tex(token.content))
        elif token.content_type == 1 or token.content_type == 2:
            tex_objects.append(mn.MathTex(token.content))
    return tex_objects

def total_width(tex_objects: list[mn.MathTex]) -> float:
    """
    Sums the width of a list of tex objects.
    """
    return sum([obj.width for obj in tex_objects])

def generate_groupings(tokens: list[Token], tex_objects: list[mn.MathTex]) -> list[Tuple[list[mn.MathTex], bool]]:
    """
    Takes a list of tokens and a list of tex objects and returns a list of groupings.
    A grouping is a tuple containing a list of tex objects and a boolean flagging
    display math. Display math groupings by design consist of just one tex object.

    In gerenal we check for empty list before adding the current grouping to groupings.
    """
    groupings = []
    current_grouping = []
    for i in range(len(tokens)): 
        if tokens[i].content_type != 2 and total_width(current_grouping) + tex_objects[i].width < constants.MAX_WIDTH:
            current_grouping.append(tex_objects[i])
        elif tokens[i].content_type != 2 and total_width(current_grouping) + tex_objects[i].width >= constants.MAX_WIDTH:
            """
            The case where the current grouping is empty but tex_objects[i] has width greater than MAX_WIDTH
            needs to be better dealt with. Right now I just explicitly prevent the current grouping to
            be added to groupings by checking for an empty list and then add tex_objects[i] to the 
            current grouping. I think this is a ugly.
            """
            if current_grouping != []:
                groupings.append((current_grouping, False))
            current_grouping = [tex_objects[i]]
        elif tokens[i].content_type == 2:
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
    tokens = textokens.generate_tokens(line)
    """
    Generate tex_objects
    """
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
