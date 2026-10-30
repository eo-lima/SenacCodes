using System.Globalization;

namespace Atividade_Estrutura_Sequencial
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Digite os dados da peca 1 (codigo, numero, valor):");
            string[] peca1 = Console.ReadLine().Split(' ');
            int codigo1 = int.Parse(peca1[0]);
            int numero1 = int.Parse(peca1[1]);
            double valor1 = double.Parse(peca1[2], CultureInfo.InvariantCulture);

            double total1 = valor1 * numero1;

            Console.WriteLine("Digite os dados da peca 2 (codigo, numero, valor):");
            string[] peca2 = Console.ReadLine().Split(' ');
            int codigo2 = int.Parse(peca2[0]);
            int numero2 = int.Parse(peca2[1]);
            double valor2 = double.Parse(peca2[2], CultureInfo.InvariantCulture);

            double total2 = valor2 * numero2;

            Console.WriteLine($"Valor a pagar: R${(total1 + total2).ToString("F2", CultureInfo.InvariantCulture)}");

        }
    }
}