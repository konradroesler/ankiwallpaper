import re
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
    def __init__(self, content: mn.VGroup, is_display_math: bool, environment: str):
        self.content = content
        self.is_display_math = is_display_math
        self.environment = environment

    def __str__(self):
        return f"VGroupToken({self.content.__str__()}, {self.is_display_math}, {self.environment})"

    def __repl__(self):
        return f"VGroupToken({self.content.__str__()}, {self.is_display_math}, {self.environment})"


class TexToken:
    def __init__(self, content: mn.MathTex, content_type: int, environment: str):
        self.content = content
        self.content_type = content_type
        self.environment = environment

    def __str__(self):
        if type(self.content) == mn.Tex:
            """
            The Tex.tex_string attribute is a manim community addon.
            """
            return f"Token({self.content.tex_string}, {self.content_type}, {self.environment})"
        elif type(self.content) == mn.MathTex:
            return f"Token({self.content.submobjects}, {self.content_type}, {self.environment})"
        else:
            raise utils.NonMathTexTypeError(
                "This object should be of type Tex or MathTex."
            )

    def __repr__(self):
        if type(self.content) == mn.Tex:
            """
            The Tex.tex_string attribute is a manim community addon.
            """
            return f"Token({self.content.tex_string}, {self.content_type}, {self.environment})"
        elif type(self.content) == mn.MathTex:
            return f"Token({self.content.submobjects}, {self.content_type}, {self.environment})"
        else:
            raise utils.NonMathTexTypeError(
                "This object should be of type Tex or MathTex."
            )


class StringToken:
    def __init__(self, content: str, content_type: int, environment: str):
        self.content = content
        self.content_type = content_type
        self.environment = environment

    def __str__(self):
        return f"Token({self.content}, {self.content_type}, {self.environment})"

    def __repr__(self):
        return f"Token({self.content}, {self.content_type}, {self.environment})"


def generate_tokens_from_non_display_math(
    text: str, environment: str
) -> list[StringToken]:
    """
    Turns a string into tokens of type 0 and 1. This assumes that
    no random '$' characters are contained in the text or inline math,
    so splitting at '$' generates the correct partition.
    """
    tokens = []
    starts_with_math = True if text[0] == "$" else False
    partition = text.split("$")
    partition = utils.removeAllOccurrences("", partition)
    """
    These are inserted after display math by anki and I don't think they are useful.
    """
    partition = [element.replace("<br>", "") for element in partition]
    for i in range(len(partition)):
        if starts_with_math and i % 2 == 0 or not starts_with_math and i % 2 == 1:
            tokens.append(
                StringToken(partition[i], content_type=1, environment=environment)
            )
        else:
            tokens.append(
                StringToken(partition[i], content_type=0, environment=environment)
            )
    return tokens


def generate_tokens(text: str, environment: str) -> list[StringToken]:
    tokens = []
    """
    First the display math is split from the non display math.
    This assumes that no random '$$' substring is contained inside
    any math or non math substring, so splitting at '$$' generates
    the correct partition.
    """
    starts_with_display_math = True if text[0:2] == "$$" else False
    display_math_partition = text.split("$$")
    display_math_partition = utils.removeAllOccurrences("", display_math_partition)
    for i in range(len(display_math_partition)):
        if (
            starts_with_display_math
            and i % 2 == 0
            or not starts_with_display_math
            and i % 2 == 1
        ):
            tokens.append(
                StringToken(
                    display_math_partition[i], content_type=2, environment=environment
                )
            )
        else:
            """
            Non display math is tokenized further since it still contains text and inline math.
            """
            tokens = tokens + generate_tokens_from_non_display_math(
                display_math_partition[i], environment=environment
            )
    return tokens


def get_environment_substrings(text: str) -> list[str]:
    r"""
    Return a list of all environment substring of
    form \begin{...} or \end{...}.
    """
    regex = r"(\\begin\{[a-z]+\}|\\end\{[a-z]+\})"
    substrings = re.findall(regex, text)
    return substrings


def get_type_of_environment(env_string: str) -> str:
    r"""
    Takes a environment_substring of form \begin{...} or \end{...}
    and return the ... part.
    """
    env_string = (
        env_string.replace(r"\begin{", "").replace(r"\end{", "").replace(r"}", "")
    )
    return env_string


def clean_tokens(tokens: list[StringToken]) -> list[StringToken]:
    """
    Removes tabs and &nbsp; from any token content.
    Removes empty tokens.
    """
    new_tokens = []
    for token in tokens:
        token.content = token.content.replace("\t", "").replace(r"&nbsp;", "")
        """
        Experimental
        """
        token.content = token.content.replace(r"\\", "")
        token.content = token.content.replace(r"\mathbb{1}", r"\mathbf{1}")
        if token.content.replace(" ", "") != "":
            new_tokens.append(token)
    return new_tokens


def insert_enumerate_numbering(tokens: list[StringToken]) -> list[StringToken]:
    r"""
    This removes the [label=...] remnants from enumerate environments and
    substitutes the \item substring for the proper numbering.
    """
    new_tokens = []
    numbering = ""
    number = 1
    for token in tokens:
        if token.environment == "enumerate":
            if "roman" in token.content:
                numbering = "roman"
            elif "alph" in token.content:
                numbering = "alph"
            elif "arabic" in token.content:
                numbering = "arabic"
            else:
                numbering = "arabic"
            token.content = re.sub(r"\[label=[a-z\(\)\*\\]+\]", "", token.content)
        else:
            numbering = "none"
        if r"\item" in token.content:
            match numbering:
                case "roman":
                    token.content = token.content.replace(
                        r"\item", "(" + "i" * number + ")"
                    )
                    number += 1
                case "alph":
                    char = chr(96 + number)
                    token.content = token.content.replace(r"\item", char + ")")
                    number += 1
                case "arabic":
                    token.content = token.content.replace(r"\item", str(number) + ")")
                    number += 1
                case _:
                    pass
        new_tokens.append(token)
    return new_tokens


def tex_environment_split(text: str) -> list[StringToken]:
    r"""
    Takes a string representing an anki card and returns a list of tokens.
    environment_substrings are string of form \begin{...} and \end{...}.
    """
    tokens = []
    environment_substrings = get_environment_substrings(text)
    splitting = []
    """
    For every environment substring found the text is split in two
    and tokens are generated for the first part.
    """
    for env_string in environment_substrings:
        """
        This splits the text only on the first occurrence of env_string.
        """
        splitting = text.split(env_string, 1)
        if "begin" in env_string:
            tokens = tokens + generate_tokens(splitting[0], environment="none")
            text = splitting[1]
        elif "end" in env_string:
            env_type = get_type_of_environment(env_string)
            tokens = tokens + generate_tokens(splitting[0], environment=env_type)
            text = splitting[1]
    r"""
    Text after the last \end{...}.
    """
    tokens = tokens + generate_tokens(text, environment="none")

    tokens = clean_tokens(tokens)

    tokens = insert_enumerate_numbering(tokens)

    return tokens
