import manim as mn

class AnkiCard(mn.Scene):
    def construct(self):
        tex1 = mn.Tex("abc")
        tex2 = mn.Tex("m"*20)
        group = mn.VGroup(tex1, tex2).arrange(
            mn.DOWN,
            buff=0.4,
            aligned_edge=mn.LEFT
        )
        group[0].set_x(0)
        self.add(group)
