import os 

os.system("cls")


produto = input("Digite a descrição do produto = ").strip()

quantidade_adquirida = int(input("Digite a quantidade adquirida = "))

preço_unitário = float(input("Digite o preço unitário = "))

total_á_pagar = quantidade_adquirida * preço_unitário

if quantidade_adquirida <= 5:
    
    desconto_total_pagar = total_á_pagar - (total_á_pagar * 0.02)
    
    print(f"O valor total á pagar é = {desconto_total_pagar}")
    
if quantidade_adquirida > 5 and quantidade_adquirida <= 10:
    
    desconto_total_pagar = total_á_pagar - (total_á_pagar * 0.03)
    
    print(f"O valor total á pagar é de = {desconto_total_pagar}")
    
if quantidade_adquirida > 10:
    
    desconto_total_pagar = total_á_pagar - (total_á_pagar * 0.05 )
    
    print(f"O valor total á pagar é = {desconto_total_pagar}")
    