age = int(input("Digite a idade do nadador: "))
if 5 <= age <= 7:
  print("Infantil A")
elif 8 <= age <= 10:
  print("Infantil B")
elif 11 <= age <= 13:
  print("Juvenil A")
elif 14 <= age <= 17:
  print("Juvenil B")
elif 18 <= age <= 60:
  print("Adulto")
else:
  print("Senior")
