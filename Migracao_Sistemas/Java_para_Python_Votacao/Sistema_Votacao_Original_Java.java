import java.util.*; // Importa bibliotecas utilitárias do Java.
// Em Python seria parecido com usar import.

public class SistemaDeVotacao {

    public static void main(String[] args) {

        // Scanner utilizado para entrada de dados pelo teclado.
        // Em Python normalmente usamos input().
        Scanner scanner = new Scanner(System.in);

        // Vetor contendo opções da votação.
        // Em Python seria parecido com:
        // opcoes = ["Opção 1", "Opção 2", "Opção 3"]
        String[] opcoes = {"Opção 1", "Opção 2", "Opção 3"};

        // Vetor que armazena quantidade de votos.
        // Em Python seria parecido com:
        // votos = [0, 0, 0]
        int[] votos = new int[opcoes.length];

        // Variável booleana que controla execução do sistema.
        // Em Python seria:
        // votacao_ativa = True
        boolean votacaoAtiva = true;

        System.out.println("=== SISTEMA DE VOTAÇÃO ===");

        System.out.println("As opções são:");

        // Estrutura de repetição para mostrar opções disponíveis.
        // Em Python seria parecido com:
        // for i in range(len(opcoes)):
        for (int i = 0; i < opcoes.length; i++) {

            // Exibe número e nome da opção.
            // Em Python seria:
            // print(f"{i + 1} - {opcoes[i]}")
            System.out.println((i + 1) + " - " + opcoes[i]);
        }

        // Estrutura principal da votação.
        // Em Python seria parecido com:
        // while votacao_ativa:
        while (votacaoAtiva) {

            System.out.print("\nEscolha uma opção (1-" + opcoes.length + ") ou 0 para encerrar: ");

            // Verifica se usuário digitou número inteiro.
            // Em Python normalmente usaríamos try/except.
            if (scanner.hasNextInt()) {

                // Recebe número digitado pelo usuário.
                // Em Python seria:
                // escolha = int(input())
                int escolha = scanner.nextInt();

                // Verifica se usuário escolheu encerrar sistema.
                // Em Python seria:
                // if escolha == 0:
                if (escolha == 0) {

                    votacaoAtiva = false;

                // Verifica se opção está dentro do limite válido.
                // Em Python seria:
                // elif escolha >= 1 and escolha <= len(opcoes):
                } else if (escolha >= 1 && escolha <= opcoes.length) {

                    // Soma 1 voto na opção escolhida.
                    // Em Python seria:
                    // votos[escolha - 1] += 1
                    votos[escolha - 1]++;

                    // Exibe opção votada.
                    // Em Python seria:
                    // print(f"Você votou na {opcoes[escolha - 1]}")
                    System.out.println("Você votou na " + opcoes[escolha - 1]);

                } else {

                    // Caso usuário digite número inválido.
                    System.out.println("Opção inválida. Tente novamente.");
                }

            } else {

                // Caso usuário digite texto ou caractere inválido.
                System.out.println("Entrada inválida. Digite apenas números.");

                // Descarta valor inválido digitado.
                // Em Python normalmente usaríamos tratamento de erro.
                scanner.next();
            }
        }

        System.out.println("\n=== RESULTADOS FINAIS ===");

        // Percorre todas as opções para exibir total de votos.
        // Em Python seria parecido com:
        // for i in range(len(opcoes)):
        for (int i = 0; i < opcoes.length; i++) {

            // Exibe nome da opção e quantidade de votos.
            // Em Python seria:
            // print(f"{opcoes[i]}: {votos[i]} voto(s)")
            System.out.println(opcoes[i] + ": " + votos[i] + " voto(s)");
        }

        // Fecha Scanner corretamente.
        // Em Python normalmente não precisamos fechar input().
        scanner.close();
    }
}