import manim as mn
import ankiwallpaper as aw


class Image0(mn.Scene):
    def construct(self):
        line = r"Raileigh-Ritzsches Variationsprinzip	$$\mathcal{E}_0 \leq \frac{\langle \Psi | \hat{H} | \Psi \rangle}{\langle \Psi | \Psi \rangle}$$			"
        group = aw.generate_group(line)
        self.add(group)

