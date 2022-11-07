class Pessoa:
    def __init__(self, nome = None, idade = None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18
    
    #Método de classe 

    def criar_apartir_data_nascimento(self, ano, mes, dia, nome):
        # Quando temos um método que cria a classe de outra forma
        # Chamamos ele de:
        # Método de Fábrica / Método de classe
        # Não cria uma instância atoa.
        idade = 2022 - ano
        return Pessoa(nome, idade)

p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")
print(p.nome, p.idade)
p1 = Pessoa().criar_de_data_nascimento(1994, 3, 21, "Guilherme")
print(p1.nome, p1.idade)
# Qual a desvantagem da segunda forma?
# Primeira é que temos que definir valores nulos no instanciamento
# da classe, pois a classe precisa dos atributos para a sua inicialização/criação
# se eles não forem definidos ou terem valores default vai dar erro.
# No entanto, o objetivo é criar a classe a partir do ano de nascimento
# sem informar previamente a idade, assim não faz sentido definir os valores na
# criação.

# O segundo é o mais importante, é estariamos instanciando duas vezes a classe
# Pessoa me p1, um quando faz a chamada "Pessoa()" e a outra no método de classe
# criar_de_data_nascimento() onde é realizada outra instancia de pessoa, apesar
# de só retornar uma, no entanto, algoritmicamente criou duas, prejudicando a 
# performance.

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))
