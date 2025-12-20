import utils

if __name__ == "__main__":
    with open("images.py", 'a') as image_file:
        image_file.write("import manim as mn\nimport groups\n\n")
        with open("Lernen.txt") as anki_file: 
            anki_text = anki_file.read()
            lines = anki_text.split('\n') 
            new_lines = []
            for line in lines:
                if "paste" not in line:
                    new_lines.append(line)
            lines = utils.remove_empty(new_lines)
            for i in range(len(lines)):
                class_def = f"""
class Image{i}(mn.Scene):
    def construct(self):
        line = r"{lines[i]}"
        group = groups.generate_group(line)
        self.add(group)

                """
                image_file.write(class_def)

