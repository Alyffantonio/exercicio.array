# Exercício 13
# Faça um algoritmo que leia 30 valores do
# tipo inteiro e armazene-os em um vetor.
# A seguir, o algoritmo deverá informar
# (1) todos os números pares que existem no
# vetor;
# (2) o menor e o maior valor existente no
# vetor;
# (3) quantos dos valores do vetor são
# maiores que a média desses valores:

num = [0]*30
num_pares = 0
soma = 0

for x in range(30):
    num[x] = int(input(f"Digite o {x+1}º numero:"))

maior = num[0]
menor = num[0]

for y in range(30):
    if num[y] % 2 == 0:
        num_pares += 1

    soma += num[y]

    if num[y] > maior:
        maior = num[y]
    if num[y] < menor:
        menor = num[y]

media = soma / 30
quant_media = 0

pares = [0] * num_pares
for z in range(30):
    indic_pares = 0
    if num[z] % 2 == 0:
        pares[indic_pares] = num[z]
        indic_pares += 1
    if num[z] > media:
        quant_media += 1

print(f'Os números pares são: {pares}')
print(f'O maior valor é {maior} e o menor é {menor}')
print(f'A quantidade de números acima da média é {quant_media}')