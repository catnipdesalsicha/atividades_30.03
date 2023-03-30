print("----------WELCOME--------")

num01 = int(input("Digite minha pomba no seu cu: "))
num02 = int(input("Digite outra pomba no seu cu: "))
num03 = int(input("Digite outra pomba no seu cu: "))

if num01 > num02 and num01 > num03:
    print("O número", num01, "é o maior")
elif num02 > num01 and num02 > num03:
    print("O número", num02, "é o maior")
elif num03> num01 and num03> num02:
    print("O número", num03, "é o maior")
else:
    print("Tem algum número igual!")
