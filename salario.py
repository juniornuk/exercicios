#quanto ganha por hora
#numero de horas trabalhadas mes
#quanto ganha por mes
#descontado 11% de imposto de renda
#descontado 8% de INSS
#desconto de 5% para sindicato

#salario bruto
#quanto pagou de INSS
#quando pagou ao sindicato
#salario liquido

valor_hora = float(input("Quanto ganha por hora: "))
horas_mes = 6 * 22

salario_bruto = valor_hora * horas_mes

valor_ir = salario_bruto * 0.11
valor_inss = (salario_bruto - valor_ir) * 0.08
valor_sindicato = (salario_bruto - valor_ir - valor_inss) * 0.05

salario_liquido = salario_bruto - (valor_ir + valor_inss + valor_sindicato)

print(f"Seu salario_bruto é: {salario_bruto:.2f}")
print(f"Seu salario_liquido é: {salario_liquido:.2f}")
print(f"pagou de IR {valor_ir:.2f}")
print(f"pagou de INSS {valor_inss:.2f}")
print(f"pagou ao sindicato {valor_sindicato:.2f}")


