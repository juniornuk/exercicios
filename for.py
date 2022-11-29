for n in range(10):
  print(n)

lista = list((n) for n in range(10)   if (n % 2) != 0)
print (lista)

quadrado = lambda x: x ** 2
print (quadrado(7))