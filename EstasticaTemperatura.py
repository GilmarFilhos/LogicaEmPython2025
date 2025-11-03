
temperaturas = []
for i in range(7):
    temp = float(input(f"Digite a temperatura do dia {i+1}: "))
    temperaturas.append(temp)

media = sum(temperaturas) / len(temperaturas)

# Encontra a maior e menor temperatura
maior = max(temperaturas)
menor = min(temperaturas)

dias_acima_media = sum(1 for t in temperaturas if t > media)


print("\n=== Estatísticas da Semana ===")
print(f"Temperaturas registradas: {temperaturas}")
print(f"Temperatura média: {media:.2f}")
print(f"Maior temperatura: {maior}")
print(f"Menor temperatura: {menor}")
print(f"Dias acima da média: {dias_acima_media}")
