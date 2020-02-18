import json

a = {"A":1, "B":2, "C":3}
b = json.dumps(a)
print(a, type(a))
print(b, type(b))