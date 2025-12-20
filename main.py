import subprocess

if __name__ == "__main__":
    """
    The note1 name should be dynamically generated when generating the whole collection.
    Each complete scene is argonized into:
    a: write animation
    b: static image
    c: fadeout animation
    """
    subprocess.run([
        "manim", 
        "--quality", "h",
        "--resolution", "1920,1080",
        "--config_file", "manim.cfg",
        "--output_file", "a1",
        "--media_dir", "./out",
        "scenes.py", "WriteAnimation"
    ])
    subprocess.run([
        "manim", 
        "--quality", "h",
        "--resolution", "1920,1080",
        "--config_file", "manim.cfg",
        "--output_file", "b1",
        "--media_dir", "./out",
        "scenes.py", "Image"
    ])
    subprocess.run([
        "manim", 
        "--quality", "h",
        "--resolution", "1920,1080",
        "--config_file", "manim.cfg",
        "--output_file", "c1",
        "--media_dir", "./out",
        "scenes.py", "FadeoutAnimation"
    ])
    """
    Postprocessing
    """
    subprocess.run([
        "mkdir", "./collection/1"
    ])
    subprocess.run([
        "mv", "-f", "./out/videos/scenes/1080p60/a1.mp4", "./collection/1/"
    ])
    subprocess.run([
        "mv", "-f", "./out/images/scenes/b1.png", "./collection/1/"
    ])
    subprocess.run([
        "mv", "-f", "./out/videos/scenes/1080p60/c1.mp4", "./collection/1/"
    ])
