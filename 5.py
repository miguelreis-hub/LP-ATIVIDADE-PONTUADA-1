import os 

os.system("cls")

letra_A = int(input("Digite o valor da letra A = "))

letra_B = int(input("Digite o valor de B ="))

operacao = input("Digite a operação desejada = (+,-,* ou /) = ").strip()

match operacao:
    
    case "+":
        soma = letra_A + letra_B
        print(f"A soma de A + B = {soma}")
        
    case "-":
        
        subtração = letra_A - letra_B
        print(f"A subtração de A - B = {subtração}")
        
    case "*":
        multiplicacao = letra_A * letra_B
        print(f"A multiplicação de A * B = {multiplicacao}")
        
    case "/":
        
        divisao = letra_A / letra_B
        print(f"A divisão de A / B = {divisao}")
    case _:
        
        print("DADO INCORRETO")