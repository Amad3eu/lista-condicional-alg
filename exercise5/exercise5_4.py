numbers = [int(input(f"Digite o número {i+1}: ")) for i in range(4)]
print("Números divisíveis por 2 e 3: ", [num for num in numbers if num % 2 == 0 and num % 3 == 0])
