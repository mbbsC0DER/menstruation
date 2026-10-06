// Terminal: dotnet run
Console.Write("Enter your name: ");
var name = Console.ReadLine()?.Trim();
Console.WriteLine($"Hello, {name}! Welcome to the Simple Application.");
while (true)
{
    Console.Write("Enter a number to square (or quit): ");
    var input = Console.ReadLine();
    if (input is null || input.Trim().Equals("quit", StringComparison.OrdinalIgnoreCase)) break;
    if (int.TryParse(input, out int number))
        Console.WriteLine($"The square of {number} is {(long)number * number}.");
    else Console.WriteLine("Invalid input. Enter an integer or quit.");
}
Console.WriteLine("Testing complete.");
