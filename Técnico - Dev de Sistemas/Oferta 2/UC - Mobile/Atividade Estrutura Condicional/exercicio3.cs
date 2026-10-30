using System;

namespace Atividade_Estrutura_Condicional
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Digite a hora inicial e final de um jogo (com espaçamento): ");
            string[] parts = Console.ReadLine().Split(' ');
            int inicio = int.Parse(parts[0]);
            int fim = int.Parse(parts[1]);

            int duracao;
            if (inicio == fim)
                duracao = 24;
            else if (fim > inicio)
                duracao = fim - inicio;
            else
                duracao = (24 - inicio) + fim;

            Console.WriteLine($"O JOGO DUROU {duracao} HORA(S)");
        }
    }
}
