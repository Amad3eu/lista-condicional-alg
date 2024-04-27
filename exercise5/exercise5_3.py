grades = [float(input(f"Digite a nota {i+1}: ")) for i in range(4)]
average = sum(grades) / len(grades)
if average >= 5:
  print("O aluno foi aprovado. Média: ", average)
else:
  print("O aluno foi reprovado. Média: ", average)


