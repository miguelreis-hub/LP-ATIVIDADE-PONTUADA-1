import os 

os.system("cls")

fruteira = input("Digita a fruta em que voçe quer comprar = ").strip().lower()

quantidade_kg = int(input("Digite a quantidade de kilos = "))

if fruteira == "morango":
    
    if quantidade_kg <= 5:
        
        valor_total_compra = quantidade_kg * 2.50
        
        print(f"O Valor total há pagar é = {valor_total_compra:.2f}R$")
        
    if quantidade_kg > 5:
        
        valor_total_compra = quantidade_kg * 2.20
        
        if quantidade_kg > 10 or valor_total_compra > 15:
            
            valor_total_compra_com_desconto = valor_total_compra - (valor_total_compra * 0.1)
            print(f"O valor total há pagar é = {valor_total_compra_com_desconto:.2f}R$")
            
        else:
            
          print(f"O valor total á pagar é = {valor_total_compra:.2f}R$")

if fruteira == "maca":
    
    if quantidade_kg <= 5:
        
        valor_total_compra = quantidade_kg * 1.80
        
        print(f"O Valor total há pagar é = {valor_total_compra:.2f}R$")
        
    if quantidade_kg > 5:
        
        valor_total_compra = quantidade_kg * 1.50
        
        if quantidade_kg > 10 or valor_total_compra > 15:
            
            valor_total_compra_com_desconto = valor_total_compra - (valor_total_compra * 0.1)
            print(f"O valor total há pagar é = {valor_total_compra_com_desconto:.2f}R$")
            
        else:
            
          print(f"O valor total á pagar é = {valor_total_compra:.2f}R$")
    
    
    
    