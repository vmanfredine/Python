# Declaração de Classe
class Pessoa:
    def __init__(self): # Método Construtor
        # Atributos de Instância
        self.nome = ""
        self.idade = 0

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} tem {self.idade} anos."

# Declaração de Objetos
p1 = Pessoa()
p1.nome = "Vitor"
p1.idade = 30
p1.aniversario()
print(p1.mensagem())

p2 = Pessoa()
p2.nome = "Natália"
p2.idade = 29
print(p2.mensagem())

p3 = Pessoa()
p3.nome = "Helena"
p3.idade = 1
print(p3.mensagem())