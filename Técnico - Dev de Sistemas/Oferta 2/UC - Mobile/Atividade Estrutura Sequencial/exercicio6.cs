using System.Globalization;

namespace Atividade_Estrutura_Sequencial
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            if (n < 0)
                Console.WriteLine("NEGATIVO");
            else
                Console.WriteLine("NAO NEGATIVO");
        }
    }
}
