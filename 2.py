import os 


os.system("cls")

nome_da_pessoa = input("Digite seu nome = ").strip()

sexo_da_pessoa = input("Digite seu sexo = ").strip()

estado_civil_da_pessoa = input("Digite o seu estado civil = ").strip()


if sexo_da_pessoa == "F" and estado_civil_da_pessoa == "CASADA":
    
    tempo_de_casada = int(input("Digite o seu tempo de casada = "))
    
    print(f"Nome = {nome_da_pessoa}\n sexo = {sexo_da_pessoa} \n estado civil = {estado_civil_da_pessoa}\n tempo de casada = {tempo_de_casada}anos")
    