using System.Globalization;

namespace Atividade_Estrutura_Sequencial
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Digite A, B e C separados por espaço:");
            string[] tokens = Console.ReadLine().Split(' ');
            double A = double.Parse(tokens[0], CultureInfo.InvariantCulture);
            double B = double.Parse(tokens[1], CultureInfo.InvariantCulture);
            double C = double.Parse(tokens[2], CultureInfo.InvariantCulture);

            double triangulo = (A * C) / 2.0;
            double pi = 3.14159;
            double circulo = pi * C * C;
            double trapezio = ((A + B) * C) / 2.0;
            double quadrado = B * B;
            double retangulo = A * B;

            Console.WriteLine("TRIANGULO: " + triangulo.ToString("F3", CultureInfo.InvariantCulture));
            Console.WriteLine("CIRCULO: " + circulo.ToString("F3", CultureInfo.InvariantCulture));
            Console.WriteLine("TRAPEZIO: " + trapezio.ToString("F3", CultureInfo.InvariantCulture));
            Console.WriteLine("QUADRADO: " + quadrado.ToString("F3", CultureInfo.InvariantCulture));
            Console.WriteLine("RETANGULO: " + retangulo.ToString("F3", CultureInfo.InvariantCulture));

        }
    }
}
