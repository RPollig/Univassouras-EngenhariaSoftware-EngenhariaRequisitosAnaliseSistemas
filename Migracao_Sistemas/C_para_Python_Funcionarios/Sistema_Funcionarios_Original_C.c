#include <stdio.h>   // Biblioteca de entrada e saída. Em Python seria parecido com usar print() e input().
#include <string.h>  // Biblioteca para trabalhar com textos. Em Python strings já têm funções próprias.

#define MAX 100      // Define uma constante com limite máximo de funcionários. Em Python seria: MAX = 100

// Cria um tipo de dado chamado Funcionario.
// Em Python, isso poderia ser parecido com um dicionário ou uma classe.
typedef struct {
    char nome[50];      // Texto com até 49 caracteres + finalizador. Em Python seria: nome = ""
    char cargo[30];     // Texto para guardar o cargo. Em Python seria: cargo = ""
    float salario;      // Número decimal. Em Python seria: salario = 0.0
} Funcionario;

// Cria um vetor/lista com espaço para 100 funcionários.
// Em Python seria parecido com: funcionarios = []
Funcionario funcionarios[MAX];

// Controla quantos funcionários já foram cadastrados.
// Em Python seria: total = 0
int total = 0;

// Declaração das funções antes de serem usadas.
// Em Python normalmente não precisa declarar antes, basta definir com def.
void adicionarFuncionario();
void listarFuncionarios();
void buscarFuncionario();

int main() {
    int opcao; // Guarda a opção escolhida pelo usuário. Em Python seria: opcao = 0

    // Estrutura de repetição do menu.
    // Em Python seria parecido com: while opcao != 0:
    do {
        printf("\n=== SISTEMA DE FUNCIONÁRIOS ===\n"); // Mostra título. Em Python: print()
        printf("1 - Adicionar funcionário\n");        // Mostra opção 1.
        printf("2 - Listar funcionários\n");          // Mostra opção 2.
        printf("3 - Buscar funcionário\n");           // Mostra opção 3.
        printf("0 - Sair\n");                         // Mostra opção para sair.
        printf("Escolha uma opção: ");                 // Solicita escolha do usuário.

        // Lê um número inteiro digitado pelo usuário.
        // Em Python seria parecido com: opcao = int(input("Escolha uma opção: "))
        scanf("%d", &opcao);

        // Limpa o buffer do teclado após o scanf.
        // Isso evita problema quando depois usamos fgets para ler texto.
        getchar();

        // Estrutura de decisão baseada na opção escolhida.
        // Em Python seria parecido com if / elif / else.
        switch (opcao) {
            case 1:
                adicionarFuncionario(); // Chama a função de cadastro. Em Python: adicionar_funcionario()
                break;

            case 2:
                listarFuncionarios(); // Chama a função de listagem. Em Python: listar_funcionarios()
                break;

            case 3:
                buscarFuncionario(); // Chama a função de busca. Em Python: buscar_funcionario()
                break;

            case 0:
                printf("Encerrando...\n"); // Mensagem de saída. Em Python: print("Encerrando...")
                break;

            default:
                printf("Opção inválida!\n"); // Caso o usuário digite opção fora do menu.
        }

    } while (opcao != 0); // Repete o menu enquanto a opção for diferente de zero.

    return 0; // Finaliza o programa corretamente. Em Python não precisa usar return no programa principal.
}

// Função responsável por cadastrar um funcionário.
// Em Python seria: def adicionar_funcionario():
void adicionarFuncionario() {

    // Verifica se o limite de funcionários foi atingido.
    // Em Python seria parecido com: if total >= MAX:
    if (total >= MAX) {
        printf("Limite atingido!\n"); // Mostra mensagem se não puder cadastrar mais.
        return; // Sai da função. Em Python também existe return.
    }

    printf("Nome: "); // Solicita o nome do funcionário.

    // Lê uma linha de texto digitada pelo usuário.
    // Em Python seria parecido com: nome = input("Nome: ")
    fgets(funcionarios[total].nome, 50, stdin);

    // Remove o \n que o fgets captura ao apertar Enter.
    // Em Python seria parecido com: nome = nome.strip()
    funcionarios[total].nome[strcspn(funcionarios[total].nome, "\n")] = '\0';

    printf("Cargo: "); // Solicita o cargo do funcionário.

    // Lê o cargo digitado pelo usuário.
    // Em Python seria parecido com: cargo = input("Cargo: ")
    fgets(funcionarios[total].cargo, 30, stdin);

    // Remove a quebra de linha do cargo.
    // Em Python seria parecido com: cargo = cargo.strip()
    funcionarios[total].cargo[strcspn(funcionarios[total].cargo, "\n")] = '\0';

    printf("Salário: "); // Solicita o salário do funcionário.

    // Lê um número decimal.
    // Em Python seria parecido com: salario = float(input("Salário: "))
    scanf("%f", &funcionarios[total].salario);

    // Limpa o buffer após ler o salário.
    getchar();

    // Aumenta o total de funcionários cadastrados.
    // Em Python seria parecido com: total += 1
    total++;

    printf("Funcionário cadastrado!\n"); // Confirma o cadastro.
}

// Função responsável por listar todos os funcionários cadastrados.
// Em Python seria: def listar_funcionarios():
void listarFuncionarios() {

    // Verifica se não existe nenhum funcionário cadastrado.
    // Em Python seria parecido com: if total == 0:
    if (total == 0) {
        printf("Nenhum funcionário cadastrado.\n");
        return;
    }

    printf("\nLista de funcionários:\n"); // Mostra o título da listagem.

    // Percorre todos os funcionários cadastrados.
    // Em Python seria parecido com: for i in range(total):
    for (int i = 0; i < total; i++) {

        // Exibe posição, nome, cargo e salário.
        // Em Python seria parecido com:
        // print(f"{i + 1}) {nome} - {cargo} - R$ {salario:.2f}")
        printf("%d) %s - %s - R$ %.2f\n", i + 1,
               funcionarios[i].nome,
               funcionarios[i].cargo,
               funcionarios[i].salario);
    }
}

// Função responsável por buscar um funcionário pelo nome.
// Em Python seria: def buscar_funcionario():
void buscarFuncionario() {
    char nomeBusca[50]; // Guarda o nome pesquisado. Em Python seria: nome_busca = ""

    printf("Nome do funcionário: "); // Solicita o nome para busca.

    // Lê o nome pesquisado.
    // Em Python seria parecido com: nome_busca = input("Nome do funcionário: ")
    fgets(nomeBusca, 50, stdin);

    // Remove a quebra de linha do texto digitado.
    // Em Python seria parecido com: nome_busca = nome_busca.strip()
    nomeBusca[strcspn(nomeBusca, "\n")] = '\0';

    // Percorre todos os funcionários cadastrados.
    // Em Python seria parecido com: for funcionario in funcionarios:
    for (int i = 0; i < total; i++) {

        // Compara dois textos em C.
        // Em Python seria parecido com: if funcionario["nome"] == nome_busca:
        if (strcmp(funcionarios[i].nome, nomeBusca) == 0) {

            // Mostra cargo e salário do funcionário encontrado.
            // Em Python seria parecido com:
            // print(f"Cargo: {cargo} | Salário: R$ {salario:.2f}")
            printf("Cargo: %s | Salário: R$ %.2f\n",
                   funcionarios[i].cargo,
                   funcionarios[i].salario);

            return; // Sai da função após encontrar o funcionário.
        }
    }

    printf("Funcionário não encontrado.\n"); // Mensagem caso o nome não seja encontrado.
}
