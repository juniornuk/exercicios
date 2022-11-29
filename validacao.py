def entrada(tipo):
    if tipo == "nome":
        print("nome não pode ser menor que 3 caracteres")
        return input("Inorme seu nome: ")

    if tipo == "idade": 
        print("Idade deve estar entre 0 e 150")
        return int(input("Informe sua idade: "))

    if tipo == "salario":
        print("Valor do salario tem que ser maior que zero")
        return float(input("Informe seu salario: "))

    if tipo == "sexo": 
        print("Digitar (m) para masculinoe (f) para feminino")
        return input("Informe seu sexo: ")

    if tipo == "ecivil":
        print("digitar (s) para solteiro, (c) para casado, (v) para viuvo e (d) para divorciado")
        return input("Informe seu estado civil: ")



valor = ""
while len(valor) <= 3:
    nome = entrada("nome")
    valor = nome

valor = -1
r = range(151)
while valor not in r:
    idade = entrada("idade")
    valor = idade

valor = -1
while valor < 0:
    salario = entrada("salario")
    valor = salario

valor = ""
while valor not in ["m", "f"]:
    sexo = entrada("sexo")
    valor = sexo

valor = ""
while valor not in ["s", "c", "v", "d"]:
    ecivil = entrada("ecivil")    
    valor = ecivil


print("\n")
print(f"nome: {nome}")
print(f"idade: {idade}")
print(f"salario: {salario}")
print(f"sexo: {sexo}")
print(f"estado civil: {ecivil}")