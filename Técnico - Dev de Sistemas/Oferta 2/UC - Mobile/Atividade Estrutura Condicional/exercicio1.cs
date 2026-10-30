namespace Atividade_Estrutura_Condicional
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Digite um número: ");
            int n = int.Parse(Console.ReadLine());

            if (n % 2 == 0) {
                Console.WriteLine("Esse número é par.");
            }
            else
            {
                Console.WriteLine("Esse número é impar.");
            }
        }
    }
}
