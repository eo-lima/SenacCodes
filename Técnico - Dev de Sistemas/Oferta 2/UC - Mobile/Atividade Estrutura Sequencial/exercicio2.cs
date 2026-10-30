    namespace AtividadeCS
{
    internal class Program
    {
        static void Main(string[] args)
        {   
            Console.WriteLine("Digite o valor do raio de um círculo: ");
            double raio = double.Parse(Console.ReadLine());

            double pi = 3.14159;
            double area = pi * (raio*2);
            Console.WriteLine($"Àrea: {area}");
        }
    }
}