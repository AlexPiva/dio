# range(stop) -> range object
# range(start, stop[, steo]) -> range object

print(list(range(4)))

# utilizando range com for

for numero in range (0, 11):
    print(numero, end=' ')

print()

#exibindo a tabuada do 5
for numero in range(0, 51, 5):
    print(numero, end=' ')