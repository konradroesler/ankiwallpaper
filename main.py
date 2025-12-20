import subprocess

if __name__ == "__main__":
    """
    The note1 name should be dynamically generated when generating the whole collection.
    """
    subprocess.run([
        "manim", 
        "--quality", "h",
        "--resolution", "1920,1080",
        "--config_file", "manim.cfg",
        "--output_file", "write1",
        "--media_dir", "./out",
        "scenes.py", "WriteAnimation"
    ])
