using System;

class Student
{
    public string name = "Asmi";
    public int age = 20;

    public void Display()
    {
        Console.WriteLine("Name = " + name);
        Console.WriteLine("Age = " + age);
    }
}

class Program
{
    static void Main()
    {
        Student s = new Student();
        s.Display();
    }
}