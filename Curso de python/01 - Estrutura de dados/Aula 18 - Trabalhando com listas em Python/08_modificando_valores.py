numeros = [1, 30, 21, 2, 9, 65, 34]

# versão 1
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

print(quadrado)

# versão 2
cubo = [numero ** 3 for numero in numeros]

print(cubo)