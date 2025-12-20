import utils

"""
The general idea of the tokization process is to input a string
as exportet from anki and output a list of tuples, where the first
entry contains a string ready to be turned into a MathTex object,
and the second entry contains an integer, where
0: actual text, later a Tex object;
1: inline math, later a MathTex object;
2: display math, later a MathTex object aligned to x = 0.
"""

def generate_tokens_from_non_display_math(text):
    tokens = []
    starts_with_math = True if text[0] == '$' else False
    partition = text.split('$')
    partition = utils.removeAllOccurrences('', partition)
    partition = [element.replace('<br>', '') for element in partition]
    for i in range(len(partition)):
        if starts_with_math and i % 2 == 0 or not starts_with_math and i % 2 == 1:
            tokens.append((partition[i], 1))
        else:
            tokens.append((partition[i], 0))
    return tokens

def generate_tokens(front, back):
    tokens = []
    """
    Generate tokens from front.
    """
    tokens = tokens + generate_tokens_from_non_display_math(front)
    """
    Generate tokens from back.
    """
    starts_with_display_math = True if back[0:2] == "$$" else False
    display_math_partition = back.split("$$")
    display_math_partition = utils.removeAllOccurrences('', display_math_partition)
    for i in range(len(display_math_partition)):
        if starts_with_display_math and i % 2 == 0 or not starts_with_display_math and i % 2 == 1:
            tokens.append((display_math_partition[i], 2))
        else:
            tokens = tokens + generate_tokens_from_non_display_math(display_math_partition[i])
    return tokens
