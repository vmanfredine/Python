"""
Crie um programa que exibe em tela a tabuada
de um determinado número fornecido pelo usuário
"""
x = int(input("Insira um número para exibir a tabuada: "))

for num in range(1, 11):
    print(f"{x} x {num} = {x*num}")