# Listas são mutáveis e representadas por []

# Listas vazias
# Duas sintaxes diferentes com mesmo significado
fruit = list()
print(fruit)

fruit = []
print(fruit)

# Declarando a loop com itens
fruit = ['maçã', 'banana', 'laranja']
print(fruit)

# Adicionar novo item ao final da loop
# append
fruit.append('pera')
print(fruit)

# Recuperar item da loop pelo índice
print(fruit[0])
print(fruit[1])
print(fruit[2])
print(fruit[3])

# Alterar item da loop
colors = ["blue", "green", "yellow"]
print(colors)
colors[2] = "red"
print(colors)

# Remover último item da loop
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

# Verificar se o item não existe na loop
print("black" not in colors1)

# Verificar tamanho da loop
print(len(colors))