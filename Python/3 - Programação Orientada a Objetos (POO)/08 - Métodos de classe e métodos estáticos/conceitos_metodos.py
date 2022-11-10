#%%
from inspect import signature
def default_to_none(func):
    sig = signature(func)
    newparams = [param.replace(default=None) for param in signature(func).parameters.values() if str(param) not in ['self', '**kwargs', '*']]
    newsig = sig.replace(parameters=newparams)
    def inner(*args, **kwargs):
        arguments = newsig.bind(*args, **kwargs)
        arguments.apply_defaults()
        return func(**arguments.arguments)
    return inner

class Persona():
    def __init__(self):
        pass 
    
    @default_to_none
    def change_characteristics(self, *, name, text, **kwargs):
        self.name = kwargs.get('name', name)
        self.text = kwargs.get('text', text)

    def change_general_characteristics(self, *, nome, idade, profissao, **kwargs):
        self.nome = kwargs.get('nome', nome)
        self.idade = kwargs.get('idade', idade)
        self.profissao = kwargs.get('profissao', profissao)
#%%
class MapperPersona():
    def __init__(self):
        pass

    @staticmethod
    def toEntity(data):
        pessoa = MapperPersona()
        pessoa.generation(data)
        pessoa.general_characteristics(data)
        persona = Persona()
        persona.change_general_characteristics(nome = pessoa.nome, idade = pessoa.idade, profissao = pessoa.profissao)
        # persona.change_characteristics(name = pessoa.name, text = pessoa.text)
        return persona

    def generation(self, data):
        self.name = 'Baby Boomers'
        self.text = 'Gosta do Zap'
        
    def general_characteristics(self, data):
        self.nome = 'Vitor'
        self.idade = 22
        self.profissao = 'Cientista'

#%%
    

class MapperPersona():

    @staticmethod
    def toEntity(data):
        generation_data = __class__.generation(data)
        general_characteristics = __class__.general_characteristics(data)
        persona = Persona()
        persona.change_general_characteristics(**general_characteristics)
        # persona.change_characteristics(**generation_data)
        return persona

    @staticmethod
    def generation(data):
        name = 'Baby Boomers'
        text = 'Gosta do Zap'
        return {'name' : name, 'text' : text}
        
    @staticmethod
    def general_characteristics(data):
        nome = 'Vitoria'
        idade = 22
        profissao = 'Cientista'
        return {'nome' : nome, 'idade' : idade, 'profissao' : profissao}



#%%
@default_to_none
def f(*, foo, bar, **kwargs):
    print('omg')
    foo = kwargs.get('foo', foo)
    bar = kwargs.get('bar', bar)
    return foo, bar

# %%
