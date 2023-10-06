# Exercício 11
# Faça um código para ler um vetor de 30
# números. Após isto, ler mais um número
# qualquer, calcular e escrever quantas
# vezes esse número aparece no vetor.



a = [0]*5

for i in range(5):
    a[i] = int(input(f"digite um numero o {i+1}º: "))

quantidade = 0
num_busc = int(input("digite um numero: "))

for x in a:
    if x == num_busc:
        quantidade += 1
print(f"o numero:{num_busc} aparece {quantidade} vezes no vetor.")