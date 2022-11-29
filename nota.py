n1, n2 = (5.6, 2.3)

media = (n1 + n2) / 2

if media >= 7:
    print(f"Aluno APROVADO com media: {media :.2f}")
elif (media < 7) and (media >= 4.5):
    print(f"Aluno em RECUPERAÇÃO com media: {media :.2f}")
else:
    print(f"Aluno REPROVADO com media: {media :.2f}")    