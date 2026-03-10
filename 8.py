import os 

os.system("cls")

cor = input("Digite a cor do cd = ").strip()

match cor:
    
    case "verde":
        
        print("O valor da cor verde = 10,00R$")
        
    case "azul":
        
        print("O valor da cor azul = 20,00R$")
        
    case "amarelo":
        
        print("O valor da cor amarela = 30,00R$")
        
    case "vermelho":
        
        print("A valor da cor vermelha  = 40,00R$")
    case _:
        
        print("Dado invalido")