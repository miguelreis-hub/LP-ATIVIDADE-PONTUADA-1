import os 

os.system("cls")

nota_1 = float(input("Digite sua primeira nota = "))

nota_2 = float(input("Digite sua segunda nota = "))

media = (nota_1 + nota_2) / 2

if media >= 6:
    
    print("PARABENS, Aprovado")
    
if media == 4:
    
    print("Recuperação")
    
if media < 4:
    
    print("Reprovado")
    