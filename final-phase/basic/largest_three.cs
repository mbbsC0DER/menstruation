using System;

class Program
{
    static void Main()
    {
        Console.Write("Enter three numbers: ");
        int a = Convert.ToInt32(Console.ReadLine());
        int b = Convert.ToInt32(Console.ReadLine());
        int c = Convert.ToInt32(Console.ReadLine());

        if (a >= b && a >= c)
            Console.WriteLine("Largest = " + a);
        else if (b >= a && b >= c)
            Console.WriteLine("Largest = " + b);
        else
            Console.WriteLine("Largest = " + c);
    }
}