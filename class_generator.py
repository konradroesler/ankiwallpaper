import src.utils as utils

if __name__ == "__main__":
    with open("images.py", "a") as image_file:
        image_file.seek(0)
        image_file.truncate()
        image_file.write("import manim as mn\nimport src.ankiwallpaper as aw\n")
        lines = utils.get_lines()
        for i in range(len(lines)):
            class_def = f"""
class Image{i}(mn.Scene):
    def construct(self):
        line = r"{lines[i]}"
        group = aw.generate_vgroup(line)
        self.add(group)
            """
            image_file.write(class_def)
