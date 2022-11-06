#%%
class Foo:
    def hello(self):
        print(self.__class__.__name__.lower())


class Bar(Foo):
    def hello(self):
        return super().hello()


bar = Bar()
bar.hello()

# Utilizando o método da classe pai

#%%
class Foo:
    def __init__(self, x = None):
        self._x = x
    def x(self):
        return self._x or 0

foo = Foo(100)
print(foo.x())

# Só é possível utilizar a sintaxe de método e não de atributo
# Por isso usamos o @property, para não perder essa propriedade.

# %%
