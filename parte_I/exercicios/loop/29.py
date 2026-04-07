"""
Crie um programa que lê um valor de início e um valor de
fim, exibindo em tela a contagem dos números dentro desse
intervalo
"""
num_1 = int(input("Insira um número: "))
num_2 = int(input("Insira outro número: "))

for i in range(num_1, num_2+1):
    print(i)