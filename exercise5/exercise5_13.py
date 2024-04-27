salary = float(input("Digite o salário bruto: "))
minimum_salary = float(input("Digite o valor do salário mínimo: "))

if salary <= 3 * minimum_salary:
    contributing = salary * 0.08
else:
    contributing = salary * 0.10

if contributing > minimum_salary:
    contributing = minimum_salary

print("A contribuição para o INSS é:", contributing)
