using System;

class Program
{
    static void Main()
    {
        Console.Write("Enter first number: ");
        int a = Convert.ToInt32(Console.ReadLine());

        Console.Write("Enter second number: ");
        int b = Convert.ToInt32(Console.ReadLine());

        Console.Write("Enter operator (+, -, *, /): ");
        char op = Convert.ToChar(Console.ReadLine());

        switch (op)
        {
            case '+':
                Console.WriteLine(a + b);
                break;

            case '-':
                Console.WriteLine(a - b);
                break;

            case '*':
                Console.WriteLine(a * b);
                break;

            case '/':
                Console.WriteLine(a / b);
                break;

            default:
                Console.WriteLine("Invalid operator");
                break;
        }
    }
}