namespace AtividadeCS
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Digite o número do funcionário: ");
            int numero = int.Parse(Console.ReadLine());
            Console.WriteLine("Digite o número de horas trabalhadas: ");
            int horas = int.Parse(Console.ReadLine());
            Console.WriteLine("Digite o seu salário por hora: ");
            double salario = double.Parse(Console.ReadLine());

            Console.WriteLine($"NUMBER: {numero}");
            Console.WriteLine($"SALARY: U$ {horas * salario}");
        }
    }
}