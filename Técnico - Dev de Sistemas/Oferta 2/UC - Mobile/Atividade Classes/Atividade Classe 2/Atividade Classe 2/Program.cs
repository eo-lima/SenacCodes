using System.Globalization;

namespace Atividade_Classe_2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Nome: ");
            string nome = Console.ReadLine()!;
            Console.Write("Salário bruto: ");
            double bruto = double.Parse(Console.ReadLine()!, CultureInfo.InvariantCulture);
            Console.Write("Imposto: ");
            double imposto = double.Parse(Console.ReadLine()!, CultureInfo.InvariantCulture);

            Funcionario f = new Funcionario(nome, bruto, imposto);

            Console.WriteLine();
            Console.WriteLine("Funcionário: " + f);

            Console.WriteLine();
            Console.Write("Digite a porcentagem para aumentar o salário: ");
            double porcentagem = double.Parse(Console.ReadLine()!, CultureInfo.InvariantCulture);
            f.AumentarSalario(porcentagem);

            Console.WriteLine();
            Console.WriteLine("Dados atualizados: " + f);
        }
    }
}
