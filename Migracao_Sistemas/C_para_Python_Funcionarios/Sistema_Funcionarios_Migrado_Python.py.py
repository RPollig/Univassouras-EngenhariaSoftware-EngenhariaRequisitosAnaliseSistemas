MAX = 100  # Define o limite máximo de funcionários que podem ser cadastrados.
funcionarios = []  # Cria uma lista vazia para guardar os funcionários cadastrados.


def adicionar_funcionario():  # Cria a função responsável por cadastrar um funcionário.
    if len(funcionarios) >= MAX:  # Verifica se a lista já chegou ao limite máximo.
        print("Limite atingido!")  # Mostra uma mensagem caso não seja possível cadastrar mais funcionários.
        return  # Encerra a função sem continuar o cadastro.

    nome = input("Nome: ")  # Pede o nome do funcionário e guarda na variável nome.
    cargo = input("Cargo: ")  # Pede o cargo do funcionário e guarda na variável cargo.

    try:  # Inicia uma tentativa para evitar erro caso o salário seja digitado errado.
        salario = float(input("Salário: "))  # Pede o salário e converte o valor para número decimal.
    except ValueError:  # Executa este bloco se o usuário digitar algo que não seja número.
        print("Salário inválido. Cadastro cancelado.")  # Mostra uma mensagem informando o erro.
        return  # Encerra a função sem salvar o funcionário.

    funcionario = {"nome": nome, "cargo": cargo, "salario": salario}  # Cria um dicionário com os dados do funcionário.
    funcionarios.append(funcionario)  # Adiciona o funcionário na lista de funcionários.
    print("Funcionário cadastrado!")  # Mostra mensagem de confirmação do cadastro.


def listar_funcionarios():  # Cria a função responsável por listar todos os funcionários.
    if len(funcionarios) == 0:  # Verifica se ainda não existe funcionário cadastrado.
        print("Nenhum funcionário cadastrado.")  # Mostra mensagem informando que a lista está vazia.
        return  # Encerra a função.

    print("\nLista de funcionários:")  # Mostra o título da listagem.
    for indice, funcionario in enumerate(funcionarios, start=1):  # Percorre a lista mostrando posição e dados de cada funcionário.
        print(f"{indice}) {funcionario['nome']} - {funcionario['cargo']} - R$ {funcionario['salario']:.2f}")  # Imprime os dados formatados.


def buscar_funcionario():  # Cria a função responsável por buscar funcionário pelo nome.
    nome_busca = input("Nome do funcionário: ")  # Pede o nome que será pesquisado.

    for funcionario in funcionarios:  # Percorre cada funcionário cadastrado na lista.
        if funcionario["nome"] == nome_busca:  # Compara o nome cadastrado com o nome pesquisado.
            print(f"Cargo: {funcionario['cargo']} | Salário: R$ {funcionario['salario']:.2f}")  # Mostra os dados se encontrar.
            return  # Encerra a função depois de encontrar o funcionário.

    print("Funcionário não encontrado.")  # Mostra mensagem caso nenhum funcionário seja encontrado.


def main():  # Cria a função principal do programa.
    opcao = -1  # Cria a variável opção com valor inicial diferente de zero.

    while opcao != 0:  # Mantém o menu rodando enquanto o usuário não escolher sair.
        print("\n=== SISTEMA DE FUNCIONÁRIOS ===")  # Mostra o título do sistema.
        print("1 - Adicionar funcionário")  # Mostra a opção de cadastro.
        print("2 - Listar funcionários")  # Mostra a opção de listagem.
        print("3 - Buscar funcionário")  # Mostra a opção de busca.
        print("0 - Sair")  # Mostra a opção para encerrar o programa.

        try:  # Tenta ler a opção escolhida como número inteiro.
            opcao = int(input("Escolha uma opção: "))  # Recebe a opção digitada pelo usuário.
        except ValueError:  # Executa este bloco se o usuário não digitar número.
            print("Opção inválida!")  # Mostra mensagem de erro.
            continue  # Volta para o começo do laço.

        if opcao == 1:  # Verifica se o usuário escolheu adicionar funcionário.
            adicionar_funcionario()  # Chama a função de cadastro.
        elif opcao == 2:  # Verifica se o usuário escolheu listar funcionários.
            listar_funcionarios()  # Chama a função de listagem.
        elif opcao == 3:  # Verifica se o usuário escolheu buscar funcionário.
            buscar_funcionario()  # Chama a função de busca.
        elif opcao == 0:  # Verifica se o usuário escolheu sair.
            print("Encerrando...")  # Mostra mensagem de encerramento.
        else:  # Executa caso a opção não esteja no menu.
            print("Opção inválida!")  # Mostra mensagem de opção inválida.


if __name__ == "__main__":  # Verifica se o arquivo está sendo executado diretamente.
    main()  # Chama a função principal para iniciar o programa.
