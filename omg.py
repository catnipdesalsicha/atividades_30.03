print("-----WELCOME------")
salario = float(input("Digite seu salário: "))

num01= salario * 1.40
num02= salario * 1.50
num03= salario * 1.60

if salario >= 500 and salario <= 1500:
    print("O novo salário é: ", num01)
elif salario >= 1501 and salario <= 2500:
    print("O novo salário é: ", num02)
elif salario >= 2501 and salario <= 3000:
    print("O novo salário é: ", num03)
else:
    print("Salário não se encaixa!!")
