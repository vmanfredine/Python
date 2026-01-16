try:
    a = int(input("Type a number: "))
    b = int(input("Type another: "))
    print(a / b)

# Um único except para ambos os erros
except (ValueError, ZeroDivisionError):
    # Se b for 0, a operação gera ZeroDivisionError. O programa imprime a mensagem em vez de quebrar.
    # Se o valor digitado for errado para as funções internas int, str ou float, gera ValueError. O programa imprime a mensagem em vez de quebrar.
    print("Invalid input")