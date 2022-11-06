class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, marcha):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = marcha

    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmm...")

    # Benefício de usar referência explícita
    # É para simplificar o uso de closures
    def trocar_marcha(self, nro_marcha):
        def _trocar_marcha():
            if nro_marcha  > self.marcha:
                print("Marcha trocada...")
                self.marcha  = nro_marcha
            else: 
                print('Não foi possível trocar de marcha')

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
print(b2)
b2.correr()
