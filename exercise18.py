salario_liquido = float(input("Digite o salário líquido após a dedução da contribuição ao INSS: "))

if salario_liquido <= 900:
  desconto_irrf = 0
elif salario_liquido <= 1800:
  desconto_irrf = salario_liquido * 0.15 - 135
else:
  desconto_irrf = salario_liquido * 0.275 - 360

salario_liquido -= desconto_irrf

print("O desconto do IRRF é:", desconto_irrf)
print("O salário líquido após o desconto do IRRF é:", salario_liquido)