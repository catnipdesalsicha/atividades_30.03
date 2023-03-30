print("------UTLTIMA ATIVIDADE--------")

idade= int(input("Digite sua idade para descobrir sua modalidade: "))

if idade== 5 and idade<=10:
    print("Sua categoria é Infantil!")
elif idade>= 11 and idade<=17:
    print("Sua categoria é juvenil!")
elif idade>=18 and idade<=31:
    print("Sua categoria é Adulto!")
elif idade>=33:
    print("Sua categoria é Master!")
else:
    print("Você é muito novo pra competir")
