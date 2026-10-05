using System;
using System.Globalization;
using System.Reflection.Metadata;

namespace Primeiro_Projeto
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Entre com seu nome completo: ");
            string nome = Console.ReadLine();
            Console.WriteLine("Quantos quartos tem na sua casa? ");
            int quartos = int.Parse(Console.ReadLine());
            Console.WriteLine("Entre com o preço de um produto: ");
            float preco = float.Parse(Console.ReadLine());
            Console.WriteLine("Entre seu último nome, idade e altura (mesma linha): ");
            string[] v = Console.ReadLine().Split(' ');
            string vetornome = v[0];
            int vetoridade = int.Parse(v[1]);
            float vetoraltura = float.Parse(v[2]);
            Console.WriteLine(nome);
            Console.WriteLine(quartos);
            Console.WriteLine(preco);
            Console.WriteLine(vetornome);
            Console.WriteLine(vetoridade);
            Console.WriteLine(vetoraltura);
             


        }
    }
}