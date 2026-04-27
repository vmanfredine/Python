from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self, titulo, quant_pessoas):
        self.titulo = titulo
        self.quant_pessoas = quant_pessoas

    def analisar (self):
        kg_total = self.quant_pessoas * 0.4
        custo_total = kg_total * 82.40
        custo_pessoa = custo_total / self.quant_pessoas

        return Panel(f"Analisando [green]{self.titulo}[/] com [blue]{self.quant_pessoas} convidados[/]\n"
                f"Cada participante comerá 0.4kg e cada Kg custa R$82.40\n"
                f"Recomendo [blue]comprar {kg_total}Kg[/] de carne\n"
                f"O custo total será de [green]R${custo_total:.2f}[/]\n"
                f"Cada pessoa pagará [yellow]R${custo_pessoa:.2f}[/] para participar", title=self.titulo,width=60)

c1 = Churrasco("Churras dos Amigos", 15)
print(c1.analisar())