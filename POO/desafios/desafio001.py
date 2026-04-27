from rich import print

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f":handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da Empresa XXX"

func1 = Funcionario("Vitor", "TI", "Analista de processos")
print(func1.apresentacao())

func2 = Funcionario("Pedro", "Administração", "Diretor")
print(func2.apresentacao())