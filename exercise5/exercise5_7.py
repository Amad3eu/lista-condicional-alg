import cmath
a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = float(input("Digite c: "))
if a == 0:
  print("Não é uma equação do segundo grau")
else:
  d = (b**2) - (4*a*c)
  sol1 = (-b-cmath.sqrt(d))/(2*a)
  sol2 = (-b+cmath.sqrt(d))/(2*a)
  print("As soluções são {0} e {1}".format(sol1,sol2))