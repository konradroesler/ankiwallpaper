import manim as mn

class AnkiCard(mn.Scene):
    def construct(self):
        line = r"Markov chain	$\mathbb{P}(X_n \in B | \mathcal{F}_m) = \mathbb{P}(X_n \in B | X_m)$"
        tex1 = mn.Tex(r'Markov chain', font_size=144)
        tex2 = mn.MathTex(r'\mathbb{P}(X_n \in B | \mathcal{F}_m) = \mathbb{P}(X_n \in B | X_m)')
        group = mn.VGroup(tex1, tex2).arrange(
                mn.DOWN,
                aligned_edge=mn.LEFT,
                buff=0.4
        )

        self.add(group)
