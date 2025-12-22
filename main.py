import subprocess
import src.utils as utils


def if_wpaperd_supported_video():
    """
    The note1 name should be dynamically generated when generating the whole collection.
    Each complete scene is argonized into:
    a: write animation
    b: static image
    c: fadeout animation
    """
    subprocess.run(
        [
            "manim",
            "--quality",
            "h",
            "--resolution",
            "1920,1080",
            "--config_file",
            "manim.cfg",
            "--output_file",
            "a1",
            "--media_dir",
            "./out",
            "--format",
            "gif",
            "scenes.py",
            "WriteAnimation",
        ]
    )
    subprocess.run(
        [
            "manim",
            "--quality",
            "h",
            "--resolution",
            "1920,1080",
            "--config_file",
            "manim.cfg",
            "--output_file",
            "b1",
            "--media_dir",
            "./out",
            "scenes.py",
            "Image",
        ]
    )
    subprocess.run(
        [
            "manim",
            "--quality",
            "h",
            "--resolution",
            "1920,1080",
            "--config_file",
            "manim.cfg",
            "--output_file",
            "c1",
            "--media_dir",
            "./out",
            "--format",
            "gif",
            "scenes.py",
            "FadeoutAnimation",
        ]
    )
    """
    Postprocessing
    """
    subprocess.run(["mkdir", "./collection/1"])
    subprocess.run(
        ["mv", "-f", "./out/videos/scenes/1080p60/a1.gif", "./collection/1/"]
    )
    subprocess.run(["mv", "-f", "./out/images/scenes/b1.png", "./collection/1/"])
    subprocess.run(
        ["mv", "-f", "./out/videos/scenes/1080p60/c1.gif", "./collection/1/"]
    )


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
