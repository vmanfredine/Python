from rich import print
from rich.panel import Panel
from rich.text import Text

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        texto_justificado = Text(f"{self.nome}\n------------------------------ \n..........R${self.preco}...........", justify="center")
        print(Panel(texto_justificado, title="Produto", width=35))

p1 = Produto("MacBook Pro", 10_000.00)
p1.etiqueta()

p2 = Produto("iPhone 17 Pro Max", 8_000.00)
p2.etiqueta()