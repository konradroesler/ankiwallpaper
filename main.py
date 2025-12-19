import manim as mn

class CreateCircle(mn.Scene):
    def construct(self):
        circle = mn.Circle()
        circle.set_fill(mn.PINK, opacity=0.5)
        self.play(mn.Create(circle))
