lista = [1, 4, 5, 7, 9, 12, 23, 50, 54, 25]

entrada_usuario = int(input("Adivinhe um número que está na lista ou digite'q' para sair: "))

while entrada_usuario != 'q':
    if entrada_usuario in lista:
        print('Você acertou!')
        break
    else:
        print('Tente novamente!')
        break