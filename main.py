import manim as mn

class MultipleTabsError(ValueError):
    def __init__(self, message):
        super().__init__(message)

def endsWith(literal,text):
    if len(text) < len(literal):
        return False
    elif text[len(literal)-len(text)+1:] == literal:
        return True
    else:
        return False

def startsWith(literal, text):
    pass

def encapsulates(literal, text):
    if startsWith(literal, text) and endsWith(literal, text):
        return True
    else:
        return False

def toManimTexObject(text, math):
    if math:
        return mn.MathTex(text)
    else:
        return mn.Tex(text)

class AnkiCard(mn.Scene):
    def construct(self):
        line = r"Markov chain	$\mathbb{P}(X_n \in B | \mathcal{F}_m) = \mathbb{P}(X_n \in B | X_m)$"
        if "paste" not in line:
            line.replace("&nbsp;", '')
            # Seperate heading (card front) from body (card back)
            fields = line.split('\t')
            if len(fields) == 2:
                heading = fields[0]
                body = fields[1]
                tex1 = mn.Tex(r'Markov chain')
                tex2 = mn.MathTex(r'\mathbb{P}(X_n \in B | \mathcal{F}_m) = \mathbb{P}(X_n \in B | X_m)')
                group = mn.VGroup(tex1, tex2).arrange(
                        mn.DOWN,
                        aligned_edge=mn.LEFT,
                        buff=0.4
                )
                self.play(mn.Write(group))
            elif len(fields) == 1:
                body = fields[0]
                # TODO
            else: 
                raise MultipleTabsError(f"Too many tab characters in: {line}")
