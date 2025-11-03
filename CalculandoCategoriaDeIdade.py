idade = float(input("Digite uma idade: "))

if idade <= 12:
    print("Criança")
elif 12 <= idade <=17:
    print("Adolecente")
elif 18 <= idade <= 59:
    print("adulto")
elif idade >= 60:
    print("idoso")
else:
    print("Algo deu errado")
    
