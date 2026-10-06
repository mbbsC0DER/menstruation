// Terminal (in tests_2): dotnet test CalculatorTests/CalculatorTests.csproj
using CalculatorAPI;
using Xunit;
public class CalculatorTests
{
    private readonly CalculatorService calculator = new();
    [Fact] public void Addition() => Assert.Equal(15, calculator.Add(10, 5));
    [Fact] public void Subtraction() => Assert.Equal(5, calculator.Subtract(10, 5));
    [Fact] public void Multiplication() => Assert.Equal(50, calculator.Multiply(10, 5));
    [Fact] public void Division() => Assert.Equal(2, calculator.Divide(10, 5));
    [Fact] public void FractionalDivision() => Assert.Equal(2.5, calculator.Divide(5, 2));
    [Fact] public void DivideByZero() => Assert.Throws<DivideByZeroException>(() => calculator.Divide(10, 0));
}
