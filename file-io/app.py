with open("test.txt", "r+") as f:
    d = f.readlines()
    f.seek(0)
    for i in d:
        if 'x' in i:
            f.write(i)
    f.truncate()