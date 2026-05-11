NUM_ALUNOS = 5  # Define a quantidade fixa de alunos, igual ao programa original em COBOL.
nomes_alunos = []  # Cria uma lista vazia para guardar os nomes dos alunos.
notas_alunos = []  # Cria uma lista vazia para guardar as notas dos alunos.
total_notas = 0  # Cria a variável que vai acumular a soma das notas.

print("=== SISTEMA DE CADASTRO DE ALUNOS ===")  # Mostra o título inicial do sistema.

for i in range(1, NUM_ALUNOS + 1):  # Repete o cadastro do aluno 1 até o aluno 5.
    nome = input(f"Digite o nome do aluno {i}: ")  # Pede o nome do aluno atual.
    nomes_alunos.append(nome)  # Guarda o nome digitado na lista de nomes.

    try:  # Inicia uma tentativa para ler a nota como número.
        nota = float(input(f"Digite a nota de {nome}: "))  # Pede a nota e converte para número decimal.
    except ValueError:  # Executa este bloco se a nota for digitada de forma inválida.
        print("Nota inválida. Será considerada nota 0.")  # Mostra aviso para o usuário.
        nota = 0  # Define a nota como zero para o programa continuar.

    notas_alunos.append(nota)  # Guarda a nota na lista de notas.
    total_notas += nota  # Soma a nota digitada ao total de notas.

media_alunos = total_notas / NUM_ALUNOS  # Calcula a média da turma dividindo total de notas pela quantidade de alunos.

print("=== LISTA DE ALUNOS ===")  # Mostra o título da listagem final.

for i in range(NUM_ALUNOS):  # Percorre as posições das listas de alunos e notas.
    print(f"{nomes_alunos[i]} | Nota: {notas_alunos[i]:.2f}")  # Mostra o nome e a nota de cada aluno.

print(f"Média da turma: {media_alunos:.2f}")  # Mostra a média final da turma formatada com duas casas decimais.
