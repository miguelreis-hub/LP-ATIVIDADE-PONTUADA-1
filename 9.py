import os 

os.system("cls")

renda_mensal = float(input("Digite sua renda mensal = "))

valor_total_emprestimo = float(input("Digite o valor total do emprestimo = "))

numero_prestação = float(input("Digite o numero das prestações, que deseja pagar "))


limite_do_emprestimo = renda_mensal * 10

limite_prestação = renda_mensal * 0.30

if (valor_total_emprestimo <= limite_prestação) and (numero_prestação <= limite_prestação):
    print("Empréstimo aprovado!")
else:
    print("Empréstimo negado!")
