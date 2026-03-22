list =  ["The", "fox", "jumped", "over", "the", "fence", "."]
list = " ".join(list)
list = list[0: -2] + "." # Pega o texto do início (0) até o penúltimo caractere (-2). Remove os dois últimos caracteres da string atual (o espaço e o ponto original) e adiciona um novo ponto final logo após o corte.
print(list)
