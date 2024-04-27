products = {}
for i in range(4):
  nome = input(f"Digite o nome do produto {i+1}: ")
  quantity = int(input(f"Digite a quantidade em estoque do produto {i+1}: "))
  products[nome] = quantity

for produto, quantity in products.items():
  if quantity < 30:
    print(f"O produto {produto} está abaixo do estoque mínimo.")