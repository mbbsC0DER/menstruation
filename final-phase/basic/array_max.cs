using System;

class Program
{
    static void Main()
    {
        int[] a = { 10, 25, 5, 40, 15 };

        int largest = a[0];

        for (int i = 1; i < a.Length; i++)
        {
            if (a[i] > largest)
                largest = a[i];
        }

        Console.WriteLine("Largest = " + largest);
    }
}