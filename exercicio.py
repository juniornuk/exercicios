tu = (1, 2, 3, 4, 5)
a, b, c, d, e = tu
print(tu[::-1])
print(type(c))

a, b, c = (2, 4, 6)
if a > b:
    if a > c:
        print(f"{a} é maior")
    else:
        print(f"{c} é maior")    

elif b > c:
    print(f"{b} é maior")
else:
    print(f"{c} é maior")    


nome = "Osmar"
valor = ""
for i in nome:
    valor = valor + i
    print(valor)


carros = [("Creta", 150),("Fiat Mobi", 75),("HB20 Sedan",100)]

for x in carros:
    print(f"Carro {x[0]}, valor de locacao {x[1]}")

