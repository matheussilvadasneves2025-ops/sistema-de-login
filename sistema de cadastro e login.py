

n_e = ""
n_s = ""
n_c = ""

def fazer_login():

    print("Bem vindo ao Jornal estudantil, faça login para continuar!")
    usuario = input("Nome de usuario ou E-mail: ")
    
    Senha = input('Senha: ')
    print()
    print()
    if Senha.strip() == "":
         print("Preencha o campo obrigatorio!")
         return False
    elif usuario.strip() == "" :
        print("Preencha o campo obrigatorio!")
        return False
    elif (usuario == n_c or usuario == n_e) and Senha == n_s:
        print("Login realizado com sucesso!")
        return True
    else:
        print("E-mail ou senha incorretos, tente novamente!")
        return False
    print()
    
def fazer_cadastro():
    global n_c, n_e, n_s
    while True:
        Cadastrar = input("Não tem uma conta? faça login gratuitamente! (Digite 'sim' para se cadastrar e 'não' caso só tenha errado o login): ").strip().lower()

        if Cadastrar == "sim":
            print("Vamos criar uma conta!")
            n_c = input("Digite um nome de usuario: ").strip()
            while True:
                n_e = input("Digite um e-mail: ").strip()
                if "@" in n_e:
                    break
                print("E-mail inválido! Tente novamente!")
            n_s = input("Digite uma senha: ").strip()
            print()
            print("Cadastro realizado com sucesso! Tente fazer login com suas credenciais.")
            return
        elif Cadastrar == "não":
            print("Tente fazer login novamente!")
            return
        else:
            print("Valor invalido! Tente novamente!")

while True:
    if fazer_login():
        print("Bem vindo(a) {}, aproveite o conteúdo do jornal estudantil!".format(n_c))
        break
    else:
        fazer_cadastro()

    