import os
import json as js
import time 

def limpar():
    return os.system("cls" if os.name == "nt" else "clear")


def cadastrar(produtos):
    while True:
        try:
            print("=== Sistema de Cadastro de Produtos ===\n")
            nome = input("Informe o nome do produto: ")
            nome = nome.capitalize()
            preco = float(input("Informe o preço do produto: "))
            quantidade = int(input("Informe a quantidade em estoque: "))
        except ValueError:
            limpar()
            print("Erro!, Valor Digitado Invalido. Tente novamente. \n")
        else:
            produtos["Nome"].append(nome)
            produtos["Preco"].append(preco)
            produtos["Quantidade"].append(quantidade)
            break
    return produtos


def listar(produtos):
    col_width = max(len(prod) for prod in produtos["Nome"]) + 2
    col2_width = max(len(str(prod)) for prod in produtos["Preco"]) + 2
    col3_width = max(len(str(prod)) for prod in produtos["Quantidade"]) + 7
    print(f'+{"-" * col_width}+{"-" * col2_width}----+{"-" * col3_width}---+')
    print(f'| {"Nome".ljust(col_width)} | {'Preço'.ljust(col2_width)} | {'Quantidade'.ljust(col3_width)} |')
    print(f'+{"-" * col_width}+{"-" * col2_width}----+{"-" * col3_width}---+')

    for i in range(len(produtos["Nome"])):
        print(f'| {produtos["Nome"][i].ljust(col_width)} | {str(produtos["Preco"][i]).ljust(col2_width)} | {str(produtos["Quantidade"][i]).ljust(col3_width)} |')
        print(f'+{"-" * col_width}+{"-" * col2_width}----+{"-" * col3_width}---+')


def buscar(produtos):
    while True:
        nome = input("Qual nome do produto que você deseja achar?: ")
        nome = nome.capitalize()
        try:
            limpar()
            print(f"""Produto: {produtos['Nome'][produtos["Nome"].index(nome)]}
Preço: {produtos['Preco'][produtos["Nome"].index(nome)]}
Quantidade: {produtos['Quantidade'][produtos["Nome"].index(nome)]}
            """)
            break
        except ValueError:
            limpar()
            print("Erro!, Nome não encontado, verificar o Nome do produto. \n")


def atualizar(produtos):
    while True:
        try:
            antigo = input("Qual o nome do produto que voce deseja substituir: ")
            antigo = antigo.lower()
            antigo = antigo.capitalize()
            produtos["Nome"].index(antigo)
            limpar()
            print(
                "== Caso não queira mudar todos apenas aperte Enter no que não quiser mudar"
            )
            nome = input("Informe o novo nome do produto: ")
            nome = nome.capitalize()
            preco = input("Informe o novo preço do produto: ")
            quantidade = input("Informe a nova quantidade em estoque: ")

            if nome:
                produtos["Nome"][produtos["Nome"].index(antigo)] = nome
            if preco:
                produtos["Preco"][produtos["Nome"].index(antigo)] = float(preco)
            if quantidade:
                produtos["Quantidade"][produtos["Nome"].index(antigo)] = int(quantidade)
            break
        except ValueError:
            limpar()
            print(
                "Erro!, Verifique o nome do produto antigo, nome novo, preco novo ou nova quantidade: \n"
            )
def excluir(produtos):
        while True:
            nome = input("Qual nome do produto que você deseja excluir?: ")
            nome = nome.capitalize()
            indice = produtos["Nome"].index(nome)
            try:
                limpar()
                produtos["Nome"].remove(produtos['Nome'][indice])
                produtos["Preco"].remove(produtos['Preco'][indice])
                produtos["Quantidade"].remove(produtos['Quantidade'][indice])
                print("Produto Excluido com sucesso:")
                print("Aperte Enter para sair")
                input()
                break
            except ValueError:
                limpar()
                print("Erro!, Nome não encontado, verificar o Nome do produto. \n")


if __name__ == "__main__":
    try:
        with open('produtos,json','r') as arquivo:
            produtos = js.load(arquivo)
    except FileNotFoundError:
        print("Arquivo não encontrado. Criando um novo dicionário.\nDigite qualquer tecla para prosseguir")
        produtos = {"Nome": [], "Preco": [], "Quantidade": []}
        input()
        limpar()
    while True:
        try:
            limpar()
            option = int(
                input(
                    "=== Sistema de Gerenciamento de Produtos ===\n1. Cadastrar produto\n2. Listar produtos\n3. Buscar produto\n4. Atualizar estoque\n5. Excluir produto\n6. Sair\nEscolha uma opção: "
                )
            )

            if option == 1:
                limpar()
                cadastrar(produtos)
                limpar()
                print("Produto Cadastrado com sucesso")
                time.sleep(2)
                limpar()
            elif option == 2:
                limpar()
                listar(produtos)
                input("Para continuar aperte qualquer tecla: ")
                limpar()
                continue
            elif option == 3:
                limpar()
                buscar(produtos)
                input("Para continuar aperte qualquer tecla: ")
                limpar()
            elif option == 4:
                limpar()
                atualizar(produtos)
                limpar()
                print("Produto Atualizado com sucesso")
                time.sleep(2)
            elif option == 5:
                limpar()
                excluir(produtos)
            elif option == 6:
                limpar()
                with open('produtos,json','w') as arquivo:
                    js.dump(produtos, arquivo, indent=4)
                print("Dados foram Salvos com Sucesso")
                print("Saindo em...")
                for i in range(3,0,-1):
                    time.sleep(1)
                    print(i) 
                limpar()
                print("Obrigado, Até mais.")
                break
            else:
                limpar()
                print("Valor invalido. Por favor tente novamente \n")
        except ValueError:
            limpar()
            print("Erro!, valor não relacionado\n")
    
