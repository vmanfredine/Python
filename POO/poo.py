class Orange:
    def __init__(self,w,c):
        self.weight = w
        self.color = c
        print("Criado!")

or1 = Orange(10, "darkorange")
print(or1)

"""
NÃo é obrigatório ter um método construtor (__init__) em uma classe Python. 
Se não escrever um __init__, o Python usará um construtor padrão (vazio) por baixo dos panos. No entanto, a utilidade da classe muda dependendo da presença dele.

def __init__(self, w, c) -> método construtor. Ele é executado automaticamente sempre que criado uma nova "instância" (uma nova laranja).

self -> Representa a própria instância que está sendo criada. É o que permite ao objeto acessar seus próprios dados.

w e c -> São os parâmetros (peso e cor) que é passado ao criar a laranja.

or1 = Orange(10, "darkorange") -> está instanciando a classe.

10 vai para o parâmetro w.

"darkorange" vai para o parâmetro c.
"""