using System;

class Program
{
    static void Main()
    {
        try
        {
            Console.Write("Enter a number: ");
            int n = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine(10 / n);
        }
        catch
        {
            Console.WriteLine("Error occurred");
        }
    }
}