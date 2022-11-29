n = 10
lista = [0, 1]
for i in range(10):
    lista.append(lista[i] + lista[i + 1])
print(lista)