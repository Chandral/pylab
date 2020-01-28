import inspect

class Checker:
    def __init__(self):
        self._age = 10

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, val):
        print(inspect.stack()[1].function)
        self._age = val


a = Checker()
print(a.age)
a.age = 33
print(a.age)