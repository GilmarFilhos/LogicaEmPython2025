
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

while b != 0:
    resto = a % b
    a = b
    b = resto

# Saída
print(f"MDC = {a}")
