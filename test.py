import manim as mn

class AnkiCard(mn.Scene):
    def construct(self):
        tex_objects = [mn.Tex("abc") for _ in range(12)]
        group = mn.VGroup(*tex_objects).arrange(
            mn.DOWN,
            buff=0.4,
            aligned_edge=mn.LEFT
        )
        self.add(group)
