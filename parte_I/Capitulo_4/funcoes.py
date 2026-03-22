def f(x):
    return x * 2

result = f(2)
print(result)

# Função sem parâmetro
def g():
    return 1 + 1

result = g()
print(result)

# Função com mais de um parâmetro
def h(x,y,z):
    return x + y + z

result = h(1,2,3)
print(result)

# Função sem return
def i():
    z = 1 + 1

result = i()
print(result)

# Função com parâmetro opcional
def j(x=2):
   return x**x
print(j())
print(j(4))

# Função com parâmetro obrigatório e opcional
def add_it(x, y=10):
    return x + y

result = (add_it(2))
print(result)