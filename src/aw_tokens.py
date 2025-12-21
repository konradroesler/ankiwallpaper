import manim as mn
import src.utils as utils

"""
The general idea of the tokization process is to input a string
as exportet from anki and output a list of tuples, where the first
entry contains a string ready to be turned into a MathTex object,
and the second entry contains an integer, where
0: actual text, later a Tex object;
1: inline math, later a MathTex object;
2: display math, later a MathTex object aligned to x = 0.
The only difference between tokens of type 1 and tokens of type 2 is 
that tokens of type 2 get centered when generating the scene.

Improved tokenization respects latex environments such as enumerate.

"""

class VGroupToken:
    def __init__(self, content: mn.VGroup, is_display_math: bool):
        self.content = content
        self.is_display_math = is_display_math

    def __str__(self):
        return f"VGroupToken({self.content.__str__()}, {self.is_display_math})"

    def __repl__(self):
        return f"VGroupToken({self.content.__str__()}, {self.is_display_math})"

class TexToken:
    def __init__(self, content: mn.MathTex, content_type: int):
        self.content = content
        self.content_type = content_type

    def __str__(self):
        if type(self.content) == mn.Tex:
            """
            The Tex.tex_string attribute is a manim community addon.
            """
            return f"Token({self.content.tex_string}, {self.content_type})"
        elif type(self.content) == mn.MathTex:
            return f"Token({self.content.submobjects}, {self.content_type})"
        else:
            raise utils.NonMathTexTypeError("This object should be of type Tex or MathTex.")

    def __repr__(self):
        if type(self.content) == mn.Tex:
            """
            The Tex.tex_string attribute is a manim community addon.
            """
            return f"Token({self.content.tex_string}, {self.content_type})"
        elif type(self.content) == mn.MathTex:
            return f"Token({self.content.submobjects}, {self.content_type})"
        else:
            raise utils.NonMathTexTypeError("This object should be of type Tex or MathTex.")

class StringToken:
    def __init__(self, content: str, content_type: int):
        self.content = content
        self.content_type = content_type

    def __str__(self):
        return f"Token({self.content}, {self.content_type})"

    def __repr__(self):
        return f"Token({self.content}, {self.content_type})"

def generate_tokens_from_non_display_math(text: str) -> list[StringToken]:
    """
    Turns a string into tokens of type 0 and 1. This assumes that
    no random '$' characters are contained in the text or inline math,
    so splitting at '$' generates the correct partition.
    """
    tokens = []
    starts_with_math = True if text[0] == '$' else False
    partition = text.split('$')
    partition = utils.removeAllOccurrences('', partition)
    """
    These are inserted after display math by anki and I don't think they are useful.
    """
    partition = [element.replace('<br>', '') for element in partition]
    for i in range(len(partition)):
        if starts_with_math and i % 2 == 0 or not starts_with_math and i % 2 == 1:
            tokens.append(StringToken(partition[i], 1))
        else:
            tokens.append(StringToken(partition[i], 0))
    return tokens

def generate_tokens(line: str) -> list[StringToken]:
    tokens = []
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
    Generate tokens from front.
    """
    tokens = tokens + generate_tokens_from_non_display_math(front)
    """
    Generate tokens from back.

    First the display math is split from the non display math.
    This assumes that no random '$$' substring is contained inside
    any math or non math substring, so splitting at '$$' generates
    the correct partition.
    """
    starts_with_display_math = True if back[0:2] == "$$" else False
    display_math_partition = back.split("$$")
    display_math_partition = utils.removeAllOccurrences('', display_math_partition)
    for i in range(len(display_math_partition)):
        if starts_with_display_math and i % 2 == 0 or not starts_with_display_math and i % 2 == 1:
            tokens.append(StringToken(display_math_partition[i], 2))
        else:
            """
            Non display math is tokenized further since it still contains text and inline math.
            """
            tokens = tokens + generate_tokens_from_non_display_math(display_math_partition[i])
    return tokens
