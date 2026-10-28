print("verifique senha e usuario")
usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == "admin" and senha == "1234":
    print("Acesso Permitido! ")
else:
    print("Usuario ou senha incorretos ")

