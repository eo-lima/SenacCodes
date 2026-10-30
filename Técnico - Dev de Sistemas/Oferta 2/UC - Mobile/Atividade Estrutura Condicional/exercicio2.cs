using System;

namespace Atividade_Estrutura_Condicional
{
    internal class Program2
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Digite 2 números (A e B) com espaçamento:");
            string[] n = Console.ReadLine().Split(' ');
            int a = int.Parse(n[0]);
            int b = int.Parse(n[1]);

            if (a % b == 0 || b % a == 0)
            {
                Console.WriteLine("São multiplos.");
            }
            else
            {
                Console.WriteLine("Não são multiplos.");
            }
        }
    }
}
