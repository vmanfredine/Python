# Tuplas são imutáveis e representadas por ()

# Tuplas vazias
# Duas sintaxes diferentes com mesmo significado
my_tupple = tuple()
print(my_tupple)

my_tupple = ()
print(my_tupple)

# Adicionar objetos
rndm = ("M. Jackson", 1958, True)
print(rndm)

# Tupla com apenas 1 objeto, adicionar , após o  elemento
new_tupple = ("Manfredine",)
print(new_tupple)

# Acessar itens da tupla
dys = ("1984", "Brave New World", "Fahreinheit 451")
print(dys[2])

# Verificar existência de um item
print("1984" in dys)

# Verificar se o item não existe
print("Handmaid's Tale" not in dys)