class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Gato(Mamifero):
    pass

class corMixin:
    def cores(self):
        return f"O ornitorrinco tem essas cores {self.cor_pelo} e {self.cor_bico}"
    # Mixins são úteis para adicionar comportamentos as classes de forma desacoplada em questão de ordem
    # Não importa a ordem de execução do Mixin, antes ou depois de qual classe.
    # Muito utilizado em DJANGO no desenvolvimento web (construção de aplicações)

class Ornitorrinco(Mamifero, Ave, corMixin):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        super().__init__(cor_bico=cor_bico, cor_pelo=cor_pelo, nro_patas=nro_patas)

    def order(self):
        # Informa a ordem de classes que vai executar.
        # Respeita a ordem que foi enviada como parâmetro na classe.
        print(Ornitorrinco.__mro__)




gato = Gato(nro_patas=4, cor_pelo="Preto")
print(gato)

ornitorrinco = Ornitorrinco(nro_patas=2, cor_bico="laranja", cor_pelo="vermelho")
print(ornitorrinco)
ornitorrinco.order()
print(ornitorrinco.cores())
