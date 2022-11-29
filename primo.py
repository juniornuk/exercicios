n = int(input(f"Enter the number: "))

check = 0

for i in range(2, n):
    if n % i == 0:
        check = 1

if check == 0:
    print(f"O numero {n} é primo")
else:
    print(f"O numero {n} não é primo")