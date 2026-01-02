x = 10
while x > 0:
    # print('{}'.format(x))
    print(x)
    x -= 1
print("Happy New Year")

# break: encerra o loop
for i in range(0, 100):
    print(i)
    break

# continue: interrompe a iteração e passa para a próxima
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

# Loop aninhado
for i in range(1, 3):
   print(i)
   for letter in ["a", "b", "c"]:
       print(letter)

while input('y or n? ') != 'n':
    for i in range (1,6):
        print(i)