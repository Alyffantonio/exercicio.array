login = [0, 0]
limit_login = 0
senha = [0, 0]
limit_senh = 0

for x in range(2):
    login[x] = input("Digite o nome do usuario: ")
    senha[x] = int(input("Digite uma senha: "))


while limit_login <= 2:
    verif_usu = input("digite o usuario:")
    for y in range(2):

        if login[y] == verif_usu:
            #print("usuario correto!")
            indice_user = y
            limit_login = 3
            break

    else:
        limit_login += 1
        print("usuario incorreto")
while limit_senh <= 2:
    verif_sen = int(input("Digite a senha:"))
    for w in range(2):

        if senha[indice_user] == verif_sen:
            print("usuario logado!")
            limit_senh = 3
            break
    else:
        print("senha incorreta")
        limit_senh += 1