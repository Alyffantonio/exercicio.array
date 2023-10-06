# Exercício 10
# Faça um código para ler um valor N qualquer (que
# será o tamanho dos vetores). Após, ler dois
# vetores A e B (de tamanho N cada um) e depois
# armazenar em um terceiro vetor Soma a soma dos
# elementos do vetor A com os do vetor B
# (respeitando as mesmas posições) e escrever o
# vetor Soma.

num = int(input("Digite um numero:"))
a = [0]*num
b = [0]*num
soma = [0]*num

for x in range(num):
    a[x] = int(input("Digite a quantos de numeros: "))

    b[x] = int(input("Digite um numero: "))

    soma[x] = a[x] + b[x]

print(a)
print(b)
print(soma)