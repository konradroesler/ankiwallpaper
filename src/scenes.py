import manim as mn
import ankiwallpaper as aw

class WriteAnimation(mn.Scene):
    """
    Convert a plaintext string containing the content of 
    an anki card into an animated wallpaper format (mp4).

    Issues: 

    I assume that anki correctly puts a tab character
    between fields (so front and back exist always).

    Any occurence of '$$$' will break the code.
    generate_tokens("token1", "$token2$$$token3$$")
    May be resolved because of the wonderful <br> (which is later removed).

    Automatic linebreaking.
    Tokens are grouping according to their type and width of their tex object.
    TODO: Improve the tokenizer to tokenize every word instead of transitions 
    from/to math mode. Even tokenize math mode objects further?

    Center display math vgroups using set_x
    """
    def construct(self):
        line = "abc"
        group = aw.generate_vgroup(line)
        run_time = aw.compute_run_time(group)
        self.play(mn.Write(group), run_time=run_time)

class Image(mn.Scene):
    def construct(self):
        line = "abc"
        group = aw.generate_vgroup(line)
        self.add(group)

class FadeoutAnimation(mn.Scene):
    def construct(self):
        line = "abc" 
        group = aw.generate_vgroup(line)
        self.play(mn.FadeOut(group), run_time=5)
