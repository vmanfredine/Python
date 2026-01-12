#gravação de arquivos
import os
import csv

os.path.join("Users", "vitor", "st.txt")

st = open("st.txt", "w")
st.write("Hi from Python!")
st.close()

# fechamento automático de arquivos
with open("st.txt", "w") as f:
    f.write("Hi from Python, again!")

# leitura em arquivos
with open("st.txt", "r") as f:
    print(f.read())

# gravar em uma lista
my_list = []
with open("st.txt", "r") as f:
    my_list.append(f.read())
print(my_list)

# Arquivo CSV
# O programa abaixo criará um novo arquivo chamado st.csv
with open("st.csv", "w", newline="") as f:
    w = csv.writer(f,
                   delimiter=",")
    w.writerow(["one",
                "two",
                "three"])
    w.writerow(["four",
                "five",
                "six"])

# Ler arquivo CSV
with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(row)