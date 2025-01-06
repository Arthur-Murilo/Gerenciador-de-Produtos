import os


def limpar():
    return os.system("cls" if os.name == "nt" else "clear")


def cadastrar(produtos):
    while True:
        try:
            print("=== Sistema de Cadastro de Produtos ===\n")
            nome = input("Informe o nome do produto: ")
            nome = nome.lower()
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
    print("""+------------+-------+------------+
| Nome       | Preço | Quantidade |
+------------+-------+------------+""")

    for i in range(len(produtos["Nome"])):
        print(
            f'| {produtos["Nome"][i]:<10} | {produtos["Preco"][i]:<5.2f} | {"":<4} {produtos["Quantidade"][i]:<5} |'
        )
    print("+------------+-------+------------+")


def buscar(produtos):
    while True:
        nome = input("Qual nome do produto que você deseja achar?: ")
        nome = nome.lower()
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
            nome = nome.lower()
            nome = nome.capitalize()
            preco = input("Informe o novo preço do produto: ")
            quantidade = input("Informe a nova quantidade em estoque: ")

            if nome == "":
                if preco == "":
                    produtos["Quantidade"][produtos["Nome"].index(antigo)] = int(
                        quantidade
                    )
                    break
                elif quantidade == "":
                    produtos["Preco"][produtos["Nome"].index(antigo)] = float(preco)
                    break
                elif preco == "" and quantidade == "":
                    break
                else:
                    produtos["Preco"][produtos["Nome"].index(antigo)] = float(preco)
                    produtos["Quantidade"][produtos["Nome"].index(antigo)] = int(
                        quantidade
                    )
                    break
            elif preco == "":
                if quantidade == "":
                    produtos["Nome"][produtos["Nome"].index(antigo)] = nome
                    break
                elif nome == "":
                    produtos["Quantidade"][produtos["Nome"].index(antigo)] = int(
                        quantidade
                    )
                    break
                elif quantidade == "" and nome == "":
                    break
                else:
                    produtos["Quantidade"][produtos["Nome"].index(antigo)] = int(
                        quantidade
                    )
                    produtos["Nome"][produtos["Nome"].index(antigo)] = nome
                    break
            elif quantidade == "":
                if preco == "":
                    produtos["Nome"][produtos["Nome"].index(antigo)] = nome
                    break
                elif nome == "":
                    produtos["Preco"][produtos["Nome"].index(antigo)] = float(preco)
                elif preco == "" and nome == "":
                    break
                else:
                    produtos["Preco"][produtos["Nome"].index(antigo)] = float(preco)
                    produtos["Nome"][produtos["Nome"].index(antigo)] = nome
                    break
            else:
                produtos["Preco"][produtos["Nome"].index(antigo)] = float(preco)
                produtos["Quantidade"][produtos["Nome"].index(antigo)] = int(quantidade)
                produtos["Nome"][produtos["Nome"].index(antigo)] = nome
                break
        except ValueError:
            limpar()
            print(
                "Erro!, Verifique o nome do produto antigo, nome novo, preco novo ou nova quantidade: \n"
            )


if __name__ == "__main__":
    produtos = {"Nome": [], "Preco": [], "Quantidade": []}
    while True:
        try:
            option = int(
                input(
                    "=== Sistema de Gerenciamento de Produtos ===\n1. Cadastrar produto\n2. Listar produtos\n3. Buscar produto\n4. Atualizar estoque\n5. Sair\nEscolha uma opção: "
                )
            )

            if option == 1:
                limpar()
                cadastrar(produtos)
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
            elif option == 5:
                limpar()
                print("Obrigado, Até mais.")
                break
            else:
                limpar()
                print("Valor invalido. Por favor tente novamente \n")
        except ValueError:
            limpar()
            print("Erro!, valor não relacionado\n")
