def entrada(tipo):
    if tipo == "nome":
        return input("Inorme seu nome ")

    if tipo == "idade": 
        return int(input("Informe sua idade: "))

    if tipo == "salario":
        return float(input("Informe seu salario"))

    if tipo == "sexo": 
        return input("Informe seu sexo: ")

    if tipo == "ecivil":
        return input("Informe seu estado civil: ")



valor = entrada("nome")

while len(valor) < 3:
    valor = entrada("nome")

valor = entrada("idade")
while valor not in range(151):
    valor = entrada("idade")

valor = entrada("salario")
while valor < 0:
    valor = entrada("salario")

valor = entrada("sexo")
while valor not in ["m", "f"]:
    valor = entrada("sexo")    e

valor = entrada("ecivil")
while valor not in ["s", "c", "v", "d"]:
    valor = entrada("ecivil")    