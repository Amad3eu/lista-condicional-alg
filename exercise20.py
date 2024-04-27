# exercise17.py

# Leitura das notas de prova
P1 = float(input("Digite a nota da prova 1: "))
P2 = float(input("Digite a nota da prova 2: "))
P3 = float(input("Digite a nota da prova 3: "))
P4 = float(input("Digite a nota da prova 4: "))

# Leitura das notas de trabalho
T1 = float(input("Digite a nota do trabalho 1: "))
T2 = float(input("Digite a nota do trabalho 2: "))
T3 = float(input("Digite a nota do trabalho 3: "))
T4 = float(input("Digite a nota do trabalho 4: "))

# Cálculo das médias
MP = (P1 + P2 + P3 + P4) / 4
MT = (T1 + T2 + T3 + T4) / 4
MF = 0.8 * MP + 0.2 * MT

# Verificação da aprovação
if MF >= 6:
    print("Aprovado")
else:
    print("Não aprovado")
