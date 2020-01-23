import random, string

file = open("test.log", 'a')
chars = string.ascii_letters + string.digits + string.punctuation
for i in range(0, 10):
    file.write(random.choice(chars))
