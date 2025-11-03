valor = float(input("Digite o valor da compra: "))

desconto = 0.10 if valor >= 500 else 0.05 if valor >= 300 else 0

valor_final = valor * (1 - desconto)

print(f"Valor com desconto: {valor_final:.2f}")
