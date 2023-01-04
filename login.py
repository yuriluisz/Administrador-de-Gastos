
import getpass
import os
import subprocess

if os.name == "nt":
    clear = "cls"
else:
    clear = "clear"

logued = 'no'

def PaginaPrincipal():
    print("Bem vindo a pagina principal!")

def login():

    ReadLogin = open("login.txt", "r")
    Leitura = ReadLogin.readlines()
    print("Insira seu Login e Senha para logar.")
    Login = input("Login: ")
    Senha = input("Senha: ")

    if Login and Senha in Leitura:
        print("Logado Com sucesso!")
        input("Presione enter para continuar!")
        ReadLogin.close()
        os.system(clear)
        PaginaPrincipal()
    else:
        print("Parece que seu login está incorreto :(")
        input("Pressione Enter para continuar!")
        ReadLogin.close()
        os.system(clear)


def registro():

    AppendLogin = open("login.txt", "a")
    print("Insira seu novo Login e sua nova Senha para continuar!")
    Login = input("Novo Login: ")
    Senha = input("Nova Senha: ")

    AppendLogin.write(Login + "\n")
    AppendLogin.write(Senha + "\n")
    os.system(clear)
    login()


def main():
    while True:
        print("Caso Ja tenha uma conta Escreva Logar!")
        print("Caso NÂO tenha uma conta escreva Registrar\n")

        LorR = input("Escolha: Logar ou Registrar? ")
        LorR.upper

        if LorR == "LOGAR":
            login()
            os.system(clear)
        elif LorR == "REGISTRAR":
            registro()
            os.system(clear)
        else:
            print("Insira uma opção valida!")
            os.system(clear) 

if __name__ == "__main__":
    main()
