using System.Globalization;
using System.Runtime.CompilerServices;
namespace AtividadeCS
{
    internal class Program
    {
        static void Main(string[] args)
        {
            double xA, xB, xC, yA, yB, yC;
            Console.WriteLine("Entre com as medidas do triângulo X: ");
            xA = double.Parse(Console.ReadLine());
            xB = double.Parse(Console.ReadLine());
            xC = double.Parse(Console.ReadLine());

            Console.WriteLine("Entre com as medidas do triângulo Y: ");
            yA = double.Parse(Console.ReadLine());
            yB = double.Parse(Console.ReadLine());
            yC = double.Parse(Console.ReadLine());

            double p = (xA + xB + xC)/2.0;
            double areax = Math.Sqrt(p * (p-xA) * (p-xB) * (p-xC));

            p = (yA + yB + yC)/2.0;
            double areay = Math.Sqrt(p * (p-yA) * (p-yB) * (p-yC));

            Console.WriteLine($"Área do Triângulo X: {areax.ToString("F4")}");
            Console.WriteLine($"Área do Triângulo Y: {areay.ToString("F4")}");

            if (areax > areay)
            {
                Console.WriteLine("A área do triângulo X é maior.");
            }
            else
            {
                Console.WriteLine("A área do triângulo Y é maior.");
            }

        }
    }
}
