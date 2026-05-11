opcoes = ["Opção 1", "Opção 2", "Opção 3"]  # Cria uma lista com as opções disponíveis para votação.
votos = [0, 0, 0]  # Cria uma lista para contar os votos de cada opção.
votacao_ativa = True  # Cria uma variável booleana para controlar se a votação continua ativa.

print("=== SISTEMA DE VOTAÇÃO ===")  # Mostra o título do sistema.
print("As opções são:")  # Mostra uma frase antes de listar as opções.

for i, opcao in enumerate(opcoes, start=1):  # Percorre as opções mostrando o número de cada uma.
    print(f"{i} - {opcao}")  # Mostra a opção com sua numeração.

while votacao_ativa:  # Mantém a votação ativa enquanto a variável for verdadeira.
    try:  # Tenta ler a escolha do usuário como número inteiro.
        escolha = int(input(f"\nEscolha uma opção (1-{len(opcoes)}) ou 0 para encerrar: "))  # Recebe o voto ou o comando de encerrar.
    except ValueError:  # Executa se o usuário digitar algo que não seja número.
        print("Entrada inválida. Digite apenas números.")  # Mostra mensagem de erro.
        continue  # Volta para o início do laço.

    if escolha == 0:  # Verifica se o usuário escolheu encerrar a votação.
        votacao_ativa = False  # Altera a variável para finalizar o laço.
    elif 1 <= escolha <= len(opcoes):  # Verifica se a escolha está dentro das opções válidas.
        votos[escolha - 1] += 1  # Soma um voto na opção escolhida.
        print(f"Você votou na {opcoes[escolha - 1]}")  # Mostra em qual opção o usuário votou.
    else:  # Executa quando o número está fora das opções disponíveis.
        print("Opção inválida. Tente novamente.")  # Mostra mensagem de opção inválida.

print("\n=== RESULTADOS FINAIS ===")  # Mostra o título dos resultados.

for i in range(len(opcoes)):  # Percorre todas as opções para mostrar seus votos.
    print(f"{opcoes[i]}: {votos[i]} voto(s)")  # Mostra a quantidade final de votos de cada opção.
