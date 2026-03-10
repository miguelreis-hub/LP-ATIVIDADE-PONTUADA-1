import os 

os.system("cls")

quantidade_de_litros = int(input("Digite a quantidade de litros = "))

tipo_combustivel = input("Digite o tipo do combustivel = ").strip()

if tipo_combustivel == "alcool":
    
    if quantidade_de_litros <= 25:
        
        valor_total_pagar = quantidade_de_litros * 3.79
        valor_total_pagar_desconto = valor_total_pagar - (valor_total_pagar * 0.02)
        
        print(f"O valor total á pagar é = {valor_total_pagar_desconto:.2f}R$")
    
    if quantidade_de_litros > 25:
        
          valor_total_pagar = quantidade_de_litros * 3.79
          valor_total_pagar_desconto = valor_total_pagar - (valor_total_pagar * 0.04)
          
          print(f"O valor total á pagar é = {valor_total_pagar_desconto:.2f}R$")

if tipo_combustivel == "gasolina":
    
     if quantidade_de_litros <= 25:
        
        valor_total_pagar = quantidade_de_litros * 6.59
        valor_total_pagar_desconto = valor_total_pagar - (valor_total_pagar * 0.03)
        
        print(f"O valor total á pagar é = {valor_total_pagar_desconto:.2f}R$")
    
     if quantidade_de_litros > 25:
        
          valor_total_pagar = quantidade_de_litros * 6.59
          valor_total_pagar_desconto = valor_total_pagar - (valor_total_pagar * 0.05)
          
          print(f"O valor total á pagar é = {valor_total_pagar_desconto:.2f}R$")
    
    
    
    
    
    
        