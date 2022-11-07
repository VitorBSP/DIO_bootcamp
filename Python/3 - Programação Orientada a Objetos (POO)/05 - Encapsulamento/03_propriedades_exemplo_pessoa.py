class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def idade(self):
        _ano_atual = 2022
        return _ano_atual - self._ano_nascimento
    
    @property
    def nome(self):
        return self._nome
    
    def get_nome(self):
        return self._nome
    
    def get_idade(self):
        _ano_atual = 2022
        return _ano_atual - self._ano_nascimento



pessoa = Pessoa("Guilherme", 1994)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")
print(f"Nome: {pessoa.get_nome()} \tIdade: {pessoa.get_idade()}")

# Os dois jeitos funcionam!
# Mas o primeiro é melhor, tem mais a "cara" e o padrão de boas práticas
# da orientação ao objeto no python.

# É mais pythonic utilizarmos o setter quando vamos utilizar alguma lógica
# para alterar o valor do atributo. 

# Lembre-se a parte de encapsulamento, tirando os decorators, são convenções
# e boas prática não regras da linguagem.
