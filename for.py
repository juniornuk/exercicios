for n in range(10):
  print(n)


#list compreension
lista = list((n) for n in range(10)   if (n % 2) != 0)
print (lista)


#funcao lambda
quadrado = lambda x: x ** 2
print (quadrado(7))