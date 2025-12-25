import re

with open("Lernen.txt", "r") as file:
    result = []
    lines = file.readlines()
    for line in lines:
        found = re.findall(r"\\[A-Za-z]+", line)
        for find in found:
            if find not in result:
                result.append(find)
    print(result)
