import src.utils as utils
from typing import Tuple

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
"""

def generate_tokens_from_non_display_math(text: str) -> list[Tuple[str, int]]:
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
            tokens.append((partition[i], 1))
        else:
            tokens.append((partition[i], 0))
    return tokens

def generate_tokens(front: str, back: str) -> list[Tuple[str, int]]:
    tokens = []
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
            tokens.append((display_math_partition[i], 2))
        else:
            """
            Non display math is tokenized further since it still contains text and inline math.
            """
            tokens = tokens + generate_tokens_from_non_display_math(display_math_partition[i])
    return tokens
