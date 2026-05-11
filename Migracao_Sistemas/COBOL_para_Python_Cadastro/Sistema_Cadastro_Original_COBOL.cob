       IDENTIFICATION DIVISION.
* Parte responsável pela identificação do programa.
* Em Python seria parecido com o nome do arquivo ou início do sistema.

       PROGRAM-ID. SISTEMA-ALUNOS.
* Nome do programa COBOL.
* Em Python seria parecido com criar um arquivo chamado sistema_alunos.py

       ENVIRONMENT DIVISION.
* Área relacionada ao ambiente do sistema.
* Em programas simples normalmente quase não é utilizada.

       DATA DIVISION.
* Parte onde ficam as variáveis do sistema.
* Em Python seria parecido com a área onde criamos variáveis.

       WORKING-STORAGE SECTION.
* Área de memória usada para armazenar dados durante execução.
* Em Python as variáveis normalmente já ficam disponíveis automaticamente.

       77 NUM-ALUNOS      PIC 9 VALUE 5.
* Variável inteira com valor inicial 5.
* PIC 9 representa número inteiro.
* Em Python seria parecido com:
* num_alunos = 5

       77 I               PIC 9 VALUE 1.
* Variável de controle do laço de repetição.
* Em Python seria parecido com:
* i = 1

       01 NOME-ALUNO-TEXT.
* Estrutura principal para armazenar nomes.

          05 NOME-ALUNO    OCCURS 5 TIMES PIC X(20).
* Vetor/lista contendo 5 nomes de alunos.
* PIC X(20) significa texto com até 20 caracteres.
* Em Python seria parecido com:
* nomes = []

       01 NOTAS-ALUNO       OCCURS 5 TIMES PIC 99V99.
* Vetor/lista para armazenar notas.
* PIC 99V99 representa número decimal.
* Em Python seria parecido com:
* notas = []

       77 TOTAL-NOTAS      PIC 99V99 VALUE 0.
* Variável que acumula soma das notas.
* Em Python seria:
* total_notas = 0

       77 MEDIA-ALUNOS     PIC 99V99 VALUE 0.
* Variável que guarda média final da turma.
* Em Python seria:
* media_alunos = 0

       PROCEDURE DIVISION.
* Parte principal da lógica do sistema.
* Em Python seria parecido com as funções e execução principal.

       MAIN-PARAGRAPH.
* Início principal do programa.

           DISPLAY "=== SISTEMA DE CADASTRO DE ALUNOS ===".
* Exibe mensagem na tela.
* Em Python seria:
* print("=== SISTEMA DE CADASTRO DE ALUNOS ===")

           PERFORM VARYING I FROM 1 BY 1 UNTIL I > NUM-ALUNOS
* Estrutura de repetição.
* Em Python seria parecido com:
* for i in range(num_alunos):

               DISPLAY "Digite o nome do aluno " I ": "
* Solicita nome do aluno.

               ACCEPT NOME-ALUNO(I)
* Recebe nome digitado pelo usuário.
* Em Python seria:
* nome = input()

               DISPLAY "Digite a nota de " NOME-ALUNO(I) ": "
* Solicita nota do aluno.

               ACCEPT NOTAS-ALUNO(I)
* Recebe nota digitada.
* Em Python seria:
* nota = float(input())

               ADD NOTAS-ALUNO(I) TO TOTAL-NOTAS
* Soma nota ao total acumulado.
* Em Python seria:
* total_notas += nota

           END-PERFORM
* Final da repetição.

           PERFORM CALCULA-MEDIA
* Chama rotina responsável pelo cálculo da média.
* Em Python seria parecido com:
* calcular_media()

           DISPLAY "=== LISTA DE ALUNOS ==="
* Exibe título da listagem.

           PERFORM VARYING I FROM 1 BY 1 UNTIL I > NUM-ALUNOS
* Novo laço para exibir alunos cadastrados.

               DISPLAY NOME-ALUNO(I) " | Nota: " NOTAS-ALUNO(I)
* Exibe nome e nota do aluno.
* Em Python seria parecido com:
* print(f"{nome} | Nota: {nota}")

           END-PERFORM
* Final do laço.

           DISPLAY "Média da turma: " MEDIA-ALUNOS
* Exibe média final da turma.
* Em Python seria:
* print(media_alunos)

           STOP RUN.
* Finaliza o programa.
* Em Python o programa termina automaticamente ao final da execução.

       CALCULA-MEDIA.
* Rotina responsável por calcular média da turma.

           DIVIDE TOTAL-NOTAS BY NUM-ALUNOS GIVING MEDIA-ALUNOS.
* Divide total das notas pela quantidade de alunos.
* Em Python seria:
* media_alunos = total_notas / num_alunos

           EXIT.
* Finaliza rotina atual.