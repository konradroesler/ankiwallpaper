if __name__ == "__main__":
    import os
    import hashlib

    directory_path = "./svgs"
    directory = os.fsencode(directory_path)

    file_names = []
    got_em = False

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".svg"):
            file_names.append(filename)

    uid = b"K7hdsQ+[]G"
    hash = hashlib.md5(uid).hexdigest()
    for name in file_names:
        if hash in name:
            got_em = True
    print(got_em)
    print(hash)
