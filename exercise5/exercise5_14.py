salario_bruto = float(input("Digite o salário bruto: "))
salario_minimo = float(input("Digite o valor do salário mínimo: "))

if salario_bruto <= 3 * salario_minimo:
    contribuicao = salario_bruto * 0.08
else:
    contribuicao = salario_bruto * 0.10

if contribuicao > salario_minimo:
    contribuicao = salario_minimo

salario_liquido = salario_bruto - contribuicao

print("A contribuição para o INSS é:", contribuicao)
print("O salário líquido é:", salario_liquido)
