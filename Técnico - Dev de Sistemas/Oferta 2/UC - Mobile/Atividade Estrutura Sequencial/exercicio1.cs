namespace AtividadeCS
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Digite um número: ");
            int n1 = int.Parse(Console.ReadLine());
            Console.WriteLine("Digite outro número: ");
            int n2 = int.Parse(Console.ReadLine());

            Console.WriteLine($"Soma: {n1+n2}");
        }
    }
}