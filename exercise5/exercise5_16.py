salario_bruto = float(input("Digite o salário bruto: "))
salario_minimo = float(input("Digite o valor do salário mínimo: "))

if salario_bruto <= 3 * salario_minimo:
    contribuicao = salario_bruto * 0.08
else:
    contribuicao = salario_bruto * 0.10

if contribuicao > salario_minimo:
    contribuicao = salario_minimo

salario_liquido = salario_bruto - contribuicao

if salario_liquido <= 900:
    desconto_irrf = 0
elif salario_liquido <= 1800:
    desconto_irrf = salario_liquido * 0.15 - 135
else:
    desconto_irrf = salario_liquido * 0.275 - 360

salario_liquido -= desconto_irrf

print("A contribuição para o INSS é:", contribuicao)
print("O desconto do IRRF é:", desconto_irrf)
print("O salário líquido é:", salario_liquido)
