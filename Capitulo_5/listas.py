# Listas são mutáveis e representadas por []

# Listas vazias
# Duas sintaxes diferentes com mesmo significado
fruit = list()
print(fruit)

fruit = []
print(fruit)

# Declarando a lista com itens
fruit = ['maçã', 'banana', 'laranja']
print(fruit)

# Adicionar novo item ao final da lista
# append
fruit.append('pera')
print(fruit)

# Recuperar item da lista pelo índice
print(fruit[0])
print(fruit[1])
print(fruit[2])
print(fruit[3])

# Alterar item da lista
colors = ["blue", "green", "yellow"]
print(colors)
colors[2] = "red"
print(colors)

# Remover último item da lista
print(colors)
item = colors.pop() # item que foi removido foi salvo na variável 'item'
print(item)
print(colors)

# Combinar listas
colors1 = ["blue", "green", "yellow"]
colors2 = ["red", "orange", "black"]
print(colors1 + colors2)

# Verificar existência de um item
print("green" in colors1)

# Verificar se o item não existe na lista
print("black" not in colors1)

# Verificar tamanho da lista
print(len(colors))