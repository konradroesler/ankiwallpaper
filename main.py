import subprocess
import src.utils as utils

if __name__ == "__main__":
    lines = utils.get_lines()
    for i in range(len(lines)):
        print(lines[i])
        subprocess.run(
            [
                "manim",
                "--quality",
                "h",
                "--resolution",
                "1920,1080",
                "--config_file",
                "manim.cfg",
                "--media_dir",
                "./out",
                "--output_file",
                f"image{i}",
                "images.py",
                f"Image{i}",
            ]
        )
        subprocess.run(
            ["mv", "-f", f"./out/images/images/image{i}.png", "./image_collection"]
        )
