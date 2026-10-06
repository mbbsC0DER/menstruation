// Terminal: dotnet run
using CalculatorAPI;
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddScoped<CalculatorService>();
var app = builder.Build();
app.MapGet("/", () => "Calculator API: try /calculate?operation=add&a=10&b=5");
app.MapGet("/calculate", (string operation, double a, double b, CalculatorService calculator) =>
{
    operation = operation.ToLowerInvariant();
    if (operation == "divide" && b == 0) return Results.BadRequest("Cannot divide by zero.");
    double? result = operation switch
    {
        "add" => calculator.Add(a, b), "subtract" => calculator.Subtract(a, b),
        "multiply" => calculator.Multiply(a, b), "divide" when b != 0 => calculator.Divide(a, b),
        _ => null
    };
    return result is null ? Results.BadRequest("Use add, subtract, multiply or divide.") : Results.Ok(new { result });
});
app.Run();
