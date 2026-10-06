using System;

class Animal
{
    public void Eat()
    {
        Console.WriteLine("Animal eats");
    }
}

class Dog : Animal
{
    public void Bark()
    {
        Console.WriteLine("Dog barks");
    }
}

class Program
{
    static void Main()
    {
        Dog d = new Dog();

        d.Eat();
        d.Bark();
    }
}