using System.Globalization;

namespace Atividade_Classe_1
{
    internal class Program
    {
        static void Main(string[] args) 
        {
        
            Console.WriteLine("Entre a largura e altura do retângulo:");
            double largura = double.Parse(Console.ReadLine()!, CultureInfo.InvariantCulture);
            double altura = double.Parse(Console.ReadLine()!, CultureInfo.InvariantCulture);

            Retangulo r = new Retangulo(largura, altura);

            Console.WriteLine("AREA = " + r.Area().ToString("F2", CultureInfo.InvariantCulture));
            Console.WriteLine("PERÍMETRO = " + r.Perimetro().ToString("F2", CultureInfo.InvariantCulture));
            Console.WriteLine("DIAGONAL = " + r.Diagonal().ToString("F2", CultureInfo.InvariantCulture));
        }
    }
}
