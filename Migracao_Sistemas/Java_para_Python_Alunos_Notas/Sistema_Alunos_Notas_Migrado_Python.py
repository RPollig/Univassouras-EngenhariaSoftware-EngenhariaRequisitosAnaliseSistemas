notas = {}  # Cria um dicionário para guardar o nome do aluno e sua nota.
lista_nomes = []  # Cria uma lista para manter a ordem dos nomes cadastrados.


def adicionar_aluno():  # Cria a função responsável por cadastrar aluno.
    nome = input("Nome do aluno: ")  # Pede o nome do aluno.

    try:  # Tenta ler a nota como número decimal.
        nota = float(input("Nota final: "))  # Pede a nota final do aluno.
    except ValueError:  # Executa este bloco se a nota não for numérica.
        print("Nota inválida. Cadastro cancelado.")  # Mostra mensagem de erro.
        return  # Encerra a função sem cadastrar.

    notas[nome] = nota  # Guarda a nota no dicionário usando o nome como chave.
    lista_nomes.append(nome)  # Adiciona o nome na lista de nomes.
    print("Aluno cadastrado com sucesso!")  # Mostra mensagem de confirmação.


def listar_alunos():  # Cria a função responsável por listar os alunos.
    if len(lista_nomes) == 0:  # Verifica se a lista está vazia.
        print("Nenhum aluno cadastrado.")  # Mostra mensagem caso não exista cadastro.
        return  # Encerra a função.

    print("\nLista de alunos:")  # Mostra o título da lista.
    for nome in lista_nomes:  # Percorre todos os nomes cadastrados.
        print(f"- {nome} | Nota: {notas[nome]}")  # Mostra o nome e a nota correspondente.


def buscar_nota():  # Cria a função responsável por buscar a nota de um aluno.
    nome = input("Nome do aluno: ")  # Pede o nome que será pesquisado.

    if nome in notas:  # Verifica se o nome existe no dicionário de notas.
        print(f"Nota de {nome}: {notas[nome]}")  # Mostra a nota encontrada.
    else:  # Executa se o aluno não estiver cadastrado.
        print("Aluno não encontrado.")  # Mostra mensagem de não encontrado.


def main():  # Cria a função principal do programa.
    opcao = -1  # Cria a variável opção com valor inicial diferente de zero.

    while opcao != 0:  # Mantém o menu aberto até o usuário escolher sair.
        print("\n=== SISTEMA DE ALUNOS ===")  # Mostra o título do sistema.
        print("1 - Adicionar aluno")  # Mostra a opção de adicionar aluno.
        print("2 - Listar alunos")  # Mostra a opção de listar alunos.
        print("3 - Buscar nota")  # Mostra a opção de buscar nota.
        print("0 - Sair")  # Mostra a opção de sair.

        try:  # Tenta converter a opção digitada para inteiro.
            opcao = int(input("Opção: "))  # Recebe a opção do usuário.
        except ValueError:  # Executa se o usuário digitar algo inválido.
            print("Opção inválida!")  # Mostra mensagem de erro.
            continue  # Volta para o menu.

        if opcao == 1:  # Verifica se a opção é adicionar aluno.
            adicionar_aluno()  # Chama a função de adicionar aluno.
        elif opcao == 2:  # Verifica se a opção é listar alunos.
            listar_alunos()  # Chama a função de listar alunos.
        elif opcao == 3:  # Verifica se a opção é buscar nota.
            buscar_nota()  # Chama a função de buscar nota.
        elif opcao == 0:  # Verifica se a opção é sair.
            print("Encerrando...")  # Mostra mensagem de encerramento.
        else:  # Executa se a opção não existir.
            print("Opção inválida!")  # Mostra mensagem de erro.


if __name__ == "__main__":  # Verifica se o arquivo está sendo executado diretamente.
    main()  # Inicia o programa chamando a função principal.
