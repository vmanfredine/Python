#Escreva um programa que faça uma pergunta e salve a resposta em um arquivo
awnser = input("Digite seu nome: ")

with open("C:\\Users\\XXXX\\Downloads\\exe 02.txt", "w") as f:
    f.write(awnser)
