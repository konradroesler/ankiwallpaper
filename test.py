import re
import manim as mn
import src.ankiwallpaper as aw
import src.aw_tokens as aw_tokens

line = r"$G$ zyklisch	$$G = \langle g \rangle$$<br>$$g^n := \begin{cases} 1, &amp; n=0 \\ g \cdot g^{n-1}, &amp; n&gt;0 \\ g \cdot g^{n+1}, &amp; n&lt;0 \end{cases}$$			"


class Image(mn.Scene):
    def construct(self):
        group = aw.generate_vgroup(line)
        self.add(group)
