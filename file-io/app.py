with open("test.txt", "r+") as f:
    file_rewrite = []
    lines = f.readlines()
    for line in lines:
        if 'a' not in line.lower():
            file_rewrite.append(line)
    f.truncate(0)
    f.seek(0)
    for line in file_rewrite:
        f.write(line)
