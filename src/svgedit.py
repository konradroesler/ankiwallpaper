"""
Inserts fill='white' into the svg tag of all svgs inside
the svgs directory, effectively making all text white.
"""

if __name__ == "__main__":
    import os
    import xml.etree.ElementTree as ET

    directory_path = "./../svgs"
    directory = os.fsencode(directory_path)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".svg"):
            path_to_file = f"{directory_path}/{filename}"
            tree = ET.parse(path_to_file)
            root = tree.getroot()
            root.set("fill", "white")
            tree.write(path_to_file, encoding="utf-8", xml_declaration=True)
