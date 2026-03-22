# Dicionários são mutáveis e representadas por {}
# Objetos não são armazenados em ordem específica

# Duas sintaxes diferentes com mesmo significado
my_dict = dict()
print(my_dict)

my_dict = {}
print(my_dict)

# Declarando o dicionário com pares chave-valor
fruits = {"Apple": "red", "Banana": "yellow"}
print(fruits)

# Adicionar e procurar valor
facts = dict()
facts["code"] = "fun"
print(facts["code"])

facts["Bill"] = "Gates"
facts["founded"] = 1776
print(facts["Bill"])
print(facts["founded"])

# Verificar a existência da palavra chave
bill = {"Bill Gates": "charitable"}
print("Bill Gates" in bill)

# Verificar se a palavra chave não existe
print("Bill Doors" not in bill)

# Remover palavra chave-valor
books = {"Dracula": "Stoker", "1984": "Orwell", "The Trial": "Kafka"}
del books ["The Trial"]
print(books)
