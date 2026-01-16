# Multiplicação de strings
from plotly.express import strip

name = "Vitor" * 3
print(name)

# Alterar maiúscula para minúscula e vice-versa
name = "Vitor Manfredine"
print(name.upper())
print(name.lower())
print(name.capitalize())

# Método format
name = "William {}".format("Faulkner")
print(name)

last = "Faulkner"
name = "William {}".format(last)
print(name)

# Dividir string
word = "Hello Yes!".split(" ")
#word = "Hello.Yes!".split(".")
print(word)

# Método join
first_three = "abcd"
result = "+".join(first_three)
print(result)

# join com string vazia
words = ["The",
         "fox",
         "jumped",
         "over",
         "the",
         "fence",
         "."]
one = "".join(words)
print(one)

# Remoção de espaços
s = "    The     "
s = s.strip()
print(s)

# Método replace
equ = "All animals are equal."
equ = equ.replace("a", "@")
print(equ)

# Buscar um índice
indice = "animals".index("m")
print(indice)

# Palavra chave in
print("Cat" in "Cat in the hat")
print("Bat" in "Cat in the hat")

# Not in
print("Potter" not in "Harry")

# Escape de string
print("She said \"Surely\"")
print("She said 'Surely'")
print('She said "Surely"')

# Nova linha
print("line1\nline2\nline3")

# Fatiamento
fict = ["Tolstoy", "Camus", "Orwell", "Huxley", "Austin"]
print(fict[0:3])

ivan = """In place of death there\
 was light."""
print(ivan[0:17])
print(ivan[17:33])

# indice "vazio"
my_name = "Vitor Manfredine Coelho"
print(my_name[:17])
print(my_name[17:])