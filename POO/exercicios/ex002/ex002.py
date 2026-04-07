# Declaração de Classe
class Pessoa:
    """
    Essa classe cria uma pessoa, que contém nome e idade
    Para criar uma nova pessoa, use: variavel = Pessoa(nome, idade)
    """
    def __init__(self, nome = "vazio", idade = 0): # Método Construtor
        # Atributos de Instância
        self.nome = nome
        self.idade = idade

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def __str__(self): # Dunder Method
        return f"{self.nome} tem {self.idade} anos."

    def __getstate__(self):
        return f"Estado: nome = {self.nome}; idade = {self.idade}"

# Declaração de Objetos
p1 = Pessoa("Vitor", 30)
p1.aniversario()
print(p1)

p2 = Pessoa("Natália", 29)
print(p2.__getstate__())

p3 = Pessoa()
print(p3)