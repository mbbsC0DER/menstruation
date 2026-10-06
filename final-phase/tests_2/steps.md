# Practical 2: Calculator API and a separate xUnit testing project

Source: `asp pract no 2.docx`.

## Visual Studio 2026 setup

Install **ASP.NET and web development** and the **.NET 10 SDK** through **Visual Studio Installer → Modify**. Both projects target .NET 10. [VS 2026 compatibility](https://learn.microsoft.com/en-us/visualstudio/releases/2026/compatibility).

## Open and test the supplied projects

1. **File → Open → Project/Solution** → `CalculatorAPI/CalculatorAPI.csproj`.
2. In Solution Explorer right-click the **solution** (not the project) → **Add → Existing Project**.
3. Select `CalculatorTests/CalculatorTests.csproj`. Both projects should now appear in the solution.
4. If Solution Explorer displays only the project, create a blank solution via **File → New → Project → Blank Solution**, name it **CalculatorTesting**, then **Add → Existing Project** for both `.csproj` files.
5. Right-click the solution → **Restore NuGet Packages**. The test project's project reference is already configured.
6. **Build → Build Solution** (Ctrl+Shift+B).
7. **Test → Test Explorer**. Click **Run All Tests**.
8. Expected: **6 passed, 0 failed**. The tests cover add, subtract, multiply, normal division, fractional division, and divide-by-zero.
9. To show the web API too, right-click **CalculatorAPI → Set as Startup Project**, select its project launch profile, and press **Ctrl+F5**.
10. Open `http://localhost:5202/calculate?operation=add&a=10&b=5`: output `{"result":15}`.
11. Change `operation` to `subtract`, `multiply`, or `divide`: expected results 5, 50, and 2. Divide by zero returns HTTP 400.

## Create the solution yourself instead

1. **File → New → Project → ASP.NET Core Web API**.
2. Project **CalculatorAPI**, solution **CalculatorTesting**, framework **.NET 10.0**, authentication **None**, HTTPS off, containers off, template OpenAPI off.
3. Replace the API `.csproj`, Program.cs, Services folder, and Properties folder with the supplied files. Remove template controllers/example endpoints; the supplied Program.cs contains the complete API.
4. Right-click the solution → **Add → New Project → xUnit Test Project**, name **CalculatorTests**, framework **.NET 10.0**.
5. Replace its `.csproj` with the supplied version and delete the generated test file. Add the supplied `CalculatorTests.cs`.
6. Under **CalculatorTests → Dependencies**, the CalculatorAPI project reference must appear. If it does not, right-click Dependencies → **Add Project Reference → CalculatorAPI → OK**.
7. Restore, build, and run the tests in Test Explorer as above. The included package versions use xUnit v2 with a Visual Studio runner; do not mix a different generated test framework into these files.

## Terminal commands

In **View → Terminal**, change to `tests_2`:

```powershell
dotnet restore CalculatorTests/CalculatorTests.csproj
dotnet test CalculatorTests/CalculatorTests.csproj
dotnet run --project CalculatorAPI/CalculatorAPI.csproj
```

Package and project references are already in the test `.csproj`; no manual test-package installation is needed.

## Code files

- `CalculatorAPI/Program.cs`: API setup and calculation endpoint.
- `CalculatorAPI/Services/CalculatorService.cs`: the four operations.
- `CalculatorTests/CalculatorTests.cs`: six independent assertions.
- Each project includes its `.csproj`; the API includes a fixed-port launch profile.

The code and CLI commands are also included as comments in the relevant source files.
