from colorama import Fore

noticia = [
"Alunos do ensino médio participam de feira de ciências",
"Estudantes do ensino médio organizam campanha de arrecadação de alimentos",
"Alunos do ensi'no médio criam projeto de sustentabilidade para a escola",
"Grêmio estudantil é absolvido após investigação de suposto desvio de verbas",

]

detalhes = [
"Alunos do ensino médio participaram de uma feira de ciências na escola, apresentando projetos inovadores e criativos. Os estudantes mostraram suas habilidades em áreas como biologia, física, química e tecnologia, impressionando os visitantes com suas descobertas e experimentos.",
"Estudantes do ensino médio organizaram uma campanha de arrecadação de alimentos para ajudar famílias carentes da comunidade. A iniciativa contou com a participação ativa dos alunos, que arrecadaram uma quantidade significativa de alimentos não perecíveis e os distribuíram para aqueles que mais precisam.",
"Alunos do ensino médio criaram um projeto de sustentabilidade para a escola, visando reduzir o impacto ambiental e promover práticas mais conscientes. O projeto inclui ações como reciclagem, economia de energia e conscientização sobre o consumo responsável, envolvendo toda a comunidade escolar.",
"O grêmio estudantil foi absolvido após uma investigação de suposto desvio de verbas. As autoridades escolares concluíram que não houve irregularidades e que os recursos foram utilizados de forma adequada para beneficiar a comunidade estudantil. O grêmio continuará suas atividades normalmente, promovendo eventos e iniciativas para os alunos."

]

n_e = ""
n_s = ""
n_c = ""

def fazer_login():

    print(Fore.RESET + "Bem vindo ao Jornal estudantil, faça login para continuar!")
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
        print(Fore.GREEN + "Login realizado com sucesso!")
        return True
    else:
        print(Fore.RED + "E-mail ou senha incorretos, tente novamente!")
        return False
    print()
    
def fazer_cadastro():
    global n_c, n_e, n_s
    while True:
        Cadastrar = input(Fore.RESET + "Não tem uma conta? faça login gratuitamente! (Digite 'sim' para se cadastrar e 'não' caso só tenha errado o login): ").strip().lower()

        if Cadastrar == "sim":
            print("Vamos criar uma conta!")
            n_c = input("Digite um nome de usuario: ").strip()
            while True:
                n_e = input(Fore.RESET + "Digite um e-mail: ").strip()
                if "@" in n_e:
                    break
                print(Fore.RED + "E-mail inválido! Tente novamente!")
            n_s = input(Fore.RESET + "Digite uma senha: ").strip()
            print()
            print(Fore.GREEN + "Cadastro realizado com sucesso! Tente fazer login com suas credenciais.")
            return
        elif Cadastrar == "não":
            print(Fore.RESET + "Tente fazer login novamente!")
            return
        else:
            print("Valor invalido! Tente novamente!")

while True:
    if fazer_login():
        print("Bem vindo(a) {}, aproveite o conteúdo do jornal estudantil!".format(n_c))
        break
    else:
        fazer_cadastro()

def opcao_menu():
    print()
    print(Fore.YELLOW + "Oque deseja fazer agora?")
    print(Fore.RESET + "1 - Ler as noticias")
    print("2 - Escrever uma noticia")
    print("3 - Sair do sistema")
    print()
    opcao = input("Digite o numero da opção desejada: ")

    if opcao == "1":
            print("Aqui estão as noticias mais recentes do jornal estudantil:")
            for i, n in enumerate(noticia):
                print(Fore.CYAN + f"Noticia {i}:" + Fore.RESET + f" {n}")
            print()
            opcao_noticia = input("Digite o numero da noticia que deseja ler ou 'Exit' para voltar ao menu: ")
            if opcao_noticia.isdigit():

                indice = int(opcao_noticia)

                if 0 <= indice < len(noticia):
                    print()
                    print(Fore.CYAN + noticia[indice] + Fore.RESET)
                    print(detalhes[indice])
                else:
                    print("Essa notícia não existe!")
                    
            elif opcao_noticia == "Exit" or opcao_noticia == "exit":
                return
            else:
                print("Opção invalida! Retornando ao menu.")
    elif opcao == "2":
        print("Vamos escrever uma noticia!")
        titulo = input("Digite o titulo da noticia: ")
        conteudo = input("Digite o conteudo da noticia: ")
        noticia.append(titulo)
        print()
        input("Noticia publicada com sucesso! Digite 'Exit' para voltar ao menu: ")
    elif opcao == "3":
        print(Fore.RED + "Você tem certeza que deseja sair? ")
    else:
        print("Opção invalida! Tente novamente!")

while True:
    opcao_menu()
    confirmacao = input(Fore.RED +"deseja sair do sistema? ('Não' resultara em voltar ao menu): ").strip().lower()
    if confirmacao == "sim":
        print()
        print("Obrigado por usar o sistema, até a próxima!")
        break
    elif confirmacao == "não":
        continue
    else:
        print(Fore.YELLOW + "Valor invalido! Continuando no sistema.")
    