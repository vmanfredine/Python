from rich import print

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        print(f":book: [blue]Você acabou de  abrir o livro [red]'{self.titulo}'[/] que tem [green]{self.paginas} páginas[/] no total. Você está agora na [yellow]página 1[/].[/blue]")

    def avancar_paginas(self, paginas_lidas):
        if paginas_lidas > self.paginas:
            print(f":warning: Você chegou ao final do livro '{self.titulo}'")
        else:
            print(f"Você avançou {paginas_lidas} páginas e agora está na página {paginas_lidas + 1}")

l1 = Livro("O Boneco de Neve", 20)
l1.avancar_paginas(10)
l1.avancar_paginas(20)