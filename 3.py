import os 

os.system("cls")

letra_a = int(input("Digite um valor inteiro para A = "))

letra_b = int(input("Digite um valor inteiro para B ="))


if letra_a == letra_b:
    
    valor_a_b = letra_a + letra_b
    
    letra_c = valor_a_b
    
    print(f"O valor de C é = {letra_c}")
    
else:
    valor_a_b = letra_a * letra_b
    
    letra_c = valor_a_b
    
    print(f"O Valor de C é = {letra_c} ")
    
    