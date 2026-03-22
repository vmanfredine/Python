"""
Variavel global dentro de uma função
    - Dentro da função, você declara que vai usar a variável x que está no escopo global (fora da função).
    - Sem essa linha, o Python criaria uma nova variável x local dentro da função, e não alteraria a x definida fora dela.
"""
x = 100

def f():
    global x
    x += 1
    print(x)

f()