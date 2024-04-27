name = input("Insira seu nome: ")
sex = input("Insira seu gênero (M/F): ")
marital_status = input("Insira seu estado civil: ")

if sex == "F" and marital_status == "CASADA":
  years_married = input("Insira o número de anos de casado: ")
  print(f"{name}, você está casado há {years_married} anos.")
else:
  print(f"Oioi, {name}.")