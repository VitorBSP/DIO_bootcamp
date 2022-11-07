class Estudante:
    escola = "DIO" # Atributos de classe
    # Atributos de classe => definidos antes de qualquer método

    def __init__(self, nome, matricula):
        # Atributos de instância => definidos com self, após
        # a definição de algum método
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

# Cada objeto tem seu próprio valor de atributos de instância
# Cada um com uma cópia única por objeto

aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovanna", 2)
mostrar_valores(aluno_1, aluno_2)

aluno_1.escola = 'UFSM' #alterando atributo de instância, da instância aluno 1
Estudante.escola = "Python"  #alterando atributo de classe, da classe Estudante
Estudante.nome = 'Vitor' # Não altera nada, pois o SELF define que o atributo é de 
                        # instância e desse jeito queremos mudar o atributo de classe
aluno_3 = Estudante("Chappie", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)

#%%
import string
letras = string.ascii_lowercase
letras.index('a')
# %%
reajuste = 1.234
reajuste = '%.2f' % reajuste
reajuste = str(reajuste).replace('.', ',')
# %%

salario = 2000
percentual = 0.10
novo_salario = salario*(1+percentual)
reajuste = novo_salario - salario
novo_salario = ('%.2f' % novo_salario).replace('.', ',')
reajuste = ('%.2f' % reajuste).replace('.', ',')
print(f'Novo salario: {novo_salario} Reajuste ganho: {reajuste} Em percentual: {int(percentual*100)} %')
# %%
