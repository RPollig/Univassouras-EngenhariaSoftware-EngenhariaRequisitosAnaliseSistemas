import java.util.*; // Importa bibliotecas utilitárias do Java.
// Em Python seria parecido com importar bibliotecas usando: import

public class SistemaAlunos {

    // HashMap funciona como um dicionário.
    // Em Python seria parecido com:
    // notas = {}
    static HashMap<String, Double> notas = new HashMap<>();

    // ArrayList funciona como uma lista dinâmica.
    // Em Python seria parecido com:
    // lista_nomes = []
    static ArrayList<String> listaNomes = new ArrayList<>();

    public static void main(String[] args) {

        // Scanner é utilizado para entrada de dados pelo teclado.
        // Em Python normalmente usamos input().
        Scanner sc = new Scanner(System.in);

        int opcao; // Variável inteira que guarda opção do menu.
        // Em Python seria: opcao = 0

        // Estrutura de repetição principal do sistema.
        // Em Python seria parecido com:
        // while opcao != 0:
        do {

            System.out.println("\n=== SISTEMA DE ALUNOS ===");

            System.out.println("1 - Adicionar aluno");

            System.out.println("2 - Listar alunos");

            System.out.println("3 - Buscar nota");

            System.out.println("0 - Sair");

            System.out.print("Opção: ");

            // Lê número inteiro digitado pelo usuário.
            // Em Python seria:
            // opcao = int(input("Opção: "))
            opcao = sc.nextInt();

            // Limpa quebra de linha do buffer.
            sc.nextLine();

            // Estrutura de decisão.
            // Em Python seria parecido com if / elif / else.
            switch (opcao) {

                case 1:

                    // Chama função para adicionar aluno.
                    // Em Python seria:
                    // adicionar_aluno()
                    adicionarAluno(sc);

                    break;

                case 2:

                    // Chama função para listar alunos.
                    listarAlunos();

                    break;

                case 3:

                    // Chama função para buscar nota.
                    buscarNota(sc);

                    break;

                case 0:

                    System.out.println("Encerrando...");

                    break;

                default:

                    System.out.println("Opção inválida!");

                    break;
            }

        } while (opcao != 0);

        // Fecha Scanner corretamente.
        // Em Python normalmente não precisamos fechar input().
        sc.close();
    }

    // Função responsável por adicionar aluno.
    // Em Python seria:
    // def adicionar_aluno():
    public static void adicionarAluno(Scanner sc) {

        System.out.print("Nome do aluno: ");

        // Recebe texto digitado pelo usuário.
        // Em Python seria:
        // nome = input("Nome do aluno: ")
        String nome = sc.nextLine();

        System.out.print("Nota final: ");

        // Recebe número decimal.
        // Em Python seria:
        // nota = float(input("Nota final: "))
        double nota = sc.nextDouble();

        // Adiciona valor dentro do HashMap.
        // Em Python seria:
        // notas[nome] = nota
        notas.put(nome, nota);

        // Adiciona nome dentro da lista.
        // Em Python seria:
        // lista_nomes.append(nome)
        listaNomes.add(nome);

        System.out.println("Aluno cadastrado com sucesso!");
    }

    // Função responsável por listar alunos cadastrados.
    // Em Python seria:
    // def listar_alunos():
    public static void listarAlunos() {

        // Verifica se lista está vazia.
        // Em Python seria:
        // if len(lista_nomes) == 0:
        if (listaNomes.isEmpty()) {

            System.out.println("Nenhum aluno cadastrado.");

            return;
        }

        System.out.println("\nLista de alunos:");

        // Estrutura foreach.
        // Em Python seria parecido com:
        // for nome in lista_nomes:
        for (String nome : listaNomes) {

            // Busca nota do aluno no HashMap.
            // Em Python seria:
            // notas[nome]
            System.out.println("- " + nome + " | Nota: " + notas.get(nome));
        }
    }

    // Função responsável por buscar nota de um aluno.
    // Em Python seria:
    // def buscar_nota():
    public static void buscarNota(Scanner sc) {

        System.out.print("Nome do aluno: ");

        // Recebe nome digitado.
        // Em Python seria:
        // nome = input("Nome do aluno: ")
        String nome = sc.nextLine();

        // Verifica se nome existe dentro do HashMap.
        // Em Python seria parecido com:
        // if nome in notas:
        if (notas.containsKey(nome)) {

            // Exibe nota encontrada.
            // Em Python seria:
            // print(f"Nota de {nome}: {notas[nome]}")
            System.out.println("Nota de " + nome + ": " + notas.get(nome));

        } else {

            System.out.println("Aluno não encontrado.");
        }
    }
}