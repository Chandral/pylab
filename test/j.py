import string

BASE_STRING = "ira"
for lc in string.ascii_lowercase:
    for UC in string.ascii_uppercase:
        print(UC + BASE_STRING + lc)