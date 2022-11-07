class Foo:
    def __init__(self, x=None):
        self._x = x

    # Property altera a sintaxe de método para atributo
    @property
    def x(self):
        return self._x or 0

    # Setter não retorna valor, apenas define o valor do objeto
    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = 0


foo = Foo(10)
print(foo.x)
del foo.x
print(foo.x)
foo.x = 10
print(foo.x)
