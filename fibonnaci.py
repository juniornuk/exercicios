n = 20
lista = [0, 1]
for i in range(n):
    lista.append(lista[i] + lista[i + 1])
print(lista)