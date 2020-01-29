class Link:
    def __init__(self):
        self.j = "asdf"


    @property
    def J_IS(self):
        return self.j

a = Link()
print(a.J_IS)