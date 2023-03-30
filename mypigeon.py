print("------------WELCOME--------------")
salario = float(input("Digite seu salário: "))

if salario <= 300:
    print("Seu salário ficou : ", salario * 1.35)
    print("35%")
else:
    print("Seu salário ficou: ", salario * 1.15)
    print("15%")
