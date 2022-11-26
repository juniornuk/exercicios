#instruções
# cada litro pinta 3 m2
# cada lata contem 18L
# cada lata custa 80 reais

area = int(input("Qual o valor da area a ser pintada: "))

litros = area / 3
valor = round(litros / 18)
total_la = litros / 18
valor_latas = valor * 80


print(f"Para pintar: {area} m2 são necessários {total_la :.2f} litros e custará R$ {valor_latas :.2f}")