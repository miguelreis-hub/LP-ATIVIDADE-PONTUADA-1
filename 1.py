import os 

os.system("cls")

letra__a = int(input("Digite o valor de A ="))

letra_b = int(input("Digite o valor de b = "))

letra_c = int(input("Digite o valor de C = "))

soma_a_e_b = letra__a + letra_b


if soma_a_e_b < letra_c:
    
    print(f"A soma de A + B = {soma_a_e_b} é menor que C = {letra_c}")
    
else:
    
    print(f"A soma de A + B = {soma_a_e_b} é maior que C = {letra_c} ")
    
    
    