from abc import ABC, abstractmethod, abstractproperty

# O módulo abc é um módulo nativo do python usado para
# criação de métodos e classes abstratas.

# Classes abstratas são usadas para que tenhamos padrões para 
# as classes que herdam os métodos da classe abstrata/classe mãe
# Ou seja, garantindo que a classe filha tenha alguns elementos da 
# classe pai. Assim, sendo útil para os comportamentos polimórficos 
# de algumas classes.


class ControleRemoto(ABC):
    # Usando o @abstractmethod definimos que as classes filhas
    # tem que implementar os métodos da classe pai.
    
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    # Definimos que tem que ter o atributo marca, e não é 
    # método e sim um atributo pois estamos tornando ele uma propety.

    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    # Como herdou a classe Controle Remoto, e a classe Controle Remoto
    # é abstrata, tem que implementar, todos os métodos e propriedades abstratas
    # definidas em Controle Remoto.

    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        return "Philco"


class ControleArCondicionado(ControleRemoto):
    # Como herdou a classe Controle Remoto, e a classe Controle Remoto
    # é abstrata, tem que implementar, todos os métodos e propriedades abstratas
    # definidas em Controle Remoto.
    
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)


controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)
