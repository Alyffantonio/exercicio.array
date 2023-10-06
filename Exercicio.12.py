# Exercício 12
# Escreva um algoritmo que solicite ao
# usuário a entrada de 5 nomes, e que exiba
# a lista desses nomes na tela.
# Após exibir essa lista, o programa deve
# mostrar também os nomes na ordem
# inversa em que o usuário os digitou, um
# por linha.

a = [0]*4

for x in range(4):
    a[x] = (input(f"Digite o {x+1}º nome: "))
for y in range(4):
    print(a[y])

print("Ordem inversa")
for z in range(3, -1, -1):
    print(a[z])
