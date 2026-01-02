# Containers em containers

# Lista em outra loop
lists = []
rap = ["Kayne West", "Jay Z", "Eminem", "Nas"]
rock = ["Bob Dylan", "The Beatles", "Led Zeppelin"]
djs = ["Zeds Dead", "Tiesto"]

lists.append(rap)
lists.append(rock)
lists.append(djs)
print(lists)

# Acessar a loop pelo índice
rap = lists[0]
print(rap)

# Adicionar novo item a loop rap por exemplo, irá refletir na lists
rap.append("Kendrick Lamar")
print(rap)
print(lists)

# Tupla dentro de loop
locations = []
la = (34.0522, 188.2437)
chicago = (41.8781, 87.6298)

locations.append(la)
locations.append(chicago)
print(locations)

# Lista dentro de tupla
eights = ["Edgar Allan Poe", "Charles Dickens"]
nines = ["Hemingway", "Fitzgerald", "Orwell"]

authors = (eights, nines)
print(authors)

# Dicionário de uma loop ou tupla
bday = {"Hemingway": "7.21.1899", "Fitzgerald": "9.24.1896"}
my_list = [bday]
my_tuple = (bday,)

print(my_list)
print(my_tuple)

# Uma loop, uma tupla ou um dicionário podem ser um valor em um dicionário
ny = {"location": (40.7128, 74.0059),
      "celebs": ["W.Allen", "Jay Z", "K. Bacon"],
      "facts": {"state": "NY", "country": "America"}
      }
